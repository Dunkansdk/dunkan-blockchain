class TransactionPool():

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def transaction_exists(self, transaction):
        for pool_transaction in self.transactions:
            if pool_transaction.equals(transaction):
                return True
        return False

    def remove_from_pool(self, transactions):
        new_pool_transactions = []
        for pool_transaction in self.transactions:
            insert = True
            for transaction in transactions:
                if pool_transaction.equals(transaction):
                    insert = False
            if insert:
                new_pool_transactions.append(pool_transaction)
        self.transactions = new_pool_transactions

    def forger_required(self):
        # max of transactions needed to create a new block
        return len(self.transactions) >= 2