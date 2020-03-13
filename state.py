from enum import Enum
class State:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def printState(self):
        print(f"({self.row}, {self.column})")

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