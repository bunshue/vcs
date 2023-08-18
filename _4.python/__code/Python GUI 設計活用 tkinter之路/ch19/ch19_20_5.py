# ch19_20_5.py
from tkinter import * 

def up(event):
    global y
    canvas.create_line(x, y, x, y - 5)
    y -= 5       
def down(event):
    global y
    canvas.create_line(x, y, x, y + 5)
    y += 5       
def left(event):
    global x
    canvas.create_line(x, y, x - 5, y)
    x -= 5  
def right(event):
    global x
    canvas.create_line(x, y, x + 5, y)
    x += 5

xWidth = 200
yHeight = 200

window = Tk() 
window.title("ch19_20_5") 

canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()

x = xWidth / 2
y = yHeight / 2
       
canvas.bind("<Up>", up)
canvas.bind("<Down>", down)
canvas.bind("<Left>", left)
canvas.bind("<Right>", right)
canvas.focus_set()
        
window.mainloop() 



