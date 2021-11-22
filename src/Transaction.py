import uuid
import time
import copy
from eth_keys.datatypes import Signature
import json

class Transaction():
    
    def __init__(self, sender_public_key, receiver_public_key, amount, type):
        self.sender_public_key = sender_public_key
        self.receiver_public_key = receiver_public_key
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.time = time.time()
        self.signature = ''

    def to_json(self):
        data = {}
        data['sender_public_key'] = self.sender_public_key
        data['receiver_public_key'] = self.receiver_public_key
        data['amount'] = self.amount
        data['id'] = self.id
        data['time'] = self.time
        if(self.signature != ''):
            data['signature'] = self.signature.__str__()
        return data

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        json_representation = copy.deepcopy(self.to_json())
        json_representation['signature'] = ''
        return json_representation

    ## TODO Improve this method.
    def equals(self, transaction):
        return self.id == transaction.id