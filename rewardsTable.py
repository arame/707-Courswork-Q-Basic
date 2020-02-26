from configRewards import ConfigRewards
from configTable import ConfigTable
import numpy as np

class RewardsTable:
    def __init__(self):
        self.rows = ConfigTable.rows
        self.columns = ConfigTable.columns
        self.origRewardValues = {"1": ConfigRewards.cell_clean, 
                            "2":ConfigRewards.cell_clean, 
                            "3": ConfigRewards.cell_clean, 
                            "4": ConfigRewards.cell_clean, 
                            "5": ConfigRewards.cell_clean,
                            "6": ConfigRewards.cell_clean,
                            "7": ConfigRewards.cell_dirty,
                            "8": ConfigRewards.cell_clean,
                            "9": ConfigRewards.cell_inaccessible,
                            "10": ConfigRewards.cell_clean,
                            "11": ConfigRewards.cell_clean,
                            "12": ConfigRewards.cell_dirty,
                            "13": ConfigRewards.cell_clean,
                            "14": ConfigRewards.cell_inaccessible,
                            "15": ConfigRewards.cell_dirty,
                            "16": ConfigRewards.cell_inaccessible,
                            "17": ConfigRewards.cell_clean,
                            "18": ConfigRewards.cell_dirty,
                            "19": ConfigRewards.cell_inaccessible,
                            "20": ConfigRewards.cell_clean,
                            "21": ConfigRewards.cell_inaccessible,
                            "22": ConfigRewards.cell_clean,
                            "23": ConfigRewards.cell_clean,
                            "24": ConfigRewards.cell_clean,
                            "25": ConfigRewards.cell_dirty
                            }
        self.rewardValues =  self.origRewardValues.copy()

        self.noDirtyCells = 0
        for r in self.rewardValues:
            value = self.rewardValues.get(r)
            if value == ConfigRewards.cell_dirty:
                self.noDirtyCells += 1

        self.table = np.zeros((self.rows, self.columns), dtype=int)
        k = 0
        for i in range(self.rows):
            for j in range(self.columns):
                k = k + 1
                self.table[i, j] = k
        print("Rewards table created")

    def resetRewardValues(self):
        self.rewardValues =  self.origRewardValues.copy()

    def getReward(self, idx):
        reward = self.rewardValues.get(str(idx))
        return reward

    def setRewardToClean(self, idx):
        self.rewardValues[str(idx)] = ConfigRewards.cell_clean
        