import sys
import re
import os
from Player import Player
from Board import Board
from coords import get_coord


class Game:

	def __init__(self, board, player1, player2):
		self.board = board
		self.players = [player1, player2]
		self.turn = 0
		self.on = True

	def check_win(self, player_name):
		# if condition de fin: return players_name
		#if no wins, return false
		return False

	def game_over(self, player_name):
			print(f"It's over! {player_name} wins!")


	def play(self):

		while self.on:
			#set first player to first element in self.players list
			currplayer = self.players[self.turn]
			print(self.board)

			position = input(f"{currplayer.name} put a stone on : ")

			os.system('clear')
			print(f"{currplayer.name} put a stone on {position}.")

			coords = get_coord(position)
			
			try:
				self.board.board = currplayer.put_stone(coords, self.board.board, self.turn)
			except ValueError as err:
				print(format(err))

			#checks for a win
			winner = self.check_win(currplayer.name)
			#if win, declare win and break loop
			if winner != False:
				self.game_over(winner)
				self.on = False

			#else, switch turns by flipping index in self.players array
			else:
				self.turn = 1 - self.turn