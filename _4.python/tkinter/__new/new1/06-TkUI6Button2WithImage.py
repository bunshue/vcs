import tkinter as tk
from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

win = tk.Tk()

def event1():
   print("btn1 pressed.")

img = ImageTk.PhotoImage(Image.open(filename))
btn1 =tk.Button(win,text="press me", image=img ,command=event1)
btn1.pack()

win.mainloop()
