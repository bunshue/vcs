import tkinter as tk

SIZE = 8 # The size of the chessboard
class EightQueens:
    def __init__(self):
        self.queens = SIZE * [-1] # Queen positions 
        self.search(0) # Search for a solution from row 0

        # Display solution in queens
        window = tk.Tk()
        window.title("Eight Queens")
        
        image = tk.PhotoImage(file = "image/queen.gif")
        for i in range(SIZE):
            for j in range(SIZE):
                if self.queens[i] == j:
                    tk.Label(window, image = image).grid(row = i, column = j)
                else:
                    tk.Label(window, width = 5, height = 2, bg = "red").grid(row = i, column = j)
                
        window.mainloop()
           
    # Search for a solution starting from a specified row 
    def search(self, row):
        if row == SIZE: # Stopping condition
            return True # A solution found to place 8 queens 
    
        for column in range(SIZE):
            self.queens[row] = column # Place it at (row, column)
            if self.isValid(row, column) and self.search(row + 1):
                return True # Found and exit for loop   
          
        # No solution for a queen placed at any column of this row
        return False

    # Check if a queen can be placed at row i and column j 
    def isValid(self, row, column):
        for i in range(1, row + 1):
            if (self.queens[row - i] == column # Check column
                or self.queens[row - i] == column - i 
                or self.queens[row - i] == column + i): 
                return False # There is a conflict
        return True # No conflict
    
EightQueens() # Create GUI
