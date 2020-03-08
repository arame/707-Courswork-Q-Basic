from configRewards import ConfigRewards
from configTable import ConfigTable
import numpy as np
import pandas as pd
from state import State
from state import StateType

class RewardsTable:
    def __init__(self):
        self.rows = ConfigTable.rows
        self.columns = ConfigTable.columns
        self.cellIdCount = self.rows * self.columns
        self.rewardValues = []
        self.noDirtyCellsCleaned = 0
        self.initialState = State.getInitialState()
        ConfigTable.cellIndex = []
        self.cellZeroRewards = -1 * np.ones((4),dtype=np.int16)
        self.cellZeroRewards[3] = 100
        self.cellCleanRewards = -1 * np.ones((4),dtype=np.int16)
        self.cellD1Rewards = -1 * np.ones((4),dtype=np.int16)
        self.cellD1Rewards[0] = 10
        self.cellD1Rewards[2] = 10
        self.cellD2Rewards = -1 * np.ones((4),dtype=np.int16)
        self.cellD2Rewards[0] = 10
        self.cellD2Rewards[1] = 10
        self.cellInaccessible = -100 * np.ones((4),dtype=np.int16)
        self.fromCells = [0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 13, 14, 15]

        self.dirtyCell1Id = 9
        self.dirtyCell2Id = 13
        self.inaccessible1Cell = 5
        self.inaccessible2Cell = 7
        self.inaccessible3Cell = 12
        self.noCells = 16
        self.rtableFull = []
        self.id = -1
        self.loadRTable()
        self.rtable = np.empty((0, 16))
        for row in self.rtableFull:
            self.rtable = np.append(self.rtable, [row.cellReward], axis = 0)

        
    
    def loadRTable(self):
        fromCellId = 0
        index1 = 1
        index2 = 4
        self.addRowsToTable2(fromCellId, index1, self.cellCleanRewards, index2, self.cellCleanRewards)
        fromCellId = 1
        index1 = 0
        index2 = 2
        index3 = 5
        self.addRowsToTable3(fromCellId, index1, self.cellZeroRewards, index2, self.cellCleanRewards, index3, self.cellInaccessible)
        fromCellId = 2
        index1 = 1
        index2 = 3
        index3 = 6
        self.addRowsToTable3(fromCellId, index1, self.cellCleanRewards, index2, self.cellCleanRewards, index3, self.cellCleanRewards)
        fromCellId = 3
        index1 = 2
        index2 = 7
        self.addRowsToTable2(fromCellId, index1, self.cellCleanRewards, index2, self.cellInaccessible)
        fromCellId = 4
        index1 = 0
        index2 = 5
        index3 = 8
        self.addRowsToTable3(fromCellId, index1, self.cellZeroRewards, index2, self.cellInaccessible, index3, self.cellCleanRewards)
        # Cell 5 is inaccessible so not put on the Rewards table
        fromCellId = 6
        index1 = 2
        index2 = 5
        index3 = 7
        index4 = 10
        self.addRowsToTable4(fromCellId, index1, self.cellCleanRewards, index2, self.cellInaccessible, index3, self.cellInaccessible, index4, self.cellCleanRewards)
        # Cell 7 is inaccessible so not put on the Rewards table
        fromCellId = 8
        index1 = 4
        index2 = 9
        index3 = 12
        self.addRowsToTable3(fromCellId, index1, self.cellCleanRewards, index2, self.cellD2Rewards, index3, self.cellInaccessible)
        fromCellId = 9
        index1 = 5
        index2 = 8
        index3 = 10
        index4 = 13
        self.addRowsToTable4(fromCellId, index1, self.cellInaccessible, index2, self.cellCleanRewards, index3, self.cellCleanRewards, index4, self.cellD1Rewards)
        fromCellId = 10
        index1 = 6
        index2 = 9
        index3 = 11
        index4 = 14
        self.addRowsToTable4(fromCellId, index1, self.cellCleanRewards, index2, self.cellD2Rewards, index3, self.cellCleanRewards, index4, self.cellCleanRewards)
        fromCellId = 11
        index1 = 7
        index2 = 10
        index3 = 15
        self.addRowsToTable3(fromCellId, index1, self.cellInaccessible, index2, self.cellCleanRewards, index3, self.cellCleanRewards)
        # Cell 12 is inaccessible so not put on the Rewards table    
        fromCellId = 13
        index1 = 9
        index2 = 12
        index3 = 14
        self.addRowsToTable3(fromCellId, index1, self.cellD2Rewards, index2, self.cellInaccessible, index3, self.cellCleanRewards)
        fromCellId = 14
        index1 = 10
        index2 = 13
        index3 = 15
        self.addRowsToTable3(fromCellId, index1, self.cellCleanRewards, index2, self.cellD1Rewards, index3, self.cellCleanRewards)
        fromCellId = 15
        index1 = 11
        index2 = 14
        self.addRowsToTable2(fromCellId, index1, self.cellCleanRewards, index2, self.cellCleanRewards)
    
    def addRowsToTable2(self, fromCellId, index1, items1, index2, items2):
        for i in range(4):
            self.id += 1
            row = RewardsTableRows(self.noCells)
            row.id = id
            row.fromCellId = fromCellId
            row.insert2(index1, items1[i], index2, items2[i])
            self.rtableFull.append(row)

    def addRowsToTable3(self, fromCellId, index1, items1, index2, items2, index3, items3):
        for i in range(4):
            self.id += 1
            row = RewardsTableRows(self.noCells)
            row.id = id
            row.fromCellId = fromCellId
            row.insert3(index1, items1[i], index2, items2[i], index3, items3[i])
            self.rtableFull.append(row)

    def addRowsToTable4(self, fromCellId, index1, items1, index2, items2, index3, items3, index4, items4):
        for i in range(4):
            self.id += 1
            row = RewardsTableRows(self.noCells)
            row.id = id
            row.fromCellId = fromCellId
            row.insert4(index1, items1[i], index2, items2[i], index3, items3[i], index4, items4[i])
            self.rtableFull.append(row)

    def getListIndex(self, state):
        self.cellIdx = ConfigTable.getCellIndex(state)
        idx = ConfigTable.cellIndex[self.cellIdx]
        return idx

    def getReward(self, state):
        self.index = self.getListIndex(state)
        reward = self.rewardValues[self.index]
        #print(f"state = ({state.row}, {state.column}), idx = {self.index}, reward = {reward}")
        if reward == ConfigRewards.cell_dirty:
            self.ProcessDirtyCell(state)

        return reward

class RewardsTableRows:
    def __init__(self, noOfCells):
        self.id = 0
        self.fromCellId = 0
        self.dirtyId = 0
        self.cellReward = np.zeros((noOfCells),dtype=np.int16)

    def insert2(self, index1, item1, index2, item2):
        self.cellReward[index1] = item1
        self.cellReward[index2] = item2

    def insert3(self, index1, item1, index2, item2, index3, item3):
        self.insert2(index1, item1, index2, item2)
        self.cellReward[index3] = item3

    def insert4(self, index1, item1, index2, item2, index3, item3, index4, item4):
        self.insert3(index1, item1, index2, item2, index3, item3)
        self.cellReward[index4] = item4
    