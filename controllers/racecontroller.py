import numpy as np
from enum import IntFlag

class Action(IntFlag):
    Nothing = 0,
    Slowdown = 1,
    Accelerate = 2,
    ShiftLeft = 3,
    ShiftRight = 4

class RaceController(object):
    def __init__(self):
        super().__init__()

    def act(self, state):
        pass

    def loopback(self, reward, new_state):
        pass
