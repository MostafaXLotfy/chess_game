from chess_components.elephant import Elephant
from chess_components.horse import Horse
from chess_components.king import King
from chess_components.pawn import Pawn
from chess_components.queen import Queen
from chess_components.rock import Rock
from grapics_and_motion.motionmanger import MotionManger
from grapics_and_motion.position import Position


class Board:

    def __init__(self):
        # a dictionary that will holds the pieces on the board and their locations as the key
        self.__white_pieces = {}
        self.__black_pieces = {}
        # a dictionary that will hold the positions on the board
        # each position is a key that is mapped to a rectangle drawn on
        self.__tuples_to_rectangles = {}
        # dictionary with a tuple of as the key and instance of position as value
        self.__tuples_to_positions = {}
        self.__initialize_board()
        self.__initialize_pieces()
        self.__motion_manger = MotionManger(self.__tuples_to_rectangles, self.__tuples_to_positions, self.__white_pieces, self.__black_pieces)
        self.__motion_manger.render()

    # this method will initialize pieces and their position on the board at the start of the game
    def __initialize_pieces(self):
        self.__black_pieces[(1, 1)] = Rock(self.__tuples_to_positions[(1, 1)], "black", "images/black_rock.png")
        self.__black_pieces[(8, 1)] = Rock(self.__tuples_to_positions[(8, 1)], "black", "images/black_rock.png")
        self.__black_pieces[(2, 1)] = Horse(self.__tuples_to_positions[(2, 1)], "black", "images/black_horse.png")
        self.__black_pieces[(7, 1)] = Horse(self.__tuples_to_positions[(7, 1)], "black", "images/black_horse.png")
        self.__black_pieces[(3, 1)] = Elephant(self.__tuples_to_positions[(3, 1)], "black", "images/black_elephant.png")
        self.__black_pieces[(6, 1)] = Elephant(self.__tuples_to_positions[(6, 1)], "black", "images/black_elephant.png")
        self.__black_pieces[(4, 1)] = Queen(self.__tuples_to_positions[(4, 1)], "black", "images/black_queen.png")
        self.__black_pieces[(5, 1)] = King(self.__tuples_to_positions[(5, 1)], "black", "images/black_king.png")

        self.__white_pieces[(1, 8)] = Rock(self.__tuples_to_positions[(1, 8)], "white", "images/white_rock.png")
        self.__white_pieces[(8, 8)] = Rock(self.__tuples_to_positions[(8, 8)], "white", "images/white_rock.png")
        self.__white_pieces[(2, 8)] = Horse(self.__tuples_to_positions[(2, 8)], "white", "images/white_horse.png")
        self.__white_pieces[(7, 8)] = Horse(self.__tuples_to_positions[(7, 8)], "white", "images/white_horse.png")
        self.__white_pieces[(3, 8)] = Elephant(self.__tuples_to_positions[(3, 8)], "white", "images/white_elephant.png")
        self.__white_pieces[(6, 8)] = Elephant(self.__tuples_to_positions[(6, 8)], "white", "images/white_elephant.png")
        self.__white_pieces[(4, 8)] = Queen(self.__tuples_to_positions[(4, 8)], "white", "images/white_queen.png")
        self.__white_pieces[(5, 8)] = King(self.__tuples_to_positions[(5, 8)], "white", "images/white_king.png")
        for i in range(1, 9):
            self.__black_pieces[(i, 2)] = Pawn(self.__tuples_to_positions[(i, 2)], "black", "images/black_pawn.png")
            self.__white_pieces[(9 - i, 7)] = Pawn(self.__tuples_to_positions[(9 - i, 7)], "white", "images/white_pawn.png")

    def manage_motion(self):
        self.__motion_manger.manage_motion()

    def __initialize_board(self):
        for i in range(1, 9):
            for j in range(1, 9):
                self.__tuples_to_positions[(i, j)] = Position(i, j, "images/square1.png") if (i + j) % 2 == 0 \
                           else Position(i, j, "images/square2.png")
                self.__tuples_to_rectangles[(i, j)] = self.__tuples_to_positions[(i, j)].rect
