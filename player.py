import sys

class Player:
	base_hp = 100
	hp = 100
	x = 0
	y = 3

	def __init__(self, name, profession):
		self.name = name
		self.profession = profession

	def move(self):
		possible_directions = ['left', 'right', 'up', 'down']
		direction = input("Move where: ")

		if direction in possible_directions:
			if direction == 'left':
				self.x -= 1
			if direction == 'right':
				self.x += 1
			if direction == 'up':
				self.y += 1
			if direction == 'down':
				self.y -= 1

			print(self.x, self.y)
		elif direction == 'quit':
			sys.exit()
		else:
			print('not a move')


	def __str__(self):
		return "I am {}, the {}. I have {} hitpoints".format(self.name, self.profession, self.hp)