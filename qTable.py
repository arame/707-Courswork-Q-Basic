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
        old = ConfigTable.getIndexForDirtyCellState(oldState)
        new = ConfigTable.getCellIndex(newState)
        q_old = self.Q_Table[old, new]
        self.q_max = np.amax(self.Q_Table)
        q_new = q_old + alpha * (reward + gamma * self.q_max - q_old)
        # print("-"*50)
        # print(f"Old Q = ({oldState.row}, {oldState.column}), index_old = {index_old}, old Value = {q_old}")
        # print(f"Update New Q = ({newState.row}, {newState.column}), index_new = {index_new}, new value = {q_new}, reward = {reward}")
        self.Q_Table[old, new] = q_new
    
    def getBestQvalue(self, state):
        x = state.row
        y = state.column
        
        self.bestState = copy.copy(state)
        self.bestQ = 0
        self.getNextQValue(state, State(x - 1, y))
        self.getNextQValue(state, State(x + 1, y))
        self.getNextQValue(state, State(x, y - 1))
        self.getNextQValue(state, State(x, y + 1))
        #print(f"Best Q = {self.bestQ} ({self.bestState.row}, {self.bestState.column})")
        if self.bestQ == 0:
            return state
        return self.bestState

    def getNextQValue(self, state, nextState):
        if nextState.row < 0 or nextState.row >= ConfigTable.rows:
            return

        if nextState.column < 0 or nextState.column >= ConfigTable.columns:
            return 

        old = ConfigTable.getIndexForDirtyCellState(state)
        new = ConfigTable.getCellIndex(nextState)
        Q = self.Q_Table[old, new]
        if Q > self.bestQ:
            self.bestQ = Q
            self.bestState = copy.copy(nextState)
