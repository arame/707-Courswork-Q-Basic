import numpy as np
from configTable import ConfigTable
from hyperparameters import Hyperparam


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
    