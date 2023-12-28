#david modified

import sys
import random

# Set up the constants:
BOARD_WIDTH = 16  # (!) Try changing this to 4 or 40.
BOARD_HEIGHT = 14  # (!) Try changing this to 4 or 20.
MOVES_PER_GAME = 20  # (!) Try changing this to 3 or 300.

# Constants for the different shapes used in colorblind mode:
HEART     = chr(9829)  # Character 9829 is '♥'.
DIAMOND   = chr(9830)  # Character 9830 is '♦'.
SPADE     = chr(9824)  # Character 9824 is '♠'.
CLUB      = chr(9827)  # Character 9827 is '♣'.
BALL      = chr(9679)  # Character 9679 is '●'.
TRIANGLE  = chr(9650)  # Character 9650 is '▲'.

BLOCK     = chr(9608)  # Character 9608 is '█'
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
UPDOWN    = chr(9474)  # Character 9474 is '│'
DOWNRIGHT = chr(9484)  # Character 9484 is '┌'
DOWNLEFT  = chr(9488)  # Character 9488 is '┐'
UPRIGHT   = chr(9492)  # Character 9492 is '└'
UPLEFT    = chr(9496)  # Character 9496 is '┘'
# A list of chr() codes is at https://inventwithpython.com/chr

# All the color/shape tiles used on the board:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
              3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'


def getNewBoard():
    """Return a dictionary of a new Flood It board."""

    # Keys are (x, y) tuples, values are the tile at that position.
    board = {}

    # Create random colors for the board.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    # Make several tiles the same as their neighbor. This creates groups
    # of the same color/shape.
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board

def displayBoard(board, displayMode):
    # Display each row:
    for y in range(BOARD_HEIGHT):
        if y == 0:  # The first row begins with '>'.
            print('>', end='')
        else:  # Later rows begin with a white vertical line.
            print(UPDOWN, end='')

        # Display each tile in this row:
        for x in range(BOARD_WIDTH):
            if displayMode == COLOR_MODE:
                print(BLOCK, end='')
            elif displayMode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        print(UPDOWN)  # Rows end with a white vertical line.
    # Display the bottom edge of the board:
    print(UPRIGHT + (LEFTRIGHT * BOARD_WIDTH) + UPLEFT)


print("""一次打印多行訊息aaa
一次打印多行訊息bbb
一次打印多行訊息ccc
一次打印多行訊息ddd""")

gameBoard = {}
gameBoard = getNewBoard()

"""
for x in range(BOARD_WIDTH):
    for y in range(BOARD_HEIGHT):
        gameBoard[(x, y)] = random.choice(TILE_TYPES)


for x in range(BOARD_WIDTH):
    for y in range(BOARD_HEIGHT):
        print(SHAPES_MAP[gameBoard[(x, y)]], end='')
"""

displayMode = SHAPE_MODE
#displayMode = COLOR_MODE

displayBoard(gameBoard, displayMode)

