import pygame, sys, random

pygame.init()

global gameDisplay,clock,borders,BLACK,WHITE,RED,GREEN,BLUE

gameDisplay = pygame.display.set_mode((600,600))  #600x600 w/ 40px borders
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
borders = (40,560)


#Colors
BLACK = (0,0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

