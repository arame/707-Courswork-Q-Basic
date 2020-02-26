from hyperparameters import Hyperparam
import numpy as np
from enum import Enum

class PolicyType(Enum):
    explore = 1
    exploit = 2

class Policy:
    def __init__(self):
        self.epsilon = Hyperparam.epsilon
        self.type = PolicyType(1)

    def next(self):
        if np.random.uniform() > self.epsilon:
            self.type = PolicyType.explore
        else:
            self.type = PolicyType.explore
        
        if self.epsilon > Hyperparam.epsilon_threshold:
            return

        #self.epsilon = self.epsilon * Hyperparam.epsilon_increase


