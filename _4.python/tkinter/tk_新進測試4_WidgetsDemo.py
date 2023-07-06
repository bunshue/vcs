import tkinter as tk

def processCheckbutton():
    print("check button is " + ("checked " if v1.get() == 1 else "unchecked"))

def processRadiobutton():
    print(("Red" if v2.get() == 1 else "Yellow") + " is selected " )

def processButton():
    print("Your name is " + name.get())

window = tk.Tk() # Create a window
window.title("Widgets Demo") # Set a title

# Add a button, a check button, and a radio button to frame1
frame1 = tk.Frame(window) # Create and add a frame to window
frame1.pack()

v1 = tk.IntVar()
cbtBold = tk.Checkbutton(frame1, text = "Bold", variable = v1, command = processCheckbutton) 
v2 = tk.IntVar()
rbRed = tk.Radiobutton(frame1, text = "Red", bg = "red", variable = v2, value = 1, command = processRadiobutton) 
rbYellow = tk.Radiobutton(frame1, text = "Yellow", bg = "yellow", variable = v2, value = 2, command = processRadiobutton) 
cbtBold.grid(row = 1, column = 1)
rbRed.grid(row = 1, column = 2)
rbYellow.grid(row = 1, column = 3)

# Add a button, a check button, and a radio button to frame1
frame2 = tk.Frame(window) # Create and add a frame to window
frame2.pack()

label = tk.Label(frame2, text = "Enter your name: ")
name = tk.StringVar()
entryName = tk.Entry(frame2, textvariable = name) 
btGetName = tk.Button(frame2, text = "Get Name", command = processButton)
message = tk.Message(frame2, text = "It is a widgets demo")
label.grid(row = 1, column = 1)
entryName.grid(row = 1, column = 2)
btGetName.grid(row = 1, column = 3)
message.grid(row = 1, column = 4)

# Add a text
text = tk.Text(window) # Create a text add to the window
text.pack()
text.insert(tk.END, "Tip\nThe best way to learn Tkinter is to read ")
text.insert(tk.END, "these carefully designed examples and use them ")
text.insert(tk.END, "to create your applications.")

window.mainloop()

