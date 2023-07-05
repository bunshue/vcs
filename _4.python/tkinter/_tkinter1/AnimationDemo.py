from tkinter import * # Import tkinter

class AnimationDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Animation Demo") # Set a title
        
        #class 內的變數
        self.width = 250 # Width of the self.canvas
        self.canvas = Canvas(window, bg = "white", width = self.width, height = 50)
        self.canvas.pack()
        
        self.x = 0 # Starting x position
        self.canvas.create_text(self.x, 30, text = "Message moving?", tags = "text")
        
        self.dx = 3
        while True:
            self.canvas.move("text", self.dx, 0) # Move text dx unit
            self.canvas.after(100) # Sleep for 100 milliseconds
            self.canvas.update() # Update canvas
            if self.x < self.width:
                self.x += self.dx  # Get the current position for string
            else:
                self.x = 0 # Reset string position to the beginning
                self.canvas.delete("text") 
                # Redraw text at the beginning
                self.canvas.create_text(self.x, 30, text = "Message moving?", tags = "text")
                
        window.mainloop()

AnimationDemo() # Create GUI
