from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

class Blockchain():
    
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.account_model = AccountModel()

    def addBlock(self, block):
        self.execute_transactions(block.transactions)
        self.blocks.append(block)

    def to_json(self):
        data = {}
        json_blocks = []
        for block in self.blocks:
            json_blocks.append(block.to_json())
        data['blocks'] = json_blocks
        return data

    def block_count_valid(self, block):
        return self.blocks[-1].block_count == block.block_count - 1

    def lastBlockHashValid(self, block):
        latestBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        return latestBlockchainBlockHash == block.last_hash

    def get_covered_transaction_set(self, transactions):
        covered_transactions = []
        for transaction in transactions:
            if self.transaction_covered(transaction):
                covered_transactions.append(transaction)
            else:
                print('Transaction is not covered by sender')
        return covered_transactions

    def transaction_covered(self, transaction):
        if transaction.type == 'EXCHANGE':
            return True

        sender_balance = self.account_model.get_balance(transaction.sender_public_key)
        return sender_balance >= transaction.amount

    # call this before append a new block
    def execute_transactions(self, transactions):
        for transaction in transactions:
            self.execute_transaction(transaction)

    def execute_transaction(self, transaction):
        sender = transaction.sender_public_key
        receiver = transaction.receiver_public_key
        amount = transaction.amount
        # substract amount
        self.account_model.update_balance(sender, -amount)
        # add amount
        self.account_model.update_balance(receiver, amount)
