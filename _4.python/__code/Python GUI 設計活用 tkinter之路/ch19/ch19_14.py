# ch19_14.py
from tkinter import *
from PIL import Image, ImageTk

tk = Tk()
img = Image.open("rushmore.jpg")
rushMore = ImageTk.PhotoImage(img)

canvas = Canvas(tk, width=img.size[0]+40,
                height=img.size[1]+30)
canvas.create_image(20,15,anchor=NW,image=rushMore)
canvas.pack(fill=BOTH,expand=True)













