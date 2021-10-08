
import pprint
from BlockchainUtils import BlockchainUtils

from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from AccountModel import AccountModel

if __name__ == '__main__':
    
    wallet = Wallet()
    accountModel = AccountModel()

    accountModel.updateBalance(wallet.publicKeyString(), 10)
    accountModel.updateBalance(wallet.publicKeyString(), -5)

    pprint.pprint(accountModel.balances)

    
    