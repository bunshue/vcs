# ex19_4.py
from tkinter import * 

window = Tk() 
window.title("ex19_4.py") 
        
xWidth = 300
yHeight = 100
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
x = 0
yMsg = 45
canvas.create_text(x, yMsg, text="王者歸來", tags="msg")
        
dx = 5
while True:
    canvas.move("msg", dx, 0)  
    canvas.after(100)       
    canvas.update()         
    if x < xWidth:
        x += dx             
    else:
        x = 0               
        canvas.delete("msg")                             
        canvas.create_text(x, yMsg, text = "王者歸來", tags = "msg")
                
window.mainloop() 


