# ex19_2.py
from tkinter import * 
    
window = Tk()           
window.title("ex19_2")  

xWidth = 400
yHeight = 250
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
for i in range(20):
    canvas.create_oval(10+i*5, 10+i*5, xWidth-10-i*5, yHeight-10-i*5)
        
window.mainloop() 


