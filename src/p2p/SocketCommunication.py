from p2pnetwork.node import Node
from p2p.PeerDiscoveryHandler import PeerDiscoveryHandler

class SocketCommunication(Node):

    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []
        self.peer_discovery_handler = PeerDiscoveryHandler(self)
        self.debug = True

    def start_socket_communication(self):
        self.start()
        self.peer_discovery_handler.start()

    def inbound_node_connected(self, node):
        self.send_to_node(node, 'Hey i am the node you connected to')
        return super().inbound_node_connected(node)

    def outbound_node_connected(self, node):
        self.send_to_node(node, 'Hey i am the node who initialized the connection')
        return super().outbound_node_connected(node)

    def node_message(self, node, data):
        return super().node_message(node, data)