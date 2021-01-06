import pygame
import random

from sprites.car import Car
from sprites.track import Track, TRACK_IMAGE_WIDTH, TRACK_IMAGE_HEIGHT, TRACK_ROAD_LEFT, TRACK_ROAD_RIGHT

from controllers.barriercontroller import BarrierController
from controllers.carcontroller import CarController
from controllers.racecontroller import Action
from controllers.humancontroller import HumanController

FPS = 30

def translate_action(action):
    accel_x = 0
    accel_y = 0
    if action & Action.Accelerate:
        accel_y += 1
    if action & Action.Slowdown:
        accel_y -= 1
    if action & Action.ShiftLeft:
        accel_x -= 3
    if action & Action.ShiftRight:
        accel_x += 3

    return accel_x, accel_y

def game_run():
    pygame.init()

    screen = pygame.display.set_mode((TRACK_IMAGE_WIDTH, TRACK_IMAGE_HEIGHT))
    track = Track(screen)

    pygame.display.set_caption("Trained car")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    car = Car((TRACK_ROAD_LEFT, TRACK_ROAD_RIGHT))
    all_sprites.add(car)

    car_controller = CarController((TRACK_IMAGE_WIDTH / 2, TRACK_IMAGE_HEIGHT - car.rect.height), car)
    # TODO: all_sprites access via adapter object
    barrier_controller = BarrierController((TRACK_ROAD_LEFT, TRACK_ROAD_RIGHT, TRACK_IMAGE_HEIGHT), all_sprites)

    game_controller = HumanController()

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        action = game_controller.act(None)
        accel_x, accel_y = translate_action(action)
        speed_x, speed_y = car_controller.update([accel_x, accel_y])
        barrier_controller.update([speed_x, speed_y])

        hits = pygame.sprite.spritecollide(car, barrier_controller.barriers, False)
        if hits:
            running = False

        all_sprites.update()

        track.update()

        all_sprites.draw(screen)
    
        pygame.display.flip()

    pygame.quit()
