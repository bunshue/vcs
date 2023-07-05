from tkinter import * # Import tkinter
from ImageViewer import ImageViewer

class ImageViewer:
    def __init__(self, container, imagefile, x, y, width, height):
        caImage = PhotoImage(file = imagefile)
        
        canvas = Canvas(container, width = width, height = height)
        canvas.pack()
        canvas.create_image(x, y, image = caImage)

window = Tk() # Create a window
window.title("Six Flags") # Set title

imageViewer = ImageViewer(window, "image/ca.gif", 90, 50, 400, 200) # Create a clock

window.mainloop() # Create an event loop
