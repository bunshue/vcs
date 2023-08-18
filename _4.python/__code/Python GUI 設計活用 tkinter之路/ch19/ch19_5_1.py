# ch19_5_1.py
from tkinter import * 
    
window = Tk()           
window.title("ch19_5_1")  

xWidth = 200
yHeight = 200
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
for i in range(19):
    canvas.create_line(10, 10+10*i, xWidth - 10, 10+10*i)
    canvas.create_line(10+10*i, 10, 10+10*i, yHeight - 10)
        
window.mainloop() 


