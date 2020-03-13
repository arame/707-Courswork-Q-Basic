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
        _state = ConfigTable.getIndexForDirtyCellState(oldState)
        _action = ConfigTable.getCellIndex(newState)
        q_old = self.Q_Table[_state, _action]
        self.getMaxQAction(newState)
        self.q_max = self.bestQ
        q_new = q_old + alpha * (reward + gamma * self.q_max - q_old)
        self.Q_Table[_state, _action] = q_new

    def getMaxQAction(self, state):
        x = state.row
        y = state.column
        
        self.bestState = copy.copy(state)
        self.bestQ = 0
        self.getNextQValue(state, State(x - 1, y))
        self.getNextQValue(state, State(x + 1, y))
        self.getNextQValue(state, State(x, y - 1))
        self.getNextQValue(state, State(x, y + 1))
    
    def getBestQvalue(self, state):
        self.getMaxQAction(state)
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
