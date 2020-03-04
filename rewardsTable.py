from configRewards import ConfigRewards
from configTable import ConfigTable
import numpy as np
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

        itemId = 0
        noDirtyCells = 0
        ConfigTable.cellIndex = []
        for i in range(self.cellIdCount):
            cellId = i + 1
            item = self.initialState[cellId]
            
            if item is StateType.start:
                self.startIndex = i
                ConfigTable.cellIndex.append(itemId)
                self.rewardValues.append(ConfigRewards.cell_clean)
                self.rewardValues.append(ConfigRewards.cell_finish)
                itemId += 2
                continue

            if item is StateType.clean:
                ConfigTable.cellIndex.append(itemId)
                self.rewardValues.append(ConfigRewards.cell_clean)
                itemId += 1
                continue  

            if item is StateType.dirty:
                ConfigTable.cellIndex.append(itemId)
                self.rewardValues.append(ConfigRewards.cell_dirty)
                self.rewardValues.append(ConfigRewards.cell_clean)
                noDirtyCells += 1
                itemId += 2
                continue              

            if item is StateType.inaccessible:
                ConfigTable.cellIndex.append(itemId)
                self.rewardValues.append(ConfigRewards.cell_inaccessible)
                itemId += 1
                continue  

        self.noDirtyCells = noDirtyCells

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

    def ProcessDirtyCell(self, state):
        self.noDirtyCellsCleaned += 1
        if self.noDirtyCellsCleaned == self.noDirtyCells:
            self.MakeStartCellFinishCell()

    def MakeStartCellFinishCell(self):
        ConfigTable.cellIndex[self.startIndex] += 1
        print("finish")
        