from tkinter import * # Import tkinter

def processOK():
    print("OK button is clicked")
 
def processCancel():
    print("Cancel button is clicked")
    
root = Tk() # Create a root window
btOK = Button(root, text = "OK", fg = "red", command = processOK) 
btOK.pack() # Place the button in the window
btCancel = Button(root, text = "Cancel", bg = "yellow", command = processCancel) 
btCancel.pack() # Place the button in the window

root.mainloop()
