from BlockchainUtils import BlockchainUtils
from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from p2p.Message import Message
from p2p.SocketCommunication import SocketCommunication
from rest.NodeAPI import NodeAPI
import sys

class Node():
    
    def __init__(self, ip, port, key_file = None):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        if key_file is not None:
            self.wallet.from_key(sys.path[0] + key_file)

    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket_communication(self)

    def start_api(self, api_port):
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(api_port)

    def handle_transaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signer_public_key = transaction.sender_public_key
        signature_valid = Wallet.signature_valid(data, signature, signer_public_key)
        transaction_exists = self.transaction_pool.transaction_exists(transaction)
        transaction_in_block = self.blockchain.transaction_exists(transaction)
        if not transaction_exists and not transaction_in_block and signature_valid:
            self.transaction_pool.add_transaction(transaction)
            message = Message(self.p2p.socket_connector, 'TRANSACTION', transaction)
            encoded_message = BlockchainUtils.encode(message)
            self.p2p.broadcast(encoded_message)
            # its time to select a new forger?
            if self.transaction_pool.forger_required():
                self.forge()

    def handle_block(self, block):
        block_count_valid = self.blockchain.block_count_valid(block)
        last_block_hash_valid = self.blockchain.last_block_hash_valid(block)
        forger_valid = self.blockchain.forger_valid(block)
        transactions_valid = self.blockchain.transaction_valid(block.transactions)
        signature_valid = Wallet.signature_valid(block.payload(), block.signature, block.forger)
        if last_block_hash_valid and forger_valid and transactions_valid and signature_valid and block_count_valid:
            self.blockchain.add_block(block)
            self.transaction_pool.remove_from_pool(block.transactions)
            message = Message(self.p2p.socket_connector, 'BLOCK', block)
            encoded_message = BlockchainUtils.encode(message)
            self.p2p.broadcast(encoded_message)


    def forge(self):
        forger = self.blockchain.next_forger()
        if forger == self.wallet.public_key_string():
            print('i am the next forger')
            block = self.blockchain.create_block(self.transaction_pool.transactions, self.wallet)
            self.transaction_pool.remove_from_pool(block.transactions)
            message = Message(self.p2p.socket_connector, 'BLOCK', block)
            encoded_message = BlockchainUtils.encode(message)
            self.p2p.broadcast(encoded_message)
        else:
            print('i am not the next forger')
