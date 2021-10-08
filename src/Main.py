
import pprint
from BlockchainUtils import BlockchainUtils

from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from AccountModel import AccountModel

if __name__ == '__main__':
    
    blockchain = Blockchain()
    pool = TransactionPool()
    
    dunkanWallet = Wallet()
    boneWallet = Wallet()
    exchangeWallet = Wallet()

    # necessary for the p2p nodes architecture
    exchangeTransaction = exchangeWallet.createTransaction(dunkanWallet.publicKeyString(), 10, 'EXCHANGE')

    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    # dunkan wants to send 5 token to bone
    transaction = dunkanWallet.createTransaction(boneWallet.publicKeyString(), 5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)

    pprint.pprint(coveredTransaction)

    
    