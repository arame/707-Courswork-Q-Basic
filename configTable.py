import numpy as np
from state import State
# The floor plan table is divided into rows and columns
# As there are 4 rows and 4 columns, there are 16 cells.
# The Reward and Q tables have rows and columns for all 16 cells
# 
# This is the one place where you can change the numbers for both at the same time
class ConfigTable:
    dirtyCells = {9: 2, 13: 1}
    dirtyCellIndex = 0
    rows = 4
    columns = 4
    floorPlanTable = np.zeros((rows, columns), dtype=int)
    cellIndex = []

    @staticmethod 
    def createTableIds():
        ConfigTable.dirtyCellIndex = 0
        id = -1
        for i in range(ConfigTable.rows):
            for j in range(ConfigTable.columns):
                id = id + 1
                ConfigTable.floorPlanTable[i, j] = id

    @staticmethod
    def getCellIndex(state):
        idx = ConfigTable.floorPlanTable[state.row, state.column]
        return idx

    @staticmethod
    def dirtyCellIndexIncrement(state):
        idx = ConfigTable.getCellIndex(state)
        ConfigTable.dirtyCellIndex += ConfigTable.dirtyCells[idx]

    @staticmethod
    def getIndexForDirtyCellState(state):
        idx = ConfigTable.getCellIndex(state)
        return idx * 4 + ConfigTable.dirtyCellIndex
