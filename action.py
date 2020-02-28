from enum import Enum
from random import seed
from random import randint

class ActionDirection(Enum):
    north = 1
    west = 2
    east = 3
    south = 4

class Action:
    @staticmethod
    def randomDir():
        rdn = randint(1, 4)
        return ActionDirection(rdn)

