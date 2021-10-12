import pprint
import sys

from p2p.Node import Node

if __name__ == '__main__':

    ip = sys.argv[1]
    port = int(sys.argv[2])
    api_port = int(sys.argv[3])

    node = Node(ip, port)
    node.start_p2p()
    node.start_api(api_port)

    
    