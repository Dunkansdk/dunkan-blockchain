class AccountModel():

    def __init__(self):
        self.accounts = []
        self.balances = {}

    def add(self, public_key_string):
        if not public_key_string in self.accounts:
            self.accounts.append(public_key_string)
            self.balances[public_key_string] = 0

    def get_balance(self, public_key_string):
        if public_key_string not in self.accounts:
            self.add(public_key_string)
        return self.balances[public_key_string]

    def update_balance(self, public_key_string, amount):
        if public_key_string not in self.accounts:
            self.add(public_key_string)
        self.balances[public_key_string] += amount
    