from test import RewardsTab
from test import RewardsTableRows
import numpy as np

r = RewardsTab()
arr = np.empty((0, 16))
for row in r.rtable:
    arr = np.append(arr, [row.cellReward], axis = 0)

print(arr)
#print(r.rtable[3])
#print(r.rtable.values)