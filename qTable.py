import numpy as np
import copy
from configTable import ConfigTable
from hyperparameters import Hyperparam
from state import State
from rewardsTable import RewardsTable

class QTable:
    def __init__(self, listLength):
        # Initialise the Q_value list to equal that of the rewards table, set to zero
        self.Q_Values = [0] * listLength
        print("Q list created")

    def update(self, newState, oldState, reward):
        alpha = Hyperparam.learning_rate
        gamma = Hyperparam.discount_factor
        index_old = ConfigTable.getListIndex(oldState)
        index_new = ConfigTable.getListIndex(newState)
        q_old = self.Q_Values[index_old]
        self.q_max = max(self.Q_Values)
        #self.getMaxQValue()
        q_new = q_old + alpha * (reward + gamma * self.q_max - q_old)
        # print("-"*50)
        # print(f"Old Q = ({oldState.row}, {oldState.column}), index_old = {index_old}, old Value = {q_old}")
        # print(f"Update New Q = ({newState.row}, {newState.column}), index_new = {index_new}, new value = {q_new}, reward = {reward}")
        self.Q_Values[index_new] = q_new
        w = 0
    
    def getMaxQValue(self):
        self.maxQ = 0
        lengthTable = ConfigTable.rows * ConfigTable.columns
        for i in range(lengthTable):
            idx = ConfigTable.cellIndex[i]
            Q = self.Q_Values[idx]
            if Q > self.maxQ:
                self.maxQ = Q
    def getBestQvalue(self, state):
        x = state.row
        y = state.column
        
        self.bestState = copy.copy(state)
        self.bestQ = 0
        self.getNextQValue(x - 1, y)
        self.getNextQValue(x + 1, y)
        self.getNextQValue(x, y - 1)
        self.getNextQValue(x, y + 1)
        print(f"Best Q = {self.bestQ} ({self.bestState.row}, {self.bestState.column})")
        if self.bestQ == 0:
            return state
        return self.bestState

    def getNextQValue(self, row, column):
        if row < 0 or row >= ConfigTable.rows:
            return

        if column < 0 or column >= ConfigTable.columns:
            return 

        state = State(row, column)
        index = ConfigTable.getListIndex(state)
        Q = self.Q_Values[index]
        if Q > self.bestQ:
            self.bestQ = Q
            self.bestState = State(row, column)
