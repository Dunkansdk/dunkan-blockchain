from consensus.Lot import Lot
from consensus.ProofOfStake import ProofOfStake
from consensus.Lot import Lot

import string
import random

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('dunkan', 10)
    pos.update('bone', 100)

    dunkan_wins = 0
    bone_wins = 0

    for i in range(100):
        forger = pos.forger(get_random_string(i))
        if forger == 'dunkan':
            dunkan_wins += 1
        elif forger == 'bone':
            bone_wins += 1

    print('dunkan won: ' + str(dunkan_wins) + ' times') 
    print('bone won: ' + str(bone_wins) + ' times')
