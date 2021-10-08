from Block import Block
from BlockchainUtils import BlockchainUtils

class Blockchain():
    
    def __init__(self):
        self.blocks = [Block.genesis()]

    def addBlock(self, block):
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data

    def blockCountValid(self, block):
        return self.blocks[-1].blockCount == block.blockCount - 1

    def lastBlockHashValid(self, block):
        latestBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        return latestBlockchainBlockHash == block.lastHash