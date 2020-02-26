from action import Action
from action import ActionDirection
from rewardsTable import RewardsTable
from configRewards import ConfigRewards
from configTable import ConfigTable
from state import State
from qTable import QTable

class Floor:
    def __init__(self):
        self.state = State()    # Always start in the top left corner cell, row = 0, column = 0
        self.newState = self.state
        self.reward = RewardsTable()
        self.qTable = QTable()
        self.terminateFlag = False
        self.superTerminateFlag = False
        self.noOfSteps = 0
        self.noOfDirtyCellsCleaned = 0
        start_cell_idx = 1
        self.firstReward = self.reward.getReward(start_cell_idx)
        print(f"First Reward for cell 1 is {self.firstReward}")

    def explore(self):
        self.OffEdgeFlag = True   
        oldrow = self.state.row
        oldcolumn = self.state.column  
        # This flag is set so that if an action is chosen
        # that goes off the edge of the grid, then choose another one
        while self.OffEdgeFlag == True:
            reward = 0
            direction = Action.randomDir()
            if direction is direction.north:
                reward = self.moveNorth()
                continue

            if direction is direction.east:
                reward = self.moveEast()
                continue

            if direction is direction.west:
                reward = self.moveWest()
                continue

            if direction is direction.south:
                reward = self.moveSouth()
                continue

        oldState = State()
        oldState.row = oldrow
        oldState.column = oldcolumn
        self.qTable.update(self.newState, oldState, reward)
        self.noOfSteps += 1
        if reward == ConfigRewards.cell_dirty:
            self.noOfDirtyCellsCleaned += 1
        if self.noOfDirtyCellsCleaned == self.reward.noDirtyCells:
            self.terminateFlag = True
            print(f"Episode terminated after {self.noOfSteps} steps")
        if self.noOfSteps == 1000:
            self.terminateFlag = True
            self.superTerminateFlag = True
            print("Episode terminated unsucessfully")

    def moveNorth(self):
        row = self.state.row - 1
        if row < 0:
            # agent not moving off the edge of the floor
            return 0

        self.newState.column = self.state.column
        self.newState.row = row
        self.OffEdgeFlag = False
        idx = self.reward.table[row, self.state.column]
        r = self.reward.getReward(idx)
        if r == ConfigRewards.cell_inaccessible:
            # agent not moving as the cell is inaccessible
            return r
        
        # agent has moved to the new cell, update the row
        self.state.row = row
        return r

    def moveWest(self):
        col = self.state.column + 1
        if col >= ConfigTable.columns:
            # agent not moving off the edge of the floor
            return 0

        self.newState.row = self.state.row
        self.newState.column = col
        self.OffEdgeFlag = False
        idx = self.reward.table[self.state.row, col]
        r = self.reward.getReward(idx)
        if r == ConfigRewards.cell_inaccessible:
            # agent not moving as the cell is inaccessible
            return r
        
        # agent has moved to the new cell, update the column
        self.state.column = col
        return r

    def moveEast(self):
        col = self.state.column - 1
        if col < 0:
            # agent not moving off the edge of the floor
            return 0

        self.newState.row = self.state.row
        self.newState.column = col
        self.OffEdgeFlag = False
        idx = self.reward.table[self.state.row, col]
        r = self.reward.getReward(idx)
        if r == ConfigRewards.cell_inaccessible:
            # agent not moving as the cell is inaccessible
            return r
        
        # agent has moved to the new cell, update the column
        self.state.column = col
        return r

    def moveSouth(self):
        row = self.state.row + 1
        if row >= ConfigTable.rows:
            # agent not moving off the edge of the floor
            return 0

        self.newState.column = self.state.column
        self.newState.row = row
        self.OffEdgeFlag = False
        idx = self.reward.table[row, self.state.column]
        r = self.reward.getReward(idx)
        if r == ConfigRewards.cell_inaccessible:
            # agent not moving as the cell is inaccessible
            return r
        
        # agent has moved to the new cell, update the row
        self.state.row = row
        return r       
            
