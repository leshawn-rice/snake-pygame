from setup.settings import *
from classes.cSnake import *
from classes.cFood import *

def quitGame():
	pygame.quit()
	sys.exit()

def displayText(text,size,xyPos):
	font = pygame.font.Font("freesansbold.ttf",size)
	nText = font.render(text,True,BLACK,GREEN)
	gameDisplay.blit(nText,xyPos)

def playMusic(song):
	pygame.mixer.music.load(song)
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)

def updateScreen():
	pygame.display.update()
	clock.tick(120)

def fillScreen():
	gameDisplay.fill(WHITE) #White bg
	pygame.draw.rect(gameDisplay, BLACK, (20, 30, borders[1], borders[1]), 8) #Border
	pygame.draw.rect(gameDisplay, GREEN, (20, 30, borders[1], borders[1])) #Game Screen


def handleKeyPresses(snake,event):
	if event.key == pygame.K_UP:
		if snake.dir == "down":
			return
		else:
			snake.dir = "up"
			snake.xChange = 0
			snake.yChange = -(snake.speed)
	elif event.key == pygame.K_DOWN:
		if snake.dir == "up":
			return
		else:
			snake.dir = "down"
			snake.xChange = 0
			snake.yChange = (snake.speed)
	elif event.key == pygame.K_RIGHT:
		if snake.dir == "left":
			return
		else:
			snake.dir = "right"
			snake.xChange = (snake.speed)
			snake.yChange = 0
	elif event.key == pygame.K_LEFT:
		if snake.dir == "right":
			return
		else:
			snake.dir = "left"
			snake.xChange = -(snake.speed)
			snake.yChange = 0
	elif event.key == pygame.K_ESCAPE:
		pauseGame()

def checkQuit(event):
	if event.type == pygame.QUIT:
		quitGame()

def createFood():
	food = Food()
	return food

def loseGame():
	lost = True
	while lost:
		fillScreen()
		displayText('You Lost!',45,(200,200))
		displayText('Press Enter to play again!',32,(125,280))
		displayText('Press Esc to exit the game!',32,(125,320))
		displayText('Your score was {0}'.format(score),32,(125,360))
		for event in pygame.event.get():
			checkQuit(event)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					lost = False
					quitGame()
				if event.key == pygame.K_RETURN:
					lost = False
					menu()
		updateScreen()


def pauseGame():
	paused = True
	while paused:
		fillScreen()
		displayText('PAUSED',64,(170,200))
		displayText('Press Esc to continue...',32,(120,280))
		for event in pygame.event.get():
			checkQuit(event)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					paused = False
		updateScreen()

def menu():
	inMenu = True
	playMusic('music/menuMusic.mp3')
	while inMenu:
		fillScreen()
		displayText('Welcome to Snake',45,(90,200))
		displayText('Press Enter to Play!',32,(125,280))
		for event in pygame.event.get():
			checkQuit(event)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					inMenu = False
					gameLoop()
		updateScreen()

def gameLoop():
	snake = Snake()
	food = createFood()

	global score
	score = 0

	gameOver = False

	playMusic('music/gameMusic.mp3')

	while not gameOver:
		fillScreen()
		snake.displaySelf()
		food.displaySelf()

		for event in pygame.event.get():
			checkQuit(event)
			if event.type == pygame.KEYDOWN:
				handleKeyPresses(snake,event)

		for i in range(snake.size):
			if ((food.xPos)<(snake.xPos+i)<(food.xPos+food.size)) and ((food.yPos)<(snake.yPos+i)<(food.yPos+food.size)):
				for j in range(4): snake.addBody()
				score += 1
				food = createFood()

		snake.xPos += snake.xChange
		snake.yPos += snake.yChange

		updateScreen()
