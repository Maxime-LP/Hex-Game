import re
import string

def get_x_index(letter):
    """ The X index is the "line" part of the board. Because coordinate is a letter to represent her,
    we need his position in alphabet.
    To begin at the 1 index, we add 1 to list index. """
    return list(string.ascii_uppercase).index(letter.upper()) + 1


def get_coord(position):
    """ Using a regex, this function checks if the position is correct """
    regex = re.match("^([a-zA-Z]{1})([0-9]{1,2})$", position)

    return regex.groups() if regex is not None else regex

def is_outside(board, line, column):
    """
    Check if the stone can be put inside the board
    """
    length = len(board)
    return length <= line or length <= column


def is_already_taken(board, line, column):
    """ Check if the place is already taken """
    return board[column][line] == 1