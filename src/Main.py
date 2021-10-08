
import pprint
from BlockchainUtils import BlockchainUtils

from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain

if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1.0
    type = 'TRANSFER'

    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()
    
    transaction = wallet.createTransaction(receiver, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    blockchain = Blockchain()

    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    block = wallet.createBlock(pool.transactions, lastHash, blockCount)

    if not blockchain.lastBlockHashValid(block):
        print('last block hash is not valid')

    if not blockchain.blockCountValid(block):
        print('last block count is not valid')

    if blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
        blockchain.addBlock(block)

    pprint.pprint(blockchain.toJson())
    