import pygame

COLOR_RED = pygame.Color("Red")
COLOR_WHITE = pygame.Color("White")

class TrainWidget(object):
    def __init__(self, screen):
        super().__init__()
        self._font = pygame.font.SysFont("Monospace", 32)
        self._screen = screen

    def show(self):
        text = f"DISASTER!"
        self._write_text(text, -1, COLOR_RED)
        text = f"Training controller..."
        self._write_text(text, 1, COLOR_WHITE)

    def _write_text(self, text, line = 0, color = COLOR_WHITE):
        text = self._font.render(text, False, color)
        text_rect = text.get_rect()
        text_rect.y = self._screen.get_rect().center[1] + (text_rect.height * line + 5)
        text_rect.x = self._screen.get_rect().center[0] - text_rect.width / 2
        self._screen.blit(text, text_rect)
