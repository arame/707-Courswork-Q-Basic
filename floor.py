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
        self.qTable = QTable(self.reward.rtable)
        self.policy = Policy()
        ConfigTable.createTableIds()
        self.log = []

    def init_episode(self):
        self.reward = RewardsTable()
        self.state = State(0, 0)    # Always start in the top left corner cell, row = 0, column = 0. 
                                # DirtyCellState is also zero
        self.newState = self.state
        self.terminateFlag = False
        self.superTerminateFlag = False
        self.noOfSteps = 0
        self.noOfDirtyCellsCleaned = 0
        self.dirtyCellsFound = []
        self.noExplore = 0
        self.noExploit = 0
        ConfigTable.dirtyCellIndex = 0

    def episodes(self):
        for episode in range(Hyperparam.noOfEpisodes):
            self.episode(episode)
            if self.policy.epsilon > Hyperparam.epsilon_threshold:
                print(f"Epsilon limit {Hyperparam.epsilon_threshold} exceeded")
                break
        print("".join(self.log))
        print("Final Q values")
        for row in self.qTable.Q_Table:
            print(row)

    def episode(self, episode):
        self.episode1 = episode + 1
        print("-"*100)
        print(f"Start episode {episode + 1}")
        self.init_episode()
        # firstReward = ConfigRewards.cell_clean
        # self.qTable.update(State(0, 0), State(0, 0), firstReward)    # Special case update for the first cell
        # print(f"First Reward for cell 1 is {firstReward}")
        while self.terminateFlag == False:
            self.selectPolicy()
            self.checkIfTooManySteps()

        print(f"Explorations = {self.noExplore}")
        print(f"Exploitations = {self.noExploit}")
        print(f"Epsilon rate = {self.policy.epsilon}")
        print(f"end episode {episode + 1}")
        

    def selectPolicy(self):
        self.policy.next()
        if self.policy.type is PolicyType.explore:
            self.explore() 
            return

        if self.policy.type is PolicyType.exploit:
            self.exploit()

    def checkIfTooManySteps(self):
        self.noOfSteps += 1
        if self.noOfSteps == 1000:
            self.terminateFlag = True
            self.superTerminateFlag = True
            print("Episode terminated unsucessfully")

    def explore(self):
        self.noExplore += 1
        oldState = copy.copy(self.state)
        reward = self.actionAndReward()
        self.qTable.update(self.newState, oldState, reward)
        if reward == ConfigRewards.cell_dirty:
            ConfigTable.dirtyCellIndexIncrement(self.newState)
        self.checkIfFinishCell(reward)

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
        #print(f"north ({self.state.row}, {self.state.column})")
        row = self.state.row - 1
        if row < 0:
            # agent not moving off the edge of the floor
            return 0

        self.newState = copy.copy(self.state)
        self.newState.row = row

        self.OffEdgeFlag = False
        isInaccessible = self.reward.isInaccessible(self.newState)
        if isInaccessible == True:
            # agent not moving as the cell is inaccessible
            return ConfigRewards.cell_inaccessible
        
        r = self.reward.getReward(self.state, self.newState)
        # agent has moved to the new cell, update the row
        self.state.row = row
        return r

    def moveWest(self):
        #print(f"West ({self.state.row}, {self.state.column})")
        col = self.state.column - 1
        if col < 0:
            # agent not moving off the edge of the floor
            return 0

        self.newState = copy.copy(self.state)
        self.newState.column = col
        self.OffEdgeFlag = False
        isInaccessible = self.reward.isInaccessible(self.newState)
        if isInaccessible == True:
            # agent not moving as the cell is inaccessible
            return ConfigRewards.cell_inaccessible
        
        r = self.reward.getReward(self.state, self.newState)
        # agent has moved to the new cell, update the column
        self.state.column = col
        return r

    def moveEast(self):
        #print(f"East ({self.state.row}, {self.state.column})")
        col = self.state.column + 1
        if col >= ConfigTable.columns:
            # agent not moving off the edge of the floor
            return 0

        self.newState = copy.copy(self.state)
        self.newState.column = col
        self.OffEdgeFlag = False
        isInaccessible = self.reward.isInaccessible(self.newState)
        if isInaccessible == True:
            # agent not moving as the cell is inaccessible
            return ConfigRewards.cell_inaccessible
        
        r = self.reward.getReward(self.state, self.newState)
        # agent has moved to the new cell, update the column
        self.state.column = col
        return r

    def moveSouth(self):
        #print(f"South ({self.state.row}, {self.state.column})")
        row = self.state.row + 1
        if row >= ConfigTable.rows:
            # agent not moving off the edge of the floor
            return 0

        self.newState = copy.copy(self.state)
        self.newState.row = row
        self.OffEdgeFlag = False
        isInaccessible = self.reward.isInaccessible(self.newState)
        if isInaccessible == True:
            # agent not moving as the cell is inaccessible
            return ConfigRewards.cell_inaccessible
        
        r = self.reward.getReward(self.state, self.newState)
        # agent has moved to the new cell, update the row
        self.state.row = row
        return r   
     
    def checkIfFinishCell(self, reward):
        # check if the last cell has been reached
        if reward == ConfigRewards.cell_finish:
            # The termination condition is met if all the cells are cleaned and the 
            # agent has returned to the cell it started in
            self.terminateFlag = True
            print("**")
            print(f"**Episode terminated after {self.noOfSteps} steps")
            print("**")
            self.log.append(f"Episode {self.episode1} completed after {self.noOfSteps} | ")

    def exploit(self):
        
        oldState = copy.copy(self.state)
        newState = self.qTable.getBestQvalue(self.state)
        if oldState == newState:
            # No Q value found to go to a new location, so explore to a new one instead
            self.explore()
            return
  
        self.noExploit += 1
        #print("Q value found, move to next cell")                 
        #self.state = copy.copy(newState)
        #idx = self.reward.getListIndex(self.state)
        reward = self.reward.getReward(self.state, newState)
        self.checkIfFinishCell(reward)
        self.state = copy.copy(newState)
