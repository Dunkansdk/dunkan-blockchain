import threading
import time

from p2p.Message import Message
from BlockchainUtils import BlockchainUtils

class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socket_communication = node

    def start(self):
        status_thread = threading.Thread(target=self.status, args={})
        status_thread.start()
        discovery_thread = threading.Thread(target=self.discovery, args={})
        discovery_thread.start()

    def status(self):
        while True:
            print('status')
            time.sleep(10)
    
    def discovery(self):
        while True:
            print('discovery')
            time.sleep(10)

    ## Send the data of the new peers on the network
    def handshake(self, node):
        handshake_message = self.handshake_message()
        self.socket_communication.send(node, handshake_message)

    ## Prepare message
    def handshake_message(self):
        connector = self.socket_communication.socket_connector
        data = self.socket_communication.peers
        message_type = 'DISCOVERY'
        message = Message(connector, message_type, data)
        encoded_message = BlockchainUtils.encode(message)
        return encoded_message

