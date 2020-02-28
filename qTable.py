import numpy as np
from configTable import ConfigTable
from hyperparameters import Hyperparam
from state import State


class QTable:
    def __init__(self):

        self.Q_table = np.zeros(ConfigTable.table.shape)
        print("Q table created")

    def update(self, newState, oldState, reward):
        alpha = Hyperparam.learning_rate
        gamma = Hyperparam.discount_factor
        x_old = oldState.row
        y_old = oldState.column
        z_old = oldState.dirtyCellIndex
        x_new = newState.row
        y_new = newState.column
        z_new = newState.dirtyCellIndex
        q_old = self.Q_table[x_old, z_old, y_old]
        self.q_max = np.max(self.Q_table)
        q_new = q_old + alpha * (reward + gamma * self.q_max - q_old)
        #print("-"*50)
        #print(f"Old Q = ({x_old}, {z_old}, {y_old}), {q_old}")
        #print(f"Update New Q = ({x_new}, {z_new}, {y_new}), {q_new}")
        self.Q_table[x_new, z_new, y_new] = q_new
    
    def getBestQvalue(self, state):
        x = state.row
        y = state.column
        z = state.dirtyCellIndex
        
        self.bestState = State()
        self.bestQ = 0
        self.getNextQValue(x - 1, y, z)
        self.getNextQValue(x + 1, y, z)
        self.getNextQValue(x, y - 1, z)
        self.getNextQValue(x, y + 1, z)
        #print(f"Best Q = {self.bestQ} ({self.bestState.row}, {self.bestState.dirtyCellIndex}, {self.bestState.column})")
        if self.bestQ == 0:
            return state
        return self.bestState

    def getNextQValue(self, row, column, dirtyCellIndex):
        if row < 0 or row >= ConfigTable.rows:
            return -1

        if column < 0 or column >= ConfigTable.columns:
            return -1 

        # Q = self.Q_table[row, column, dirtyCellIndex]
        Q = self.Q_table[row, dirtyCellIndex, column]
        if Q > self.bestQ:
            self.bestQ = Q
            self.bestState.row = row
            self.bestState.column = column
            self.bestState.dirtyCellIndex = dirtyCellIndex
