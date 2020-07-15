from chess_components.piece import Piece
from grapics_and_motion.position import Position


class Pawn(Piece):

    def __init__(self, position, color, image):
        super().__init__(position, color, image)
        # list that holds the steps pawn could take to move as an instance of class Position
        self.__move_steps = [Position(0, 1), Position(0, 2)]
        # list that holds the steps pawn could take to kill enemy if possible as an instance of class position
        self.__kill_steps = [Position(-1, 1), Position(1, 1)]
        self.__first_move = True

    def calculate_moves(self, white: dict, black: dict):
        # list that will hold the positions of possible moves the piece could move to
        moves = []
        # list that will hold the positions of possible enemies the piece could kil
        enemies = []

        # calculating positions of possible moves
        for move in self.__move_steps:
            possible_move = self.position - move if self.color == "white" else self.position + move
            possible_move = possible_move.tuple
            if self.color == "white" and possible_move in white or self.color == "black" and possible_move in black:
                break
            if possible_move not in white and possible_move not in black and 0 < possible_move[0] < 9 and 0 < possible_move[1] < 9:
                moves.append(possible_move)

        # calculating positions of possible enemies
        for enemy in self.__kill_steps:
            possible_enemy = self.position - enemy if self.color == "white" else self.position + enemy
            possible_enemy = possible_enemy.tuple
            if (self.color == "white" and possible_enemy in black) or (self.color == "black" and possible_enemy in white):
                if 0 < possible_enemy[0] < 9 and 0 < possible_enemy[1] < 9:
                    enemies.append(possible_enemy)

        return moves, enemies

    def change_pos(self, position):
        super(Pawn, self).change_pos(position)
        if self.__first_move:
            self.__move_steps.pop()
            self.__first_move = False
