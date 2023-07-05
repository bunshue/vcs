import tkinter as tk
import tkinter.messagebox

# Check if the numbers entered form a valid solution
def validate():
    # Get the numbers from the entries
    values = [[eval(x.get()) 
               for x in cells[i]] for i in range(9)]
    
    if isValid(values):
        tkinter.messagebox.showinfo("Check Sudoku Solution", "The solution is valid")
    else:
        tkinter.messagebox.showwarning("Check Sudoku Solution", "The solution is invalid")
    
window = tk.Tk()
window.title("Pick Four Cards Randomly")

frame1 = tk.Frame(window) # Hold four labels for displaying cards
frame1.pack()

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
text = tk.Text(frame1, wrap = tk.WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

frame2 = tk.Frame(window) # Hold four labels for displaying cards
frame2.pack()

tk.Label(frame2, text = "Enter a filename: ").pack(side = tk.LEFT)
filename = tk.StringVar()
tk.Entry(frame2, width = 40, textvariable = filename).pack(side = tk.LEFT)
tk.Button(frame2, text = "Validate", command = validate).pack()

window.mainloop()
