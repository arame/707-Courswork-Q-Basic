import numpy as np
from floor import Floor
from configRewards import ConfigRewards
from configTable import ConfigTable
from hyperparameters import Hyperparam
from rewardsTable import RewardsTable
from qTable import QTable
from state import State
from policy import Policy

print("\n"*10)
print("-"*100)
print("Start of QLearning Basic design for AI vacuum cleaner")
Hyperparam.display()
print("-"*100)
episodes = 0
while episodes < 50:
    episodes += 1
    f = Floor()
    while f.terminateFlag == False:
        policy = Policy()
        policy.next()
        if policy.type.explore:
            f.explore()
    print(f"Episode {episodes} completed")
    print(f"After {f.noOfSteps} step completed")


print("-"*100)
print("End of QLearning Basic design for AI vacuum cleaner")
Hyperparam.display()
print("-"*100)