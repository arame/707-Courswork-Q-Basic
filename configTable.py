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
    # This is a dictionary of table cells that the agent can be located on
    # Note that for inaccessible cells a value of -1 is assigned. 
    # The agent cannot be located on an inaccessible cell
    fromCells = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: -1, 6: 5, 7: -1, 8: 6, 9: 7, 10: 8, 11: 9, 12: -1, 13: 10, 14: 11, 15: 12}
    
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
    def getRewardTableIndex(state):
        cellIdx = ConfigTable.getCellIndex(state)
        column = cellIdx
        row = cellIdx * 4 + ConfigTable.dirtyCellIndex
        return State(row, column)

        #raise Exception(f"!! Invalid tablecell exception, for cell ({state.row}, {state.column})")

    @staticmethod
    def dirtyCellIndexIncrement(state):
        idx = ConfigTable.table[state.row, state.column]
        ConfigTable.dirtyCellIndex += ConfigTable.dirtyCells[idx]
