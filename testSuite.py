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
print("Start of QLearning Basic Test Suite")
Hyperparam.display()
print("-"*100)

ConfigTable.createTableIds()
s = State(0, 0)
s1 = State(0, 0)
s2 = State(0, 1)
s3 = State(0, 2)
s4 = State(0, 3)
s5 = State(1, 0)
s6 = State(1, 1)
s7 = State(1, 2)
s8 = State(1, 3)
s9 = State(2, 0)
s10 = State(2, 1)
s11 = State(2, 2)
s12 = State(2, 3)
s13 = State(3, 0)
s14 = State(3, 1)
s15 = State(3, 2)
s16 = State(3, 3)
r = RewardsTable()
listLength = r.rewardValues.__len__()
q = QTable(listLength)

print(f"State = ({s1.row}, {s1.column})")
reward = r.getReward(s1)
print(f"Reward for state ({s1.row}, {s1.column}) is {reward}, index = {r.index} cell index = {r.cellIdx}")
q.update(s1, s, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"State = ({s2.row}, {s2.column})")
reward = r.getReward(s2)
print(f"Reward for state ({s2.row}, {s2.column}) is {reward} index = {r.index} cell index = {r.cellIdx}")
q.update(s2, s1, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"D1 Dirty State = ({s7.row}, {s7.column})")
reward = r.getReward(s7)
print(f"Reward for state ({s7.row}, {s7.column}) is {reward} index = {r.index} cell index = {r.cellIdx}")
q.update(s7, s1, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"D2 Dirty State = ({s10.row}, {s10.column})")
reward = r.getReward(s10)
print(f"Reward for state ({s10.row}, {s10.column}) is {reward} index = {r.index} cell index = {r.cellIdx}")
q.update(s10, s7, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"D3 Dirty State = ({s14.row}, {s14.column})")
reward = r.getReward(s14)
print(f"Reward for state ({s14.row}, {s14.column}) is {reward} index = {r.index} cell index = {r.cellIdx}")
q.update(s14, s10, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"D1 Dirty State = ({s7.row}, {s7.column})")
reward = r.getReward(s7)
print(f"Reward for state ({s7.row}, {s7.column}) is {reward} index = {r.index} cell index = {r.cellIdx}")
q.update(s7, s14, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"D2 Dirty State = ({s10.row}, {s10.column})")
reward = r.getReward(s10)
print(f"Reward for state ({s10.row}, {s10.column}) is {reward} index = {r.index} cell index = {r.cellIdx}")
q.update(s10, s7, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"D3 Dirty State = ({s14.row}, {s14.column})")
reward = r.getReward(s14)
print(f"Reward for state ({s14.row}, {s14.column}) is {reward} index = {r.index} cell index = {r.cellIdx}")
q.update(s14, s10, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"State = ({s2.row}, {s2.column})")
reward = r.getReward(s2)
print(f"Reward for state ({s2.row}, {s2.column}) is {reward}, index = {r.index} cell index = {r.cellIdx}")
q.update(s2, s14, reward)
print(f"Q = {q.Q_Values}")

print("*"*100)
print(f"State = ({s1.row}, {s1.column})")
reward = r.getReward(s1)
print(f"Reward for state ({s1.row}, {s1.column}) is {reward}, index = {r.index} cell index = {r.cellIdx}")
q.update(s1, s2, reward)
print(f"Q = {q.Q_Values}")


print("-"*100)
print("End of QLearning Basic Test Suite")
print("-"*100)