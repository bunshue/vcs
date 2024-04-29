"""Hungry Robots, by Al Sweigart al@inventwithpython.com
Escape the hungry robots by making them crash into each other.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game"""

import random, sys

# Set up the constants:
WIDTH = 40           # (!) Try changing this to 70 or 10.
HEIGHT = 20          # (!) Try changing this to 10.
NUM_ROBOTS = 10      # (!) Try changing this to 1 or 30.
NUM_TELEPORTS = 2    # (!) Try changing this to 0 or 9999.
NUM_DEAD_ROBOTS = 2  # (!) Try changing this to 0 or 20.
NUM_WALLS = 100      # (!) Try changing this to 0 or 300.

EMPTY_SPACE = ' '    # (!) Try changing this to '.'.
PLAYER = '@'         # (!) Try changing this to 'R'.
ROBOT = 'R'          # (!) Try changing this to '@'.
DEAD_ROBOT = 'X'     # (!) Try changing this to 'R'.

# (!) Try changing this to '#' or 'O' or ' ':
WALL = chr(9617)  # Character 9617 is '░'


def main():
    # Set up a new game:
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    displayBoard(board, robots, playerPosition)


def getNewBoard():
    """Returns a dictionary that represents the board. The keys are
    (x, y) tuples of integer indexes for board positions, the values are
    WALL, EMPTY_SPACE, or DEAD_ROBOT. The dictionary also has the key
    'teleports' for the number of teleports the player has left.
    The living robots are stored separately from the board dictionary."""
    board = {'teleports': NUM_TELEPORTS}

    # Create an empty board:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # Add walls on the edges of the board:
    for x in range(WIDTH):
        board[(x, 0)] = WALL  # Make top wall.
        board[(x, HEIGHT - 1)] = WALL  # Make bottom wall.
    for y in range(HEIGHT):
        board[(0, y)] = WALL  # Make left wall.
        board[(WIDTH - 1, y)] = WALL  # Make right wall.

    # Add the random walls:
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # Add the starting dead robots:
    for i in range(NUM_DEAD_ROBOTS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    """Return a (x, y) integer tuple of an empty space on the board."""
    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    """Return True if the (x, y) is empty on the board and there's also
    no robot there."""
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def addRobots(board):
    """Add NUM_ROBOTS number of robots to empty spaces on the board and
    return a list of these (x, y) spaces where robots are now located."""
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x, y))
    return robots


def displayBoard(board, robots, playerPosition):
    """Display the board, robots, and player on the screen."""
    # Loop over every space on the board:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Draw the appropriate character:
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == playerPosition:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()  # Print a newline.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
