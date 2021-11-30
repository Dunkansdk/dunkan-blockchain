from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Block import Block
from eth_keys import keys
from eth_utils import decode_hex

import os

class Wallet():

    def __init__(self, private_key=None):
            self.key_pair = keys.PrivateKey((os.urandom(32)))            

    def from_key(self, private_key):
        if private_key:
            private_key_bytes = decode_hex(private_key)
            self.key_pair = keys.PrivateKey(private_key_bytes)

    def sign(self, data):
        data_hash = BlockchainUtils.hash(data)
        signature = self.key_pair.sign_msg_hash(data_hash.digest())
        return signature

    @staticmethod
    def signature_valid(data, signature, public_key_string):
        data_hash = BlockchainUtils.hash(data)
        public_key = signature.recover_public_key_from_msg_hash(data_hash.digest())
        signature_valid = public_key.verify_msg_hash(data_hash.digest(), signature)
        return signature_valid and public_key_string == public_key.to_checksum_address()

    def public_key_string(self):
        public_key_string = self.key_pair.public_key.to_checksum_address()
        return public_key_string

    def create_transaction(self, receiver, amount, type):
        transaction = Transaction(self.public_key_string(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction
        
    def create_block(self, transactions, last_hash, block_count):
        print('Last Hash: ', last_hash)
        block = Block(transactions, last_hash, self.public_key_string(), block_count)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
