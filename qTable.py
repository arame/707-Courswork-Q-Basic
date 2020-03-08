import numpy as np
import copy
from configTable import ConfigTable
from hyperparameters import Hyperparam
from state import State
from rewardsTable import RewardsTable

class QTable:
    def __init__(self, rtable):
        # Initialise the Q_value table to equal that of the rewards table, set to zero
        self.Q_Table = np.zeros(rtable.shape)
        print("Q table created")

    def update(self, newState, oldState, reward):
        alpha = Hyperparam.learning_rate
        gamma = Hyperparam.discount_factor
        old = ConfigTable.getRewardTableIndex(oldState)
        new = ConfigTable.getRewardTableIndex(newState)
        q_old = self.Q_Table[old.row, old.column]
        self.q_max = np.amax(self.Q_Table)
        #self.getMaxQValue()
        q_new = q_old + alpha * (reward + gamma * self.q_max - q_old)
        # print("-"*50)
        # print(f"Old Q = ({oldState.row}, {oldState.column}), index_old = {index_old}, old Value = {q_old}")
        # print(f"Update New Q = ({newState.row}, {newState.column}), index_new = {index_new}, new value = {q_new}, reward = {reward}")
        self.Q_Table[new.row, new.column] = q_new
    
    # def getMaxQValue(self):
    #     self.maxQ = 0
    #     lengthTable = ConfigTable.rows * ConfigTable.columns
    #     for i in range(lengthTable):
    #         idx = ConfigTable.cellIndex[i]
    #         Q = self.Q_Table[idx]
    #         if Q > self.maxQ:
    #             self.maxQ = Q
    def getBestQvalue(self, state):
        x = state.row
        y = state.column
        
        self.bestState = copy.copy(state)
        self.bestQ = 0
        self.getNextQValue(x - 1, y)
        self.getNextQValue(x + 1, y)
        self.getNextQValue(x, y - 1)
        self.getNextQValue(x, y + 1)
        #print(f"Best Q = {self.bestQ} ({self.bestState.row}, {self.bestState.column})")
        if self.bestQ == 0:
            return state
        return self.bestState

    def getNextQValue(self, row, column):
        if row < 0 or row >= ConfigTable.rows:
            return

        if column < 0 or column >= ConfigTable.columns:
            return 

        state = State(row, column)
        index = ConfigTable.getRewardTableIndex(state)
        Q = self.Q_Table[index.row, index.column]
        if Q > self.bestQ:
            self.bestQ = Q
            self.bestState = State(row, column)
