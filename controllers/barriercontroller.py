import random
from sprites.barrier import Barrier, BARRIER_SIZE

class BarrierController(object):
    def __init__(self, track_limits, sprites):
        self.barriers = []
        self._track_limits = track_limits
        self._top = 0
        y = track_limits[1] / 2
        for _ in range(0, 40):
            x = random.randint(track_limits[0], track_limits[1])
            b = Barrier([x, y])
            y -= BARRIER_SIZE[1] * 8
            self.barriers.append(b)
            sprites.add(b)
        self._top = y + track_limits[1] / 2

    def update(self, speed):
        for b in self.barriers:
            b.move([0, speed[1]])
            if b.rect.y >= self._track_limits[2] + BARRIER_SIZE[1]:
                b.rect.y = self._top
