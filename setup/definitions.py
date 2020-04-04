from setup.settings import *
from classes.cSnake import *
from classes.cFood import *


def quitGame():
    '''
    Performs the function of quitting the game
    '''
    pygame.quit()
    sys.exit()


def checkQuit(event):
    '''
    Checks to see if the user clicked the X button on the window
    '''
    if event.type == pygame.QUIT:
        quitGame()


def displayText(text, size, xyPos):
    '''
    Takes in a string, size int, and xy tuple as arguments,
    and displays the given string with the given size to the given location
    '''
    font = pygame.font.Font("freesansbold.ttf", size)
    nText = font.render(text, True, BLACK, GREEN)
    gameDisplay.blit(nText, xyPos)


def playMusic(song):
    '''
    Plays a song given as a string value if it exists.
    If that file doesn't exist it prints an error to the
    command line and skips the song
    '''
    try:
        pygame.mixer.music.load(song)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("ERROR: Couldn\'t play the song \"{0}\"".format(song))


def updateScreen():
    '''
    Uodates the screen with an FPS of 120
    '''
    pygame.display.update()
    clock.tick(120)


def fillScreen():
    '''
    Fills the screen with a white bg,
    and a green screen w/ a black border
    '''
    gameDisplay.fill(WHITE)  # White bg
    pygame.draw.rect(gameDisplay, BLACK,
                     (20, 30, borders[1], borders[1]), 8)  # Border
    pygame.draw.rect(gameDisplay, GREEN,
                     (20, 30, borders[1], borders[1]))  # Game Screen


def createFood():
    '''
    Creates another food object in a random xy position
    '''
    food = Food()
    return food


def handleKeyPresses(snake, event):
    '''
    Given a snake object and an event as args,
    listens for key presses and moves the
    snake/pauses the game
    '''
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


def pauseGame():
    '''
    Pauses the game state using the Esc key,
    unpauses with the same key
    '''
    paused = True
    while paused:
        fillScreen()
        displayText('PAUSED', 64, (170, 200))
        displayText('Press Esc to continue...', 32, (120, 280))
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
        updateScreen()


def loseGame():
    '''
    Enacts the lost-game game state,
    tells the user their score, and
    prompts them to quit or play again,
    taking them to the menu
    '''
    lost = True
    while lost:
        fillScreen()
        displayText('You Lost!', 45, (200, 200))
        displayText('Press Enter to play again!', 32, (125, 280))
        displayText('Press Esc to exit the game!', 32, (125, 320))
        displayText('Your score was {0}'.format(score), 32, (125, 360))
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


def gameLoop():
    '''
    This function actually plays the game.
    Listens for events such as key presses
    and interactions with the window, and
    updates the score and the position of the snake
    '''
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
                handleKeyPresses(snake, event)
        for i in range(snake.size):
            if ((food.xPos) < (snake.xPos+i) < (food.xPos+food.size)) and
            ((food.yPos) < (snake.yPos+i) < (food.yPos+food.size)):
                for j in range(4):
                    snake.addBody()
                score += 1
                food = createFood()
        snake.xPos += snake.xChange
        snake.yPos += snake.yChange
        updateScreen()


def menu():
    '''
    Plays the menu song, welcomes the player,
    and prompts them to press Enter to start the game
    '''
    inMenu = True
    playMusic('music/menuMusic.mp3')
    while inMenu:
        fillScreen()
        displayText('Welcome to Snake', 45, (90, 200))
        displayText('Press Enter to Play!', 32, (125, 280))
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inMenu = False
                    gameLoop()
        updateScreen()
