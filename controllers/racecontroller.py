import numpy as np
from enum import IntFlag

class Action(IntFlag):
    Nothing = 0,
    Slowdown = 2,
    Accelerate = 4,
    ShiftLeft = 8,
    ShiftRight = 16

class RaceController(object):
    def __init__(self):
        super().__init__()

    def act(self, state):
        pass

    def remember(self, state, action, reward, new_state):
        pass
