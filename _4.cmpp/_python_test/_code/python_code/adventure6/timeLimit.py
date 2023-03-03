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

# Goal position
goalX = size[0] / 2 - 10
goalY = size[1] / 2 - 10
goalW = 20
goalH = 20

# points
points = 0

# colours
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

    if -10 < y - ballY < 10 and -10 < x - ballX < 10:
        pygame.draw.circle(screen, white, [x, y], 15)

        xDiff = x - ballX
        yDiff = y - ballY

        if ballX == 0:
            xDiff -= 5
        elif ballX == size[0]:
            xDiff += 5
        if ballY == 0:
            yDiff -= 5
        elif ballY == size[1]:
            yDiff += 5

        x += xDiff * 3
        ballX -= xDiff * 3

        y += yDiff * 3
        ballY -= yDiff * 3

# Game loop
done = False

# get current time
timeStart = pygame.time.get_ticks()

while not done:
    screen.fill(black)

    #Draw the goal
    pygame.draw.rect(screen, white, (goalX, goalY, goalW, goalH))

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

    # Draw points
    for point in range(points):
        pointX = 0 + point * 5
        pygame.draw.rect(screen, white, (pointX, 3, 4, 7))

    # draw player
    pygame.draw.circle(screen, red, [x, y], 6)

    # draw ball
    pygame.draw.circle(screen, blue, [ballX, ballY], 6)

    # Check ball is in goal
    if goalX <= ballX <= goalX + goalH and goalY <= ballY <= goalY + goalH:
        points += 1
        ballX = random.randrange(0, size[0])
        ballY = random.randrange(0, size[0])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Check elapsed time
    timeNow = pygame.time.get_ticks()
    if timeNow - timeStart >= 60000:
        done = True

    clock.tick(72)
pygame.quit()
print "Total points: " + str(points)
