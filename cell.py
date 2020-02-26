from configRewards import ConfigRewards
from enum import Enum

class Cell:
    def __init__(self, idx, cellType):
        self.idx = idx
        if cellType.isClean:
            self.reward = ConfigRewards.cell_clean
        if cellType.isDirty:
            self.reward = ConfigRewards.cell_dirty
        if cellType.isInaccessible:
            self.reward = ConfigRewards.cell_inaccessible
        

        self.cellType = cellType

class CellType(Enum):
    isClean = 1
    isDirty = 2
    isInaccessable = 3

