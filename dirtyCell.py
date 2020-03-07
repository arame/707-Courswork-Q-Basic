
class DirtyCell:
    def __init__(self, cellId):
        self.cellId = cellId
        self.isDirty = True

    def clean(self):
        self.isDirty = False
