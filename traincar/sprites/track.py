import pygame

TRACK_IMAGE_WIDTH = 600
TRACK_IMAGE_HEIGHT = 800
TRACK_ROAD_LEFT = 100
TRACK_ROAD_RIGHT = 450

class Track(object):
    def __init__(self, screen):
        self._screen = screen
        self._track = pygame.image.load('assets/track.jpg')

    def update(self):
        self._screen.blit(self._track, (0, 0))
