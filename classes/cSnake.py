import setup.definitions
from setup.definitions import *
from setup.settings import *

class Snake(object):
	def __init__(self):
		self.size = 15
		self.speed = 2.5
		self.xPos = 100 #Starting x pos
		self.xChange = 0
		self.yChange = 0
		self.yPos = 100 #Starting y pos
		self.headPos = (self.xPos,self.yPos)
		self.img = pygame.image.load('images/head.png')
		self.img = pygame.transform.scale(self.img,(self.size,self.size))
		self.dir = None
		self.bodyArray = [] #Essentially linked list for bodies
	def displaySelf(self):
		self.updateHeadPos()
		self.updateBody()
		gameDisplay.blit(self.img,self.headPos)
		for body in self.bodyArray:
			gameDisplay.blit(self.img,body[0])
	def updateHeadPos(self):
		self.headPos = (self.xPos,self.yPos)
		for body in self.bodyArray:
			if self.headPos == body[0]:
				setup.definitions.loseGame()
				setup.definitions.quitGame()
		if self.headPos[0]<borders[0]-24 or self.headPos[0]>borders[1]+12:
			setup.definitions.loseGame()
			setup.definitions.quitGame()
		if self.headPos[1]<borders[0]-13 or self.headPos[1]>borders[1]+18:
			setup.definitions.loseGame()
			setup.definitions.quitGame()
	def updateBody(self):
		newPos = self.headPos
		for body in self.bodyArray:
			body[0] = body[1]
			body[1] = newPos
			newPos = body[0]
	def addBody(self):
		if not self.bodyArray:
			self.bodyArray.append([self.headPos,self.headPos])
		else:
			self.bodyArray.append([self.bodyArray[-1][0], self.bodyArray[-1][1]])