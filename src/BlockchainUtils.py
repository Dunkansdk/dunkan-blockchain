from Crypto.Hash import SHA256
import json
import jsonpickle
import eth_utils
import binascii
from Crypto.Hash import keccak

class BlockchainUtils():

    @staticmethod
    def hash(data):
        data_string = json.dumps(data)
        data_bytes = data_string.encode('utf-8')
        data_hash = keccak.new(digest_bits=256)
        data_hash.update(data_bytes)
        return data_hash

    @staticmethod
    def encode(data):
        return jsonpickle.encode(data, unpicklable=True)

    @staticmethod
    def decode(data):
        return jsonpickle.decode(data)
