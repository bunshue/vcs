import random
import sys

EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:
    def __init__(self, originalSetup):
        # originalSetup is a string of 81 characters for the puzzle
        # setup, with numbers and periods (for the blank spaces).
        # See https://inventwithpython.com/sudokupuzzles.txt
        self.originalSetup = originalSetup

        # The state of the sudoku grid is represented by a dictionary
        # with (x, y) keys and values of the number (as a string) at
        # that space.
        self.grid = {}
        self.resetGrid()  # Set the grid state to its original setup.
        self.moves = []  # Tracks each move for the undo feature.

    def resetGrid(self):
        """Reset the state of the grid, tracked by self.grid, to the
        state in self.originalSetup."""
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE

        assert len(self.originalSetup) == FULL_GRID_SIZE
        i = 0  # i goes from 0 to 80
        y = 0  # y goes from 0 to 8
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.originalSetup[i]
                i += 1
            y += 1

    def display(self):
        """Display the current state of the grid on the screen."""
        print('   A B C   D E F   G H I')  # Display column labels.
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    # Display row label:
                    print(str(y + 1) + '  ', end='')

                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:
                    # Display a vertical line:
                    print('| ', end='')
            print()  # Print a newline.

# Load the sudokupuzzles.txt file:
with open('sudokupuzzles.txt') as puzzleFile:
    puzzles = puzzleFile.readlines()

# Remove the newlines at the end of each puzzle:
for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))

"""
while True:  # Main game loop.
    grid.display()

    if action.startswith('R'):

    if action.startswith('N'):
        grid = SudokuGrid(random.choice(puzzles))

    if action.startswith('O'):
        originalGrid.display()
"""



