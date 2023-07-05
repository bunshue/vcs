import tkinter as tk

SIZE = 8 # The size of the chessboard
queens = [0, 4, 7, 5, 2, 6, 1, 3]

print(queens)

# Display solution in queens
window = tk.Tk()
window.title("Eight Queens")

image = tk.PhotoImage(file = "image/queen.gif")
for i in range(SIZE):
    for j in range(SIZE):
        if queens[i] == j:
            tk.Label(window, image = image).grid(row = i, column = j)
        else:
            tk.Label(window, width = 5, height = 2, bg = "red").grid(row = i, column = j)
        
window.mainloop()

