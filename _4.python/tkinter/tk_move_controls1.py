import tkinter as tk

window = tk.Tk() # Create a window
window.title("Animation Demo") # Set a title

#公用變數
width = 250 # Width of the canvas
canvas = tk.Canvas(window, bg = "white", width = width, height = 50)
canvas.pack()

x = 0 # Starting x position
sleepTime = 100 # Set a sleep time 
canvas.create_text(x, 30, text = "Message moving?", tags = "text")

dx = 3

while True:
    canvas.move("text", dx, 0) # Move text dx unit
    canvas.after(sleepTime) # Sleep for 100 milliseconds
    canvas.update() # Update canvas
    if x < width:
        x += dx  # Set new position 
    else:
        x = 0 # Reset string position to the beginning
        canvas.delete("text") 
        # Redraw text at the beginning
        canvas.create_text(x, 30, text = "Message moving?", tags = "text")

window.mainloop()
