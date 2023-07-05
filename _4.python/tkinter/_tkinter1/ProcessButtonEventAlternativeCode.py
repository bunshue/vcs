from tkinter import * # Import tkinter

def processOK():
    print("你按了 OK")

def processCancel():
    print("你按了 Cancel")

window = Tk() # Create a window

btOK = Button(window, text = "OK", fg = "red", command = processOK) 
btOK.pack() # Place the button in the window

btCancel = Button(window, text = "Cancel", bg = "yellow", command = processCancel) 
btCancel.pack() # Place the button in the window

window.mainloop() # Create an event loop
