from abc import ABC

import pygame

from grapics_and_motion.render import Renderer

""" This class is a bas class to all pieces in the chess game"""


class Piece(ABC):
    def __init__(self, position, color, image):
        #  instance of class Position that holds where the piece is
        self.__position = position
        self.__color = color
        # drawing picture after it was loaded
        self.__surface = pygame.image.load(image)
        self.__renderer = Renderer(0, surface=self.__surface, coordinates=self.__position.position_to_coordinates())

    # this function will return positions of possible moves and enemies to kill
    def calculate_moves(self, white: dict, black: dict):
        pass

    def change_pos(self, position):
        self.__position = position
        self.__renderer = Renderer(0, surface=self.__surface, coordinates=self.__position.position_to_coordinates())

    @property
    def position(self):
        return self.__position

    @property
    def color(self):
        return self.__color

    def render(self):
        self.__renderer.render()