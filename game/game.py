import pygame
import random

from sprites.car import Car

from controllers.barriercontroller import BarrierController
from controllers.carcontroller import CarController

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 800

TRACK_LEFT = 100
TRACK_RIGHT = 450

FPS = 30

def speed_update(ref_speed, speed):
    ref_speed[:] = speed[:]

def game_run():
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    track = pygame.image.load('assets/track.jpg')
    screen.blit(track, (0, 0))

    pygame.display.set_caption("Trained car")
    clock = pygame.time.Clock()
    game_speed = [0, 0]

    all_sprites = pygame.sprite.Group()
    car = Car((TRACK_LEFT, TRACK_RIGHT))
    all_sprites.add(car)

    car_controller = CarController((DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - car.rect.height), car, lambda speed : speed_update(game_speed, speed))
    # TODO: all_sprites access via adapter object
    barrier_controller = BarrierController((TRACK_LEFT, TRACK_RIGHT, DISPLAY_HEIGHT), all_sprites)

    running = True

    while running:
        clock.tick(FPS)
        accel_y = 0
        accel_x = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            accel_x += -2
        if keystate[pygame.K_RIGHT]:
            accel_x += 2
        if keystate[pygame.K_UP]:
            accel_y += 1
        if keystate[pygame.K_DOWN]:
            accel_y -= 1

        car_controller.tick([accel_x, accel_y])
        barrier_controller.tick(game_speed)

        hits = pygame.sprite.spritecollide(car, barrier_controller.barriers, False)
        if hits:
            running = False

        all_sprites.update()

        screen.blit(track, (0, 0))
        all_sprites.draw(screen)
    
        pygame.display.flip()

    pygame.quit()
