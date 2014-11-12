import random
from player import Player


class Game():
	GRID = ([0, 0], [0, 1], [0, 2], [0, 3],
			[1, 0], [1, 1], [1, 2], [1, 3],
			[2, 0], [2, 1], [2, 2], [2, 3],
			[2, 0], [3, 1], [3, 2], [3, 3])


	def showCurrentGrid(self):
		pass
		#for index, cell in enumerate(self.GRID)
		#	if index in [0, 1, 2, 3, 4, 6, 7]

	def runGameLoop(self, player): 
		while True:
			self.showCurrentGrid()
			player.move()	

	def createCharacter(self):
		player = Player(self.name, self.profession)
		print(player)
		self.runGameLoop(player)

	
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
		
		self.createCharacter()
		#self.showCurrentGrid()


	def getCharacterInformation(self):
		self.name = input("Player Name: ").title()

		if len(self.name) >= 1:
			print("---------------------\n")
			print("------Welcome {}-----\n".format(self.name))
			print("---------------------\n")
			self.getCharacterClass()

		else:
			self.getCharacterInformation()	


	def __init__(self):
		self.getCharacterInformation()


game = Game()
