from chess_components.piece import Piece
from grapics_and_motion.position import Position


class Horse(Piece):

    def __init__(self, position, color, image):
        super().__init__(position, color, image)
        # list that holds the steps pawn could take to move as an instance of class Position
        self.__move_steps = [Position(2, -1), Position(2, 1), Position(-2, 1), Position(-2, -1), Position(1, -2),
                             Position(-1, -2), Position(1, 2), Position(-1, 2)]

    def calculate_moves(self, white: dict, black: dict):
        moves, enemies = [], []
        for move in self.__move_steps:
            possible_move = (move + self.position).tuple
            if 0 < possible_move[0] < 9 and 0 < possible_move[1] < 9:
                if possible_move in white and self.color == "white" or possible_move in black and self.color == "black":
                    pass
                elif possible_move in white and self.color == "black" or possible_move in black and self.color == "white":
                    enemies.append(possible_move)
                elif possible_move not in white and possible_move not in black:
                    moves.append(possible_move)
        return moves, enemies
