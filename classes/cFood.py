from setup.definitions import *
from setup.settings import *

class Food(object):
	def __init__(self):
		self.size = 10
		self.xPos = random.randint(borders[0],borders[1])
		self.yPos = random.randint(borders[0],borders[1])
		self.pos = (self.xPos,self.yPos)
		self.img = pygame.image.load('images/food.png')
		self.img = pygame.transform.scale(self.img,(self.size,self.size))
	def displaySelf(self):
		gameDisplay.blit(self.img,self.pos)