class EnvironemtController(object):
    def __init__(self, barriers, car):
        super().__init__()
        self._barriers = barriers
        self._car = car

        self.restart()

    def snapshot(self):
        state = []
        state += self._speed
        state += [self._car.rect.x, self._car.rect.y, self._car.rect.x + self._car.rect.width, self._car.rect.y + self._car.rect.height]
        for b in self._barriers:
            state += [b.rect.x, b.rect.y]

        return state

    def reward(self):
        value = 0
        value += 3 if self._speed[1] > 0 else -1
        value += 7 if self._speed[1] > self._prev_speed[1] else 0
        value += 5 if self._speed[0] != self._prev_speed[0] else 0
        value += -2 if self._bounce_border else 0
        value += -17 if self._bounce_barrier else 0
        return value

    def on_speed_update(self, speed):
        self._speed = speed[:]

    def on_bounce_border(self):
        self._bounce_border = True

    def on_bounce_barrier(self):
        self._bounce_barrier = True

    def update(self):
        self._prev_speed = self._speed[:]
        self._bounce_barrier = False
        self._bounce_border = False

    def restart(self):
        self._speed = [0, 0]
        self._prev_speed = [0, 0]
        self._bounce_border = False
        self._bounce_barrier = False
