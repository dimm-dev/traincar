import numpy as np

from sprites.car import Car
from utils.limits import normalize_range_limits, normalize_glide_limits

SPEED_LIMITS = (0, 25)
GLIDE_LIMITS = (0, 10)

class CarController(object):
    def __init__(self, start_pos, car, speed_update):
        super().__init__()
        self._car = car
        self._speed = [0, 0]
        self._speed_update = speed_update
        car.moveto(start_pos)

    def tick(self, accel):
        speed = np.add(self._speed, accel)
        speed = [normalize_glide_limits(speed[0], GLIDE_LIMITS), normalize_range_limits(speed[1], SPEED_LIMITS)]
        self._speed[1] = speed[1]
        self._car.move(speed)
        self._speed_update(speed)
