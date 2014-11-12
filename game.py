import random
from player import Player


class Game():
	GRID = ([0,0], [0,1], [0,2],
			[1,0], [1,1], [1,2],
			[2,0], [2,1], [2,2])


	def showCurrentGrid(self):
		pass
		#for index, cell in enumerate(self.GRID)
		#	if index in [0, 1, 2, 3, 4, 6, 7]

	def createCharacter(self, playerData):
		player = Player(playerData)

	
	def getCharacterClass(self):
		print("Are you a [W]arrior, [M]agician, or [B]owman?")
		self.profession = input("Class: ")

		if self.profession == 'w':
			self.profession = "Warrior"
		elif self.profession == 'm':
			self.profession = "Magician"
		elif self.profession == 'b':
			self.profession = "Bowman"
		else:
			self.getCharacterClass()
			return

		print("Thanks {}, you are a {}.".format(self.name, self.profession))
		self.createCharacter((self.name, self.profession))
		self.showCurrentGrid()


	def getCharacterInformation(self):
		
		self.name = input("Player Name: ")

		if len(self.name) >= 1:
			print("---------------------\n")
			print("Welcome {}".format(self.name))
			print("---------------------\n")
			self.getCharacterClass()

		else:
			self.getCharacterInformation()	


	def __init__(self):
		self.getCharacterInformation()


game = Game()
