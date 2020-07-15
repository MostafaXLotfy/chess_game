import pygame
screen = pygame.display.set_mode((800, 800))
class Renderer:
    # this class will draw the pieces, positions, and available moves of piece on the screen
    def __init__(self, choice, dictionary=None, surface=None, coordinates=None):
        self.__screen = screen
        if choice == 1:
            # initializing a dictionary that holds positions on the board
            # these positions are mapped to the parameters to draw a position on the board
            self.__dictionary = True
            self.__single = False
            if self.__dictionary is None or surface is not None or coordinates is not None:
                raise ValueError("you should only pass a reference of the positions dictionary")
            self.__positions_to_surfaces = dictionary
        elif choice == 0:
            # this will initialize a variable that will hold a surface to be drawn on the screen and  its coordinates
            self.__dictionary = False
            self.__single = True
            if dictionary is not None or surface is None or coordinates is None:
                raise ValueError("you should only pass a reference of the surface and the coordinates")
            self.__surface = surface
            self.__coordinates = coordinates

    # this function is used to render things on the screen
    def render(self):
        if self.__dictionary:
            self.__render_dictionary()
        else:
            self.__render_single()

    # this function will draw boards on the sceen
    def __render_dictionary(self):
        for position in self.__positions_to_surfaces:
            screen.blit(self.__positions_to_surfaces[position])

    # this function will draw images on the screen
    def __render_single(self):
        screen.blit(self.__surface, self.__coordinates)
