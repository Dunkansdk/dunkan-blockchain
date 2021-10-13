from Wallet import Wallet
from BlockchainUtils import BlockchainUtils

import requests

if __name__ == '__main__':
    bone = Wallet()
    dunkan = Wallet()
    exchange = Wallet()

    transaction = exchange.createTransaction(dunkan.public_key_string(), 10, 'EXCHANGE')

    url = 'http://localhost:5000/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)}
    print(package)
    request = requests.post(url, json=package)
    print(request.text)
