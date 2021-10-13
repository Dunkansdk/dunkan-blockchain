import threading
import time

from p2p.Message import Message
from BlockchainUtils import BlockchainUtils

class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socket_communication = node

    def start(self):
    #    status_thread = threading.Thread(target=self.status, args={})
    #    status_thread.start()
        discovery_thread = threading.Thread(target=self.discovery, args={})
        discovery_thread.start()
    
    '''
    def status(self):
        while True:
            print('Currenct Connections:')
            for peer in self.socket_communication.peers:
                print(str(peer.ip) + ':' + str(peer.port))
            time.sleep(10)
    '''

    def discovery(self):
        while True:
            handshake_message = self.handshake_message()
            self.socket_communication.broadcast(handshake_message)
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

    # Replicate message to all nodes
    def handle_message(self, message):
        peers_socket_connector = message.sender_connector
        peers_peer_list = message.data
        new_peer = True

        for peer in self.socket_communication.peers:
            if peer.equals(peers_socket_connector):
                new_peer = False

        if new_peer:
            self.socket_communication.peers.append(peers_socket_connector)

        for peers_peer in peers_peer_list:
            peer_know = False
            for peer in self.socket_communication.peers:
                if peer.equals(peers_peer):
                    peer_know = True
            if not peer_know and not peers_peer.equals(self.socket_communication.socket_connector):
                self.socket_communication.connect_with_node(peers_peer.ip, peers_peer.port)
            