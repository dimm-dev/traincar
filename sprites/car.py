import pygame

from utils.limits import normalize_range_limits

class Car(pygame.sprite.Sprite):
    def __init__(self, track_limits):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("assets/car.png").convert_alpha()
        self.image = pygame.transform.scale(image, (60, 120)).convert_alpha()
        self.rect = self.image.get_rect()
        self._track_limits = track_limits

    def move(self, speed):
        self.rect.x = normalize_range_limits(self.rect.x + speed[0], self._track_limits)

    def moveto(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        pass
