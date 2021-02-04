from coords import *

class Player:

	def __init__(self, name, color):
		self.name = name
		self.color = color

	def put_stone(self, coords, board, turn):
	    new_board = board[:]
	    if coords is None:
	        raise ValueError("Coordinates for the stone is incorrect. Please, pick a new one")

	    line = get_x_index(coords[0]) - 1
	    column = int(coords[1]) - 1

	    if is_outside(board, line, column):
	        raise ValueError("Stone can't be put outside the board")

	    if is_already_taken(board, line, column):
	        raise ValueError("A stone already exists at this position")

	    new_board[column][line] = turn + 1

	    return new_board
