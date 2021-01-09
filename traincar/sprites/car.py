import pygame

from utils.limits import normalize_range_limits

CAR_WIDTH = 50
CAR_HEIGHT = 100

class Car(pygame.sprite.Sprite):
    def __init__(self, track_limits):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("assets/car.png").convert_alpha()
        self.image = pygame.transform.scale(image, (CAR_WIDTH, CAR_HEIGHT)).convert_alpha()
        self.rect = self.image.get_rect()
        self._track_limits = track_limits

        self.track_bounce_delegate = []

    def move(self, speed):
        # TODO: interaction with the track object?
        expected = self.rect.x + speed[0]
        self.rect.x = normalize_range_limits(self.rect.x + speed[0], self._track_limits)
        if self.rect.x != expected:
            self._notify_border_bounce()

    def moveto(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def _notify_border_bounce(self):
        for endpoint in self.track_bounce_delegate:
            endpoint()

    def update(self):
        pass
