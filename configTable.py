import numpy as np
from state import State
# The values for rows and columns are the same for both rewards tables and Q tables
# This is the one place where you can change the numbers for both at the same time
class ConfigTable:
    dirtyCells = {9: 2, 13: 1}
    dirtyCellIndex = 0
    rows = 4
    columns = 4
    table = np.zeros((rows, columns), dtype=int)
    cellIndex = []

    @staticmethod 
    def createTableIds():
        ConfigTable.dirtyCellIndex = 0
        id = -1
        for i in range(ConfigTable.rows):
            for j in range(ConfigTable.columns):
                id = id + 1
                ConfigTable.table[i, j] = id

    @staticmethod
    def getCellIndex(state):
        idx = ConfigTable.table[state.row, state.column]
        return idx

    @staticmethod
    def dirtyCellIndexIncrement(state):
        idx = ConfigTable.getCellIndex(state)
        ConfigTable.dirtyCellIndex += ConfigTable.dirtyCells[idx]

    @staticmethod
    def getIndexForDirtyCellState(state):
        idx = ConfigTable.getCellIndex(state)
        return idx * 4 + ConfigTable.dirtyCellIndex
