class State: 
    def __init__(self):
        self.row = 0
        self.dirtyCellIndex = 0
        self.column = 0

    def __eq__(self, other):
        if not isinstance(other, State):
            # do not compare unrelated type
            return NotImplemented
        return self.row == other.row and self.dirtyCellIndex == other.dirtyCellIndex and self.column == other.column
