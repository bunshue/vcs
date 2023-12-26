# ch31_23.py
import turtle
    
def keyUp():
    t.seth(90)
    t.forward(50)
def keyDn():
    t.seth(270)
    t.forward(50)
    
t = turtle.Pen()
t.screen.onkey(keyUp, 'Up')
t.screen.onkey(keyDn, 'Down')
t.screen.listen()
t.screen.mainloop()



