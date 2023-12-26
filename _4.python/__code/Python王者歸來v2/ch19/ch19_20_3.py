# ch19_20_3.py
from tkinter import *

def circleIncrease(event):
    global r
    canvas.delete("myCircle")
    if r < 200:
        r += 5
    canvas.create_oval(200-r,200-r,200+r,200+r,fill='yellow',tag="myCircle")
    
def circleDecrease(event):
    global r
    canvas.delete("myCircle")
    if r > 5:
        r -= 5
    canvas.create_oval(200-r,200-r,200+r,200+r,fill='yellow',tag="myCircle")
    
tk = Tk()
canvas= Canvas(tk, width=400, height=400)
canvas.pack()

r = 100
canvas.create_oval(200-r,200-r,200+r,200+r,fill='yellow',tag="myCircle")
canvas.bind('<Button-1>', circleIncrease)
canvas.bind('<Button-3>', circleDecrease)

mainloop()







