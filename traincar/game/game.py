import pygame
from traincar.game.appcontext import AppContext

FPS = 30

def app_run():
    pygame.init()

    pygame.display.set_caption("Trained car")
    clock = pygame.time.Clock()
    context = AppContext()

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            running = running and event.type != pygame.QUIT

        if running and not context.update():
            context.restart()
    
        pygame.display.flip()

    pygame.quit()
