import numpy as np
from state import State
# The values for rows and columns are the same for both rewards tables and Q tables
# This is the one place where you can change the numbers for both at the same time
class ConfigTable:
    rows = 4
    columns = 4
    table = np.zeros((rows, columns), dtype=int)
    cellIndex = []
    
    @staticmethod 
    def createTableIds():
        id = 0
        for i in range(ConfigTable.rows):
            for j in range(ConfigTable.columns):
                id = id + 1
                ConfigTable.table[i, j] = id

    @staticmethod
    def getCellIndex(state):
        idx = ConfigTable.table[state.row, state.column]
        return idx - 1

    @staticmethod
    def getListIndex(state):
        cellIdx = ConfigTable.getCellIndex(state)
        idx = ConfigTable.cellIndex[cellIdx]
        return idx