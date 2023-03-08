import random
import pygame
pygame.init()
# Window setup
size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# player position
x = size[0] / 2
y = size[1] / 2

# ball position
ballX = random.randrange(0, size[0])
ballY = random.randrange(0, size[1])

# colours
red = pygame.color.Color('#FF8080')
blue = pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')


def checkOffScreenX(x):
    if x > size[0]:
        x = 0
    elif x < 0:
        x = size[0]
    return x


def checkOffScreenY(y):
    if y > size[1]:
        y = 0
    elif y < 0:
        y = size[1]
    return y


def checkTouching():
    """Causes a mini explosion if the players are touching"""
    global x
    global ballX
    global y
    global ballY

    # Check player and ball are touching
    if -5 < y - ballY < 5 and -5 < x - ballX < 5:
        #draw an explosion
        pygame.draw.circle(screen, white, [x, y], 5)

        xDiff = x - ballX
        yDiff = y - ballY

        # check ball on edge of screen
        if ballX == 0:
            xDiff -= 5
        elif ballX == size[0]:
            xDiff += 5
        if ballY == 0:
            yDiff -= 5
        elif ballY == size[1]:
            yDiff += 5

        # move the ball and player
        x += xDiff * 5
        ballX -= xDiff * 5

        y += yDiff * 5
        ballY -= yDiff * 5

# Game loop
done = False
while not done:
    screen.fill(black)

    keys = pygame.key.get_pressed()

    #player movement
    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1

    # Check off screen
    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    ballX = checkOffScreenX(ballX)
    ballY = checkOffScreenY(ballY)

    # Check player is touching the ball
    checkTouching()

    # draw player
    pygame.draw.circle(screen, red, [x, y], 1)

    # draw ball
    pygame.draw.circle(screen, blue, [ballX, ballY], 1)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(72)
pygame.quit()