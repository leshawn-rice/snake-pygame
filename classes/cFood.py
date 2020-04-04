from setup.definitions import *
from setup.settings import *


class Food(object):
    def __init__(self):
        '''
        Called anytime a food object is initialized.
        Puts the food at a random x-y coordinate and
        sets the image and size for the food.
        '''
        self.size = 10
        self.xPos = random.randint(borders[0], borders[1])
        self.yPos = random.randint(borders[0], borders[1])
        self.pos = (self.xPos, self.yPos)
        self.img = pygame.image.load('images/food.png')
        self.img = pygame.transform.scale(self.img, (self.size, self.size))

    def displaySelf(self):
        '''
        Displays the current food object to the
        screen based on the food's current position
        '''
        gameDisplay.blit(self.img, self.pos)
