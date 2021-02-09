import string

class Board:
	def __init__(self):
		self.size = int(input('Size of the gameboard : '))
		self.board = [[0 for i in range(self.size)] for j in range(self.size)]


	def __str__(self):
		""" This function returns a string containing the current state of the board """
		schema = ""
		headers = "  "
		alphabet = list(string.ascii_uppercase)
		alphabet.reverse()

		i = 0
		for line in self.board:
			line_txt = ""
			headers += alphabet.pop().__add__(" ")

			line_txt += str(f" {i+1}").__add__(' ' * (i + 1)) if i < 9 else str(i + 1).__add__(' ' * (i + 1))

			for stone in line:
			    if stone == 0:
			        line_txt += "⬡ "
			    elif stone == 1:
			        line_txt += "\033[34m⬢ \033[0m"
			    else:
			        line_txt += "\033[31m⬢ \033[0m"

			schema += line_txt.__add__("\n")

			i = i + 1

		return headers.__add__("\n") + schema