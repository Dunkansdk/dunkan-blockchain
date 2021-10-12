from Crypto.Hash import SHA256
import json
import jsonpickle

class BlockchainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

    @staticmethod
    def encode(data):
        return jsonpickle.encode(data, unpicklable=True)

    @staticmethod
    def decode(data):
        return jsonpickle.decode(data)
