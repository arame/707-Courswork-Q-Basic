from test import RewardsTab
from test import RewardsTableRows
from state import State
from configTable import ConfigTable
import numpy as np

# r = RewardsTab()
# arr = np.empty((0, 16))
# for row in r.rtable:
#     arr = np.append(arr, [row.cellReward], axis = 0)

# print(arr)
#print(r.rtable[3])
#print(r.rtable.values)

s1 = State(1, 0)
dirtyCellIndex = 2
ConfigTable.createTableIds()
state1 = ConfigTable.getRewardTableIndex(s1)
print(f"tablecell = ({state1.row}, {state1.column})")

# s2 = State(1, 1)
# dirtyCellIndex = 2
# ConfigTable.createTableIds()
# state2 = ConfigTable.getTableIndex(s2)
# print(f"tablecell = ({state2.row}, {state2.column})")

s3 = State(1, 2)
dirtyCellIndex = 2
ConfigTable.createTableIds()
state3 = ConfigTable.getRewardTableIndex(s3)
print(f"tablecell = ({state3.row}, {state3.column})")

s4 = State(2, 2)
dirtyCellIndex = 2
ConfigTable.createTableIds()
state4 = ConfigTable.getRewardTableIndex(s4)
print(f"tablecell = ({state4.row}, {state4.column})")