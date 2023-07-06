'''
綁定鍵盤滑鼠事件 Canvas
'''
from tkinter import * # Import tkinter

class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        title = '綁定鍵盤滑鼠事件 Canvas'
        window.title(title)
        canvas = Canvas(window, bg = 'pink', width = 300, height = 300)
        canvas.pack()
        
        # Bind with <Button-1> event
        canvas.bind("<Button-1>", self.processMouseEvent)
        
        # Bind with <Key> event
        canvas.bind("<Key>", self.processKeyEvent)
        canvas.focus_set()
        
        window.mainloop() # Create an event loop

    def processMouseEvent(self, event):
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked? ", event.num)
    
    def processKeyEvent(self, event):    
        print("keysym? ", event.keysym)
        print("char? ", event.char)
        print("keycode? ", event.keycode)
    
MouseKeyEventDemo() # Create GUI
