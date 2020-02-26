import numpy as np
from configTable import ConfigTable
from hyperparameters import Hyperparam
from state import State


class QTable:
    def __init__(self):
        self.rows = ConfigTable.rows
        self.columns = ConfigTable.columns
        self.Q_table = np.zeros((self.rows, self.columns))
        print("Q table created")

    def update(self, newState, oldState, reward):
        alpha = Hyperparam.learning_rate
        gamma = Hyperparam.discount_factor
        x_old = oldState.row
        y_old = oldState.column
        x_new = newState.row
        y_new = newState.column
        q_old = self.Q_table[x_old, y_old]
        self.calcMaxQ()
        q_new = q_old + alpha * (reward + gamma * self.q_max - q_old)
        self.Q_table[x_new, y_new] = q_new

    def calcMaxQ(self):
        self.q_max = 0
        for x in range(self.rows):
            for y in range(self.columns):
                if self.q_max < self.Q_table[x, y]:
                    self.q_max = self.Q_table[x, y]
    
    def getBestQvalue(self, state):
        x = state.row
        y = state.column
        self.bestState = State()
        self.bestQ = 0
        Q = self.getNextQValue(x - 1, y)
        self.checkIfBestQ(Q, x - 1, y)
        Q = self.getNextQValue(x + 1, y)
        self.checkIfBestQ(Q, x + 1, y)
        Q = self.getNextQValue(x, y - 1)
        self.checkIfBestQ(Q, x, y - 1)
        Q = self.getNextQValue(x, y + 1)
        self.checkIfBestQ(Q, x, y + 1)
        return self.bestState

    def getNextQValue(self, row, column):
        if row < 0 or row >= ConfigTable.rows:
            return -1

        if column < 0 or column >= ConfigTable.columns:
            return -1 

        Q = self.Q_table[row, column]
        return Q

    def checkIfBestQ(self, Q, x, y):
        if Q > self.bestQ:
            self.bestQ = Q
            self.bestState.row = x
            self.bestState.column = y
