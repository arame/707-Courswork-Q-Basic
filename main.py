import numpy as np
from floor import Floor
from configRewards import ConfigRewards
from configTable import ConfigTable
from hyperparameters import Hyperparam
from rewardsTable import RewardsTable
from qTable import QTable
from state import State


print("\n"*10)
print("-"*100)
print("Start of QLearning Basic design for AI vacuum cleaner")
Hyperparam.display()
print("-"*100)
episodes = 0
f = Floor()
f.episodes()
print("-"*100)
print("End of QLearning Basic design for AI vacuum cleaner")
Hyperparam.display()
print("-"*100)