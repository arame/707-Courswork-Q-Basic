class DirtyCellIndex:
     # Dictionary of dirty cells, 
     # key = cell id, 
     # value = how much to increment the dirty cell index once the cell is cleaned
     dirtyCells = {9: 2, 13: 1}
     idx = 0

     @staticmethod
     def increment(type):
          if DirtyCellIndex.idx + DirtyCellIndex.dirtyCells[type] < 4:
               DirtyCellIndex.idx += DirtyCellIndex.dirtyCells[type]
     @staticmethod
     def get(index):
         return DirtyCellIndex.idx + index 