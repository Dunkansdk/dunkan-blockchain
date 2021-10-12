import json

from p2pnetwork.node import Node
from BlockchainUtils import BlockchainUtils
from p2p.PeerDiscoveryHandler import PeerDiscoveryHandler
from p2p.SocketConnector import SocketConnector

class SocketCommunication(Node):

    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []
        self.peer_discovery_handler = PeerDiscoveryHandler(self)
        self.socket_connector = SocketConnector(ip, port)
        self.debug = True

    def connect_first_node(self):
        if self.socket_connector.port != 10001:
            self.connect_with_node('localhost', 10001)

    def start_socket_communication(self):
        self.start()
        self.peer_discovery_handler.start()
        self.connect_first_node()

    def inbound_node_connected(self, node):
        self.peer_discovery_handler.handshake(node)
        #return super().inbound_node_connected(node)

    def outbound_node_connected(self, node):
        self.peer_discovery_handler.handshake(node)
        #return super().outbound_node_connected(node)

    def node_message(self, node, data):
        data = BlockchainUtils.decode(json.dumps(data))
        if data.message_type == 'DISCOVERY':
            self.peer_discovery_handler.handle_message(data)
        return super().node_message(node, data)
 
    def send(self, receiver, data):
        self.send_to_node(receiver, data)

    def broadcast(self, data):
        self.send_to_nodes(data)