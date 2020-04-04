import setup.definitions
from setup.definitions import *
from setup.settings import *


class Snake(object):
    def __init__(self):
        '''
        Called when a snake object is initialized.
        Creates the head of the snake and sets the
        size and speed of the snake
        '''
        self.size = 15
        self.speed = 2.5
        self.xPos = 100  # Starting x pos
        self.xChange = 0
        self.yChange = 0
        self.yPos = 100  # Starting y pos
        self.headPos = (self.xPos, self.yPos)
        self.img = pygame.image.load('images/head.png')
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        self.dir = None
        self.bodyArray = []  # Essentially linked list for bodies

    def displaySelf(self):
        '''
        Displays the snake's head and body to the screen
        '''
        self.updateHeadPos()
        self.updateBody()
        gameDisplay.blit(self.img, self.headPos)
        for body in self.bodyArray:
            gameDisplay.blit(self.img, body[0])

    def updateHeadPos(self):
        '''
        Updates the position of the head based on the
        x-y coordinates of the snake, then checks for collisions
        '''
        self.headPos = (self.xPos, self.yPos)
        for body in self.bodyArray:
            if self.headPos == body[0]:  # Check collision w/ body
                setup.definitions.loseGame()
                setup.definitions.quitGame()
        # Check for wall collision on x-axis (left or right wall)
        if self.headPos[0] < borders[0]-24 or self.headPos[0] > borders[1]+12:
            setup.definitions.loseGame()
            setup.definitions.quitGame()
        # Check for wall collision on y-axis (top or bottom wall)
        if self.headPos[1] < borders[0]-13 or self.headPos[1] > borders[1]+18:
            setup.definitions.loseGame()
            setup.definitions.quitGame()

    def updateBody(self):
        '''
        Updates the position of each of the snake's bodies
        '''
        newPos = self.headPos
        for body in self.bodyArray:
            body[0] = body[1]
            body[1] = newPos
            newPos = body[0]

    def addBody(self):
        '''
        Adds a body to the linked-list of bodies for the snake
        '''
        if not self.bodyArray:
            self.bodyArray.append([self.headPos, self.headPos])
        else:
            self.bodyArray.append(
                [self.bodyArray[-1][0], self.bodyArray[-1][1]])
