import copy
from action import Action
from action import ActionDirection
from rewardsTable import RewardsTable
from configRewards import ConfigRewards
from configTable import ConfigTable
from state import State
from qTable import QTable
from policy import Policy
from policy import PolicyType
from hyperparameters import Hyperparam

class Floor:
    def __init__(self):
        self.reward = RewardsTable()
        self.qTable = QTable()

    def init_episode(self):
        self.state = State()    # Always start in the top left corner cell, row = 0, column = 0
        self.newState = self.state
        self.terminateFlag = False
        self.superTerminateFlag = False
        self.noOfSteps = 0
        self.noOfDirtyCellsCleaned = 0
        self.reward.resetRewardValues() # For a new episode the reward table needs to be reset to the original

    def episodes(self):
        for episode in range(Hyperparam.noOfEpisodes):
            self.episode(episode)

    def episode(self, episode):
        print("-"*100)
        print(f"Start episode {episode + 1}")
        self.init_episode()
        start_cell_idx = 1
        firstReward = self.reward.getReward(start_cell_idx)
        state = State()
        self.qTable.update(state, state, firstReward)    # Special case update for the first cell
        print(f"First Reward for cell 1 is {firstReward}")
        while self.terminateFlag == False:
            self.selectPolicy()
            self.checkIfTooManySteps()

        print(f"end episode {episode + 1}")

    def selectPolicy(self):
        policy = Policy()
        policy.next()
        if policy.type is PolicyType.explore:
            self.explore() 
            return

        if policy.type is PolicyType.exploit:
            self.explore()
            #self.exploit()

    def checkIfTooManySteps(self):
        if self.noOfSteps == 1000:
            self.terminateFlag = True
            self.superTerminateFlag = True
            print("Episode terminated unsucessfully")

    def explore(self):
        if self.noOfSteps % 500 == 0:
            print(f"explore on step {self.noOfSteps + 1}")

        oldState = copy.copy(self.state)
        reward = self.actionAndReward()
        self.qTable.update(self.newState, oldState, reward)
        self.noOfSteps += 1
        idx = self.reward.table[self.state.row, self.state.column]
        self.checkIfDirtyCell(idx, reward)

    def actionAndReward(self):
        self.OffEdgeFlag = True
        # This flag is set so that if an action is chosen
        # that goes off the edge of the grid, then choose another one
        while self.OffEdgeFlag == True:
            direction = Action.randomDir()
            if direction is direction.north:
                reward = self.moveNorth()
                continue

            if direction is direction.east:
                reward =  self.moveEast()
                continue

            if direction is direction.west:
                reward =  self.moveWest()
                continue

            if direction is direction.south:
                reward =  self.moveSouth()
                continue

        return reward

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
        self.checkIfDirtyCell(idx, r)
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
            
    def checkIfDirtyCell(self, idx, reward):
        # If the cell was dirty, it should now be clean
        if reward == ConfigRewards.cell_dirty:
            self.noOfDirtyCellsCleaned += 1
            print(f"Dirty Cell {idx} cleaned no {self.noOfDirtyCellsCleaned}")
            self.reward.setRewardToClean(idx)
        # The termination condition is met if all the cells are cleaned
        if self.noOfDirtyCellsCleaned == self.reward.noDirtyCells:
            self.terminateFlag = True
            print(f"Episode terminated after {self.noOfSteps} steps")
    
    def exploit(self):
        #if self.noOfSteps % 500 == 0:
        #print(f"exploit on step {self.noOfSteps}")
        newState = self.qTable.getBestQvalue(self.state)
        self.state = newState
        idx = self.reward.table[self.state.row, self.state.column]
        reward = self.reward.rewardValues[str(idx)]
        self.checkIfDirtyCell(idx, reward)
