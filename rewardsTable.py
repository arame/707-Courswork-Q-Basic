from configRewards import ConfigRewards
from configTable import ConfigTable
import numpy as np

class RewardsTable:
    def __init__(self):
        self.rows = ConfigTable.rows
        self.columns = ConfigTable.columns
        self.dirtyCellStates = ConfigTable.dirtyCellStates
        self.rewardValues = {"1": ConfigRewards.cell_clean, 
                                "2": ConfigRewards.cell_clean, 
                                "3": ConfigRewards.cell_clean, 
                                "4": ConfigRewards.cell_clean, 
                                "5": ConfigRewards.cell_clean,
                                "6": ConfigRewards.cell_clean, 
                                "7": ConfigRewards.cell_clean, 
                                "8": ConfigRewards.cell_clean, 
                                "9": ConfigRewards.cell_clean,
                                "10": ConfigRewards.cell_clean,
                                "11": ConfigRewards.cell_clean,
                                "12": ConfigRewards.cell_clean,
                                "13": ConfigRewards.cell_clean,
                                "14": ConfigRewards.cell_clean,
                                "15": ConfigRewards.cell_clean,
                                "16": ConfigRewards.cell_clean,
                                "17": ConfigRewards.cell_clean,
                                "18": ConfigRewards.cell_clean,
                                "19": ConfigRewards.cell_clean,
                                "20": ConfigRewards.cell_clean,
                                "21": ConfigRewards.cell_clean,
                                "22": ConfigRewards.cell_clean,
                                "23": ConfigRewards.cell_clean,
                                "24": ConfigRewards.cell_clean,
                                "25": ConfigRewards.cell_clean,
                                "26": ConfigRewards.cell_clean,
                                "27": ConfigRewards.cell_clean,
                                "28": ConfigRewards.cell_clean,
                                "29": ConfigRewards.cell_finish,
                                "30": ConfigRewards.cell_clean,
                                "31": ConfigRewards.cell_clean,
                                "32": ConfigRewards.cell_clean,
                                "33": ConfigRewards.cell_clean,
                                "34": ConfigRewards.cell_inaccessible,
                                "35": ConfigRewards.cell_dirty,
                                "36": ConfigRewards.cell_inaccessible,
                                "37": ConfigRewards.cell_clean,
                                "38": ConfigRewards.cell_inaccessible,
                                "39": ConfigRewards.cell_clean,
                                "40": ConfigRewards.cell_inaccessible,
                                "41": ConfigRewards.cell_clean,
                                "42": ConfigRewards.cell_inaccessible,
                                "43": ConfigRewards.cell_dirty,
                                "44": ConfigRewards.cell_inaccessible,
                                "45": ConfigRewards.cell_clean,
                                "46": ConfigRewards.cell_inaccessible,
                                "47": ConfigRewards.cell_clean,
                                "48": ConfigRewards.cell_inaccessible,
                                "49": ConfigRewards.cell_clean,
                                "50": ConfigRewards.cell_inaccessible,
                                "51": ConfigRewards.cell_dirty,
                                "52": ConfigRewards.cell_inaccessible,
                                "53": ConfigRewards.cell_clean,
                                "54": ConfigRewards.cell_inaccessible,
                                "55": ConfigRewards.cell_clean,
                                "56": ConfigRewards.cell_inaccessible,
                                "57": ConfigRewards.cell_clean,
                                "58": ConfigRewards.cell_inaccessible,
                                "59": ConfigRewards.cell_dirty,
                                "60": ConfigRewards.cell_inaccessible,
                                "61": ConfigRewards.cell_clean,
                                "62": ConfigRewards.cell_inaccessible,
                                "63": ConfigRewards.cell_clean,
                                "64": ConfigRewards.cell_inaccessible,
                                "65": ConfigRewards.cell_clean,
                                "66": ConfigRewards.cell_dirty,
                                "67": ConfigRewards.cell_clean,
                                "68": ConfigRewards.cell_clean,
                                "69": ConfigRewards.cell_clean,
                                "70": ConfigRewards.cell_dirty,
                                "71": ConfigRewards.cell_clean,
                                "72": ConfigRewards.cell_clean,
                                "73": ConfigRewards.cell_clean,
                                "74": ConfigRewards.cell_clean,
                                "75": ConfigRewards.cell_clean,
                                "76": ConfigRewards.cell_clean,
                                "77": ConfigRewards.cell_clean,
                                "78": ConfigRewards.cell_clean,
                                "79": ConfigRewards.cell_clean,
                                "80": ConfigRewards.cell_clean,
                                "81": ConfigRewards.cell_clean,
                                "82": ConfigRewards.cell_dirty,
                                "83": ConfigRewards.cell_clean,
                                "84": ConfigRewards.cell_clean,
                                "85": ConfigRewards.cell_clean,
                                "86": ConfigRewards.cell_dirty,
                                "87": ConfigRewards.cell_clean,
                                "88": ConfigRewards.cell_clean,
                                "89": ConfigRewards.cell_clean,
                                "90": ConfigRewards.cell_clean,
                                "91": ConfigRewards.cell_clean,
                                "92": ConfigRewards.cell_clean,
                                "93": ConfigRewards.cell_clean,
                                "94": ConfigRewards.cell_clean,
                                "95": ConfigRewards.cell_clean,
                                "96": ConfigRewards.cell_clean,
                                "97": ConfigRewards.cell_inaccessible,
                                "98": ConfigRewards.cell_dirty,
                                "99": ConfigRewards.cell_clean,
                                "100": ConfigRewards.cell_clean,
                                "101": ConfigRewards.cell_inaccessible,
                                "102": ConfigRewards.cell_dirty,
                                "103": ConfigRewards.cell_clean,
                                "104": ConfigRewards.cell_clean,
                                "105": ConfigRewards.cell_inaccessible,
                                "106": ConfigRewards.cell_clean,
                                "107": ConfigRewards.cell_clean,
                                "108": ConfigRewards.cell_clean,
                                "109": ConfigRewards.cell_inaccessible,
                                "110": ConfigRewards.cell_clean,
                                "111": ConfigRewards.cell_clean,
                                "112": ConfigRewards.cell_clean,
                                "113": ConfigRewards.cell_inaccessible,
                                "114": ConfigRewards.cell_dirty,
                                "115": ConfigRewards.cell_clean,
                                "116": ConfigRewards.cell_clean,
                                "117": ConfigRewards.cell_inaccessible,
                                "118": ConfigRewards.cell_dirty,
                                "119": ConfigRewards.cell_clean,
                                "120": ConfigRewards.cell_clean,
                                "121": ConfigRewards.cell_inaccessible,
                                "122": ConfigRewards.cell_clean,
                                "123": ConfigRewards.cell_clean,
                                "124": ConfigRewards.cell_clean,
                                "125": ConfigRewards.cell_inaccessible,
                                "126": ConfigRewards.cell_clean,
                                "127": ConfigRewards.cell_clean,
                                "128": ConfigRewards.cell_clean
                                }

        noDirtyCells = 0
        for r in self.rewardValues:
            value = self.rewardValues.get(r)
            if value == ConfigRewards.cell_dirty:
                noDirtyCells += 1
        self.noDirtyCells = noDirtyCells / 4

        self.table = np.zeros(ConfigTable.table.shape, dtype=int)
        id = 0
        # for i in range(self.rows):
        #     for j in range(self.columns):
        #         for k in range(self.dirtyCellStates):
        #             id += 1
        #             self.table[i, j, k] = id
        #             print(f"row {i}, column {j}, k {k}, id {id}")
        for i in range(self.rows):
            for j in range(self.dirtyCellStates):
                for k in range(self.columns):
                
                    id += 1
                    self.table[i, j, k] = id
                    #print(f"row {i}, column {k}, k {j}, id {id}")
        print("Rewards table created")

    def getTableIndex(self, state):
        # idx = self.table[state.row, state.column, state.dirtyCellIndex]
        idx = self.table[state.row, state.dirtyCellIndex, state.column]
        return idx

    def getReward(self, state):
        idx = self.getTableIndex(state)
        index = str(idx)
        reward = self.rewardValues.get(index)
        print(f"state = ({state.row}, {state.dirtyCellIndex}, {state.column}), idx = {index}, reward = {reward}")
        return reward

    def setRewardToClean(self, idx):
        self.rewardValues[str(idx)] = ConfigRewards.cell_clean
        