import pygame

from grapics_and_motion.position import coordinates_to_position


# this class will be used to detect if a position is clicked on the screen or not
class MotionManger:
    def __init__(self, tuples_to_rectangles, tuples_to_positions, white_pieces, black_pieces):

        # these dictionaries has a tuple that represents a position on the board like (1,1), (2,2) as keys
        # holds all rectangles on the board that are used to detect where the mouse is clicked
        self.__tuples_to_rectangles = tuples_to_rectangles
        # holds white_pieces on the board
        self.__white_pieces = white_pieces
        # holds black_pieces on the board
        self.__black_pieces = black_pieces
        # holds all positions on the board
        self.__tuples_to_positions = tuples_to_positions

        # flags that represents which player turn to play
        self.__white_turn = False
        self.__black_Turn = True

        # a flag that represents if there is a piece clicked
        self.__piece_clicked = False
        # position of the clicked piece and the piece its self
        self.__clicked_piece_position = None
        self.__clicked_piece = None

        # moves available for current selected piece
        self.__piece_moves = None
        self.__piece_enemies = None

    """this function will get what position on the board was clicked and perform 
    the appropriate action according to the click"""

    def manage_motion(self):
        clicked_coordinates = pygame.mouse.get_pos()
        clicked_pos = coordinates_to_position(*clicked_coordinates)

        #  this will determine which peace the player selected and show the available moves of this piece
        if not self.__piece_clicked:
            # this will select white pieces if only white player is to play
            if clicked_pos in self.__white_pieces and self.__white_turn:
                self.__piece_clicked = True
                self.__clicked_piece_position = clicked_pos
                self.__clicked_piece = self.__white_pieces[clicked_pos]
                self.__show_moves()
            # this will select black pieces if only black player is to play
            elif clicked_pos in self.__black_pieces and self.__black_Turn:
                self.__piece_clicked = True
                self.__clicked_piece_position = clicked_pos
                self.__clicked_piece = self.__black_pieces[clicked_pos]
                self.__show_moves()

        # this will hide the moves of a piece if the piece is selected again or another space that is not valid
        elif self.__piece_clicked and clicked_pos == self.__clicked_piece_position:
            self.__piece_clicked = False
            self.__piece_enemies, self.__piece_clicked = None, None
            self.render()

        # this will move the piece if an empty space is clicked after piece is selected
        # it will move the piece only to a valid place
        elif self.__piece_clicked and clicked_pos in self.__piece_moves:
            self.__piece_clicked = False
            self.__move_piece(clicked_pos)
            self.__toggle_turns()

        # this will kill an enemy piece and the current piece will move to that position
        elif self.__piece_clicked and ((clicked_pos in self.__white_pieces and self.__black_Turn) or
                 (self.__piece_clicked and clicked_pos in self.__black_pieces and self.__white_turn)) and clicked_pos in self.__piece_enemies:
            self.__piece_clicked = False
            self.__kill_piece(clicked_pos)
            self.__toggle_turns()

    # this is used to change player turn
    def __toggle_turns(self):
        if self.__black_Turn:
            self.__white_turn = True
            self.__black_Turn = False
        else:
            self.__white_turn = False
            self.__black_Turn = True

    def __show_moves(self):
        self.__piece_moves, self.__piece_enemies = self.__clicked_piece.calculate_moves(self.__white_pieces, self.__black_pieces)
        for move in self.__piece_moves:
            self.__tuples_to_positions[move].set_as_move()
        for enemy in self.__piece_enemies:
            self.__tuples_to_positions[enemy].set_as_enemy()

    def __move_piece(self, tuple_to_move):
        position_to_move = self.__tuples_to_positions[tuple_to_move]
        self.__clicked_piece.change_pos(position_to_move)
        if self.__white_turn:
            del self.__white_pieces[self.__clicked_piece_position]
            self.__white_pieces[tuple_to_move] = self.__clicked_piece
        else:
            del self.__black_pieces[self.__clicked_piece_position]
            self.__black_pieces[tuple_to_move] = self.__clicked_piece
        self.render()

    def __kill_piece(self, tuple_for_piece_to_kill):
        if self.__white_turn:
            del self.__black_pieces[tuple_for_piece_to_kill]
        else:
            del self.__white_pieces[tuple_for_piece_to_kill]
        self.__move_piece(tuple_for_piece_to_kill)

    def render(self):
        for position in self.__tuples_to_positions:
            self.__tuples_to_positions[position].render()
        for piece in self.__white_pieces:
            self.__white_pieces[piece].render()
        for piece in self.__black_pieces:
            self.__black_pieces[piece].render()
        pygame.display.update()
