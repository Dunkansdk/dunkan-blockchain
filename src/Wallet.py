from Crypto import Signature
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Block import Block

class Wallet():

    def __init__(self):
        self.key_pair = RSA.generate(2048)

    # Read the key from a file
    def from_key(self, file):
        with open(file, 'r') as keyfile:
            self.key_pair = RSA.importKey(keyfile.read())

    def sign(self, data):
        data_hash = BlockchainUtils.hash(data)
        signature_scheme = PKCS1_v1_5.new(self.key_pair)
        signature = signature_scheme.sign(data_hash)
        return signature.hex()

    @staticmethod
    def signature_valid(data, signature, public_key_string):
        signature = bytes.fromhex(signature)
        data_hash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(public_key_string)
        signature_scheme = PKCS1_v1_5.new(publicKey)
        signature_valid = signature_scheme.verify(data_hash, signature)
        return signature_valid

    def public_key_string(self):
        public_key_string = self.key_pair.publickey().exportKey('PEM').decode('utf-8')
        return public_key_string

    def create_transaction(self, receiver, amount, type):
        transaction = Transaction(self.public_key_string(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction
        
    def create_block(self, transactions, last_hash, block_count):
        block = Block(transactions, last_hash, self.public_key_string(), block_count)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
