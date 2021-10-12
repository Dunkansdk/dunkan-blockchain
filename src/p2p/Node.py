from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from p2p.SocketCommunication import SocketCommunication
from rest.NodeAPI import NodeAPI

class Node():
    
    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket_communication()

    def start_api(self, api_port):
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(api_port)