#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk
from PIL import ImageTk, Image

win = tk.Tk()

c1 = tk.Canvas(win, 
           width=1000, 
           height=200)
coord = 10, 10, 100, 100
arc = c1.create_arc(coord, start=0, extent=350, fill="red")


img =  ImageTk.PhotoImage(file="python.png")
c1.create_image(300,100,image=img)



c1.create_line(500,100,600,10, 
              fill="red", width=3)

c1.create_text(700,50,
              text="PowenKo")

c1.create_rectangle(800,50,900,100,fill="blue")

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   c1.create_oval( x1, y1, x2, y2, fill = python_green )

c1.bind( "<B1-Motion>", paint )


c1.pack()
win.mainloop()





