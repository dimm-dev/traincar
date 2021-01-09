import pygame

from game.statuswidget import StatusWidget
from game.trainwidget import TrainWidget

from sprites.car import Car
from sprites.track import Track, TRACK_IMAGE_WIDTH, TRACK_IMAGE_HEIGHT, TRACK_ROAD_LEFT, TRACK_ROAD_RIGHT

from controllers.barriercontroller import BarrierController
from controllers.carcontroller import CarController
from controllers.environmentcontroller import EnvironemtController
from controllers.humancontroller import HumanController
from controllers.dqncontroller import DQNController

from utils.actions import translate_action

class AppContext(object):
    def __init__(self):
        super().__init__()
        self._screen = pygame.display.set_mode((TRACK_IMAGE_WIDTH, TRACK_IMAGE_HEIGHT))
        self._track = Track(self._screen)
        self._all_sprites = pygame.sprite.Group()
        self._car = Car((TRACK_ROAD_LEFT, TRACK_ROAD_RIGHT))
        self._all_sprites.add(self._car)
        self._car_controller = CarController((TRACK_IMAGE_WIDTH / 2, TRACK_IMAGE_HEIGHT - self._car.rect.height), self._car)
        # TODO: all_sprites access via adapter object
        self._barrier_controller = BarrierController((TRACK_ROAD_LEFT, TRACK_ROAD_RIGHT, TRACK_IMAGE_HEIGHT), self._all_sprites)
        self._game_controller = DQNController() # HumanController()
        self._environment = EnvironemtController(self._barrier_controller.barriers, self._car)

        self._widget = StatusWidget(self._screen, pygame.Rect(5, 5, 150, 150))

        self._updates = [self._all_sprites.update, self._track.update, self._widget.update, lambda : self._all_sprites.draw(self._screen), self._environment.update ]

        self._car.track_bounce_delegate.append(self._border_bounce)
        self.speed_update_delegate = [self._barrier_controller.update, self._environment.on_speed_update, self._environment.on_speed_update, self._widget.on_speed_update]
        self.border_bounce_delegate = [self._environment.on_bounce_border, self._widget.on_bounce_border]
        self.barrier_bounce_delegate = [self._environment.on_bounce_barrier, self._widget.on_bounce_barrier]
        self.action_delegate = [self._widget.on_action_update]
        self.car_position_delegate = [self._widget.on_car_update]

        self._update = self._real_update

    def update(self):
        return self._update()

    def restart(self):
        self._update = self._notify_train
        return True

    def _notify_train(self):
        w = TrainWidget(self._screen)
        w.show()
        self._update = self._restart_modules
        return True

    def _restart_modules(self):
        self._update = self._real_update
        for gem in [self._environment, self._car_controller, self._barrier_controller, self._game_controller]:
            gem.restart()
        return True

    def _real_update(self):
        cont = self._make_iteration()
        self._do_updates()

        return cont

    def _dispatch_speed(self, speed):
        for endpoint in self.speed_update_delegate:
            endpoint(speed)

    def _do_updates(self):
        for endpoint in self._updates:
            endpoint()

    def _make_iteration(self):
        action = self._game_controller.act(self._environment)
        accel_x, accel_y = translate_action(action)
        speed_x, speed_y = self._car_controller.update([accel_x, accel_y])

        self._dispatch_speed([speed_x, speed_y])

        hits = pygame.sprite.spritecollide(self._car, self._barrier_controller.barriers, False)
        if hits:
            self._barrier_bounce()

        reward = self._environment.reward()
        self._dispatch_action(action, reward)
        self._dispatch_car_position(self._car.rect)
        self._game_controller.loopback(reward, self._environment)

        return len(hits) == 0

    def _notify_impl(self, delegate):
        for endpoint in delegate:
            endpoint()

    def _border_bounce(self):
        self._notify_impl(self.border_bounce_delegate)

    def _barrier_bounce(self):
        self._notify_impl(self.barrier_bounce_delegate)

    def _dispatch_action(self, act, reward):
        for endpoint in self.action_delegate:
            endpoint(act, reward)

    def _dispatch_car_position(self, rect):
        for endpoint in self.car_position_delegate:
            endpoint(rect)
