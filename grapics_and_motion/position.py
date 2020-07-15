from math import ceil

import pygame

from grapics_and_motion.render import Renderer
from grapics_and_motion.render import screen


def coordinates_to_position(x, y):
    return int(ceil(x / 100)), int(ceil(y / 100))


def position_to_coordinates(x, y):
    return (x - 1) * 100, (y - 1) * 100


class Position:
    # a class that represents positions on the board
    def __init__(self, x, y, image=None):
        self.__x = x
        self.__y = y
        if image is not None:
            self.__image = pygame.image.load(image)
            self.__rect = self.__image.get_rect()
            self.__renderer = Renderer(0, surface=self.__image, coordinates=self.position_to_coordinates())

    def render(self):
        self.__renderer.render()

    # addition of two positions
    def __add__(self, other):
        return Position(self.__x + other.__x, self.__y + other.__y, None)

    # subtraction of two positions
    def __sub__(self, other):
        return Position(self.__x - other.__x, self.__y - other.__y, None)

    # calculating the coordinates of position on the screen
    def position_to_coordinates(self):
        return (self.__x - 1) * 100, (self.__y - 1) * 100

    def set_as_move(self):
        screen.blit(pygame.image.load("images/move.png"), self.position_to_coordinates())
        pygame.display.update()

    def set_as_enemy(self):
        screen.blit(pygame.image.load("images/enemy.png"), self.position_to_coordinates())
        pygame.display.update()

    @property
    def rect(self):
        return self.__rect

    @property
    def tuple(self):
        return self.__x, self.__y

