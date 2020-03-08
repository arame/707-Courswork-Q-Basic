from enum import Enum
class State:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def printState(self):
        print(f"({self.row}, {self.column})")

    @staticmethod
    def getInitialState():
        return {1: StateType.start, 2: StateType.clean, 3: StateType.clean, 4: StateType.clean,
                            5: StateType.clean, 6: StateType.inaccessible, 7: StateType.dirty, 8:StateType.inaccessible,
                            9: StateType.clean, 10: StateType.dirty, 11: StateType.clean, 12: StateType.clean,
                            13: StateType.inaccessible, 14: StateType.dirty, 15: StateType.clean, 16: StateType.clean } 

        
        

    # This method allows comparison between objects
    def __eq__(self, other):
        if not isinstance(other, State):
            # do not compare unrelated type
            return NotImplemented
        return self.row == other.row and self.column == other.column

class StateType(Enum):
    start = 1
    finish = 2
    clean = 3
    dirty = 4
    inaccessible = 5