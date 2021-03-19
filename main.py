import pygame
# import random
import time

pygame.init()  # Initialises pygame


def ping():
    # Player code
    playerImg = pygame.image.load("pingLeft96.png")
    playerX = 0
    playerY = 202
    playerYMove = 0

    # Opponent
    oppImg = pygame.image.load("pingRight96.png")
    oppX = 800
    oppY = 202
    oppYMove = 0
    # oppXMove = 0

    # Ball
    ballImg = pygame.image.load("ball32.png")
    ballX = 434
    ballY = 234
    ballXMove = -0.1
    ballYMove = 0.1
    # ballBeginY = random.randint(0, 1)
    # ballBeginX = random.randint(0, 1)
    ballBuildUp = 1.5

    # Text code
    font = pygame.font.Font("freesansbold.ttf", 32)
    winFont = font.render("YOU WIN", True, (255, 255, 255))
    loseFont = font.render("YOU LOSE", True, (225, 225, 225))

    def player(x, y):
        screen.blit(playerImg, (x, y))

    def opponent(x, y):
        screen.blit(oppImg, (x, y))

    def ball(x, y):
        screen.blit(ballImg, (x, y))

    def win():
        screen.blit(winFont, (200, 250))
        pygame.display.update()

    def lose():
        screen.blit(loseFont, (200, 250))
        pygame.display.update()

    pingRunning = True
    while pingRunning:
        screen.fill((0, 0, 0))
        # Checks for inputs
        for gameEvent in pygame.event.get():
            if gameEvent.type == pygame.QUIT:
                pingRunning = False
            if gameEvent.type == pygame.KEYDOWN:
                if gameEvent.key == pygame.K_UP:
                    playerYMove = -0.3
                if gameEvent.key == pygame.K_DOWN:
                    playerYMove = 0.3
            if gameEvent.type == pygame.KEYUP:
                if gameEvent.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    playerYMove = 0

        # Ball movement
        ballY += ballYMove
        ballX += ballXMove
        # Ball border collision
        if ballY <= 0:
            ballYMove = -ballYMove
        if ballY >= 466:
            ballYMove = -ballYMove
        # Opponent ball collision
        if (ballY + 16 >= oppY) and (ballY + 16 <= oppY + 96):
            # Builds the speed when colliding with the Opponent, up to a point
            if ballX >= oppX + 10:
                if 1 > ballXMove > -1:
                    ballXMove = -ballXMove * ballBuildUp
                    ballYMove *= ballBuildUp
                else:
                    ballXMove = -ballXMove
        # Player ball collision
        if (ballY + 16 >= playerY) and (ballY + 16 <= playerY + 96):
            if ballX <= playerX + 55:
                # Builds the speed when colliding with the player, up to a point
                if 1 > ballXMove > -1:
                    ballXMove = -ballXMove * ballBuildUp
                    ballYMove *= ballBuildUp
                else:
                    ballXMove = -ballXMove

        # Opponent follows ball
        oppY = ballY + 16

        # Player movement and border collision
        playerY += playerYMove
        if playerY <= 0:
            playerY = 0
        if playerY >= 404:
            playerY = 404

        # Opponent movement and border collision
        oppY += oppYMove
        if oppY <= 0:
            oppY = 0
        if oppY >= 404:
            oppY = 404

        # Win or lose
        if ballX >= 900:
            win()
            time.sleep(3)
            pingRunning = False
        if ballX <= -50:
            lose()
            time.sleep(3)
            pingRunning = False

        # Updates screen
        ball(ballX, ballY)
        opponent(oppX, oppY)
        player(playerX, playerY)
        pygame.display.update()


# Make screen
screen = pygame.display.set_mode((900, 500))  # Sets the size of the window
pygame.display.set_caption("Ping")  # Changes the window heading
pygame.display.set_icon(pygame.image.load("pingIcon96.png"))  # Gives the window a specific image for the icon

# Launch game
ping()

# Replay text code
replayFont = pygame.font.Font("freesansbold.ttf", 64)
replayText = replayFont.render("REPLAY?", True, (255, 255, 255))

# Button text
yesNoFont = pygame.font.Font("freesansbold.ttf", 32)
yesText = yesNoFont.render("YES", True, (255, 255, 255))
noText = yesNoFont.render("NO", True, (255, 255, 255))

running = True
while running:
    # Gets the mouse x and y position
    mousePos = pygame.mouse.get_pos()

    # Refreshes the screen to black so updates can be made
    screen.fill((0, 0, 0))

    # Puts the boxes and text on screen
    screen.blit(replayText, (200, 250))

    # Looks for events
    for event in pygame.event.get():
        # If the player presses the exit window button, then quit the program
        if event.type == pygame.QUIT:
            running = False
        # If the player clicks, check if they've clicked over one of the buttons
        if event.type == pygame.MOUSEBUTTONUP:
            # Have they clicked over the "yes" button? If so, call the ping() method
            if 225 < mousePos[0] < 325 and 325 < mousePos[1] < 375:
                ping()
            # Have they clicked over the "no" button? If so, exit the loop and program as a result
            if 375 < mousePos[0] < 475 and 325 < mousePos[1] < 375:
                running = False

    # If the mouse is over the yes box or no box, change the colour
    if 225 < mousePos[0] < 325 and 325 < mousePos[1] < 375:
        pygame.draw.rect(screen, (115, 255, 152), (225, 325, 100, 50))
    else:
        pygame.draw.rect(screen, (255, 255, 255), (225, 325, 100, 50))

    if 375 < mousePos[0] < 475 and 325 < mousePos[1] < 375:
        pygame.draw.rect(screen, (255, 97, 102), (375, 325, 100, 50))
    else:
        pygame.draw.rect(screen, (255, 255, 255), (375, 325, 100, 50))

    # Adds the "yes" and "no" text to the buttons
    screen.blit(yesText, (225, 325))
    screen.blit(noText, (375, 325))

    # Updates the screen on every loop
    pygame.display.update()
