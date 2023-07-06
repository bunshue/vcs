#右鍵選單

import tkinter as tk
    
class PopupMenuDemo:
    def __init__(self):
        window = tk.Tk()
        window.title("Popup Menu Demo")

        #右鍵選單
        self.menu = tk.Menu(window, tearoff = 0)
        self.menu.add_command(label = "Draw a line", command = self.displayLine)
        self.menu.add_command(label = "Draw an oval", command = self.displayOval)
        self.menu.add_command(label = "Draw a rectangle", command = self.displayRect)
        self.menu.add_command(label = "Clear", command = self.clearCanvas)
        
        # Place canvas in window
        self.canvas = tk.Canvas(window, width = 200, height = 100, bg = 'white')
        self.canvas.pack()
        
        # Bind popup to canvas
        self.canvas.bind("<Button-3>", self.popup)
        
        window.mainloop()
        
    # Display a rectangle
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
        
    # Display an oval
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags = "oval")
    
    # Display a line
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, tags = "line")
        self.canvas.create_line(10, 90, 190, 10, tags = "line")
    
    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "line")

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)
    
PopupMenuDemo() # Create GUI
