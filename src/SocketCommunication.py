from p2pnetwork.node import Node

class SocketCommunication(Node):

    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)

    def start_socket_communication(self):
        self.start()