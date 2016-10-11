import pygame, sys
from pygame.locals import *

FPS = 75
#WINDOW
WINDOWWIDTH = 1200
WINDOWHEIGHT = 900

#PADDLE AND STUFF
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

#COLOURS
BLACK = (0,  0,  0)
WHITE = (255,255,255)

def drawarena():
    DISPLAYSURF.fill((0,0,0))
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWWIDTH)))
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0), ((WINDOWWIDTH/2))


def drawPaddle(paddle):
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    pygame.draw.rect(DISPLAYSURF, WHITE, Paddle)

def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, Paddle)
#IMPORTANT STUFF PROBABLY
def main():
    pygame.init()
    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pong')

    # BALL AND PADDLE
    ballX = WINDOWWIDTH / 2 - LINETHICKNESS / 2
    ballY = WINDOWHEIGHT / 2 - LINETHICKNESS / 2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) / 2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) / 2

    # WE DON'T UNDERSTAND THIS BIT
    paddle1 = pygame.Rect(PADDLEOFFSET, playerOnePosition, LINETHICKNESS, PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS, PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    # pretty drawing
    drawarena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    drawarena();
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    pygame.display.update()
    FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main();