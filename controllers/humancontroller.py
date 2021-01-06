import pygame
from controllers.racecontroller import Action, RaceController

class HumanController(RaceController):
    def __init__(self):
        super().__init__()

    def act(self, state):
        act = Action.Nothing

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            act |= Action.ShiftLeft
        if keystate[pygame.K_RIGHT]:
            act |= Action.ShiftRight
        if keystate[pygame.K_UP]:
            act |= Action.Accelerate
        if keystate[pygame.K_DOWN]:
            act |= Action.Slowdown

        return act;

    def loopback(self, state, action, reward, new_state):
        pass
