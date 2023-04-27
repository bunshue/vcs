from tkinter import * # Import tkinter

filename = 'image/us.gif'

root = Tk() # Create a root window
root.title("Display Image") # Set title

photo = PhotoImage(file = filename)
Label(root, text = "Blue", image = photo, bg = "blue").pack(fill = BOTH, expand = 1)

root.mainloop() # Create an event loop
