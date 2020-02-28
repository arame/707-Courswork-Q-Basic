import numpy as np
# The values for rows and columns are the same for both rewards tables and Q tables
# This is the one place where you can change the numbers for both at the same time
class ConfigTable:
    rows = 4
    columns = 4
    dirtyCellStates = 8
    #table = np.zeros((rows, columns, dirtyCellStates), dtype=int)
    table = np.zeros((rows, dirtyCellStates, columns), dtype=int)
    tableId = np.zeros((rows, columns), dtype=int)
    
    @staticmethod 
    def createTableIds():
        k = 0
        for i in range(ConfigTable.rows):
            for j in range(ConfigTable.columns):
                k = k + 1
                ConfigTable.tableId[i, j] = k