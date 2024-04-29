import sys, os

# Maze file constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'  # (!) Try changing this to '+' or 'o'.
BLOCK = chr(9617)  # Character 9617 is '░'

def displayMaze(maze):
    # Display the maze:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end='')
            elif (x, y) == (exitx, exity):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
        print()  # Print a newline after printing the row.


print('Maze files found in', os.getcwd())
for fileInCurrentFolder in os.listdir():
    if (fileInCurrentFolder.startswith('maze') and
        fileInCurrentFolder.endswith('.txt')):
        print('  ', fileInCurrentFolder)

filename = 'maze75x11s1.txt'

# Load the maze from a file:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
print(lines)
playerx = None
playery = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

displayMaze(maze)

