import pygame

BARRIER_SIZE = (16, 24)

class Barrier(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("assets/barrier.png").convert_alpha()
        self.image = pygame.transform.scale(image, BARRIER_SIZE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move(self, speed):
        self.rect.x += speed[0]
        self.rect.y += speed[1]

    def update(self):
        pass
