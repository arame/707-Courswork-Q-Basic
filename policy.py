from hyperparameters import Hyperparam
import numpy as np
from enum import Enum

class PolicyType(Enum):
    explore = 1
    exploit = 2

class Policy:
    def __init__(self):
        explore = 1
        self.epsilon = Hyperparam.epsilon
        self.type = PolicyType(explore)     # By default the policy type is explore

    def next(self):
        if np.random.uniform() > self.epsilon:
            self.type = PolicyType.explore
        else:
            self.type = PolicyType.exploit
        
        if self.epsilon > Hyperparam.epsilon_threshold:
            return

        self.epsilon = self.epsilon * Hyperparam.epsilon_increase


