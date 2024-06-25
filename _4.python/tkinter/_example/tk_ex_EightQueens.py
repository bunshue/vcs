import tkinter as tk

SIZE = 8 # The size of the chessboard


# Search for a solution starting from a specified row 
def search(row):
    if row == SIZE: # Stopping condition
        return True # A solution found to place 8 queens 

    for column in range(SIZE):
        queens[row] = column # Place it at (row, column)
        if isValid(row, column) and search(row + 1):
            return True # Found and exit for loop   
          
    # No solution for a queen placed at any column of this row
    return False

# Check if a queen can be placed at row i and column j 
def isValid(row, column):
    for i in range(1, row + 1):
        if (queens[row - i] == column # Check column
            or queens[row - i] == column - i 
            or queens[row - i] == column + i): 
            return False # There is a conflict
    return True # No conflict


queens = SIZE * [-1] # Queen positions 
search(0) # Search for a solution from row 0

window = tk.Tk()
window.title("Eight Queens") # Set a title

image = tk.PhotoImage(file = "data/queen.gif")
for i in range(SIZE):
    for j in range(SIZE):
        if queens[i] == j:
            tk.Label(window, image = image).grid(
                row = i, column = j)
        else:
            tk.Label(window, width = 5, height = 2, 
                bg = "red").grid(row = i, column = j)

window.mainloop()

