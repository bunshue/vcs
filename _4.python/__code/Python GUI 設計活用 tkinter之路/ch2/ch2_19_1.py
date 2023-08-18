# ch2_19_1.py
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch2_19_1")
root.geometry("680x400")

image = Image.open("yellowstone.jpg")
yellowstone = ImageTk.PhotoImage(image)
label = Label(root,image=yellowstone)
label.pack()

root.mainloop()




