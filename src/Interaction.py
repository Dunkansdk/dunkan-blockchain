from Wallet import Wallet
from BlockchainUtils import BlockchainUtils

import requests

if __name__ == '__main__':
    bone = Wallet()
    dunkan = Wallet()
    exchange = Wallet()

    transaction = exchange.create_transaction(dunkan.public_key_string(), 10, 'EXCHANGE')
    url = 'http://localhost:5000/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)

    transaction = exchange.create_transaction(dunkan.public_key_string(), 10, 'EXCHANGE')
    url = 'http://localhost:5001/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)

    transaction = dunkan.create_transaction(bone.public_key_string(), 10, 'TRANSACTION')
    url = 'http://localhost:5001/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)
