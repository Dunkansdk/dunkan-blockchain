from consensus.Lot import Lot
from BlockchainUtils import BlockchainUtils
from eth_keys import keys
from eth_utils import decode_hex

import sys

class ProofOfStake():

    def __init__(self, private_key = None):
        self.stakers = {}
        self.genesis_node_stake(private_key)

    # Create a default staker to process transactions
    def genesis_node_stake(self, private_key = None):
        if private_key is None:
            genesis_public_key = open(sys.path[0] + '/keys/genesisPublicKey.pem', 'r').read()
        else:
            private_key_bytes = decode_hex(private_key)
            key_pair = keys.PrivateKey(private_key_bytes)
            genesis_public_key = key_pair.public_key.to_checksum_address()
        self.stakers[genesis_public_key] = 1

    def update(self, public_key_string, stake):
        if public_key_string in list(self.stakers.keys()):
            self.stakers[public_key_string] += stake
        else:
            self.stakers[public_key_string] = stake

    def get(self, public_key_string):
        if public_key_string in list(self.stakers.keys()):
            return self.stakers[public_key_string]
        else:
            return None

    def validator_lots(self, seed):
        lots = []
        for validator in list(self.stakers.keys()):
            print('Validator: ', validator)
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake + 1, seed))
        return lots
    
    def winner(self, lots, seed):
        winner_lot = None
        least_offset = None
        ref_hash_int_value = int(BlockchainUtils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lot_int_value = int(lot.lot_hash(), 16)
            offset = abs(lot_int_value - ref_hash_int_value)
            if least_offset is None or offset < least_offset:
                least_offset = offset
                winner_lot = lot
        return winner_lot

    def forger(self, last_block_hash):
        lots = self.validator_lots(last_block_hash)
        winner_lot = self.winner(lots, last_block_hash)
        return winner_lot.public_key