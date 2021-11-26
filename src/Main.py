import argparse

from p2p.Node import Node

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", "-ip", help="Set node IP")
    parser.add_argument("--port", "-p", type=int, help="Set node port")
    parser.add_argument("--api-port", "-ap", type=int, help="Set API Port")
    parser.add_argument("--genesis-private-key", "-g", help="Set the private key for genesis block")
    parser.add_argument("--set-stakers", "-s", help="Set Validators public keys")
    parser.add_argument("--config", "-c", help="Config file (rewrite all params)")

    args = parser.parse_args()

    if args.config:
        print('// TODO')
    else:
        if not args.port or not args.ip or not args.api_port:
            print('[ERROR] Fill all fields or select a config.yml file path')
        else:
            node = Node(args.ip, args.port, args.genesis_private_key)
            node.start_p2p()
            node.start_api(args.api_port)
    