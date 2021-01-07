from enum import Enum
import pygame

from controllers.racecontroller import Action

class Position(Enum):
    Left = 1
    Right = 2
    Center = 3

COLOR_WHITE = pygame.Color("White")
COLOR_RED = pygame.Color("Red")

class StatusWidget(object):
    def __init__(self, screen, rect):
        super().__init__()
        self._pos = rect
        self._font = pygame.font.SysFont("Monospace", 16)
        self._rect = rect
        self._screen = screen

        self._speed = [ 0, 0 ]
        self._car_rect = pygame.Rect(0, 0, 0, 0)
        self._border_bounce = False
        self._barrier_bounce = False
        self._action = Action.Nothing
        self._reward = 0

    def update(self):
        text = f"Speed x/y: {self._speed[0]}/{self._speed[1]}"
        self._write_text(text, 0, Position.Left)
        text = f"Car position: {self._car_rect.center[0]}/{self._car_rect.center[1]}"
        self._write_text(text, 1)
        text = f"Action: {self._action.name}/Reward: {self._reward}"
        self._write_text(text, 2)
        if self._border_bounce:
            text = "Border!"
            self._write_text(text, 3, Position.Center, COLOR_RED)
        if self._barrier_bounce:
            text = "DISASTER!"
            self._write_text(text, 4, Position.Center, COLOR_RED)
        self._barrier_bounce = self._border_bounce = False

    def _write_text(self, text, line = 0, align = Position.Left, color = COLOR_WHITE):
        text = self._font.render(text, False, color)
        text_rect = self._text_rect(text, align, line)
        self._screen.blit(text, text_rect)

    def on_speed_update(self, speed):
        self._speed = speed[:]

    def on_car_update(self, rect):
        self._car_rect = rect

    def on_bounce_border(self):
        self._border_bounce = True

    def on_bounce_barrier(self):
        self._barrier_bounce = True

    def on_action_update(self, action, reward):
        self._action = action
        self._reward = reward

    def _text_rect(self, text, align, line):
        text_rect = None
        if align == Position.Center:
            text_rect = text.get_rect(center=(self._pos.center[0], self._pos.y + text.get_rect().height * line + 5))
        elif align == Position.Right:
            text_rect = text.get_rect()
            text_rect.x = self._pos.x + self._pos.width - text.get_rect().width
            text_rect.y = self._pos.y + text.get_rect().height * line + 5
        elif  align == Position.Left:
            text_rect = text.get_rect()
            text_rect.x = self._pos.x
            text_rect.y = self._pos.y + text.get_rect().height * line + 5
        return text_rect
