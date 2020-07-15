import pygame

from chess_components.board import Board

pygame.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
RUN = True
clock = pygame.time.Clock()

board = Board()
pygame.display.set_caption("Chess")
clicked_pos = None
clicked = False
counter = 0
while RUN:
    clock.tick(10)
    # this will stop the game when the game window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    if pygame.mouse.get_pressed()[0]:
        board.manage_motion()
        # there is a delay so that the game doesn't respond to the same click many times
        pygame.time.delay(200)
pygame.quit()
exit(0)
