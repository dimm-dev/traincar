import pygame

from traincar.utils.assets import build_asset_path

BARRIER_SIZE = (20, 30)

class Barrier(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(build_asset_path("barrier.png")).convert_alpha()
        self.image = pygame.transform.scale(image, BARRIER_SIZE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move(self, speed):
        self.rect.x += speed[0]
        self.rect.y += speed[1]

    def update(self):
        pass
