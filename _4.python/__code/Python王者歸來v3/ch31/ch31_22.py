# ch31_22.py
import turtle
    
def drawSignal(x, y):
    if x > 0:
        t.fillcolor('yellow')
    else:
        t.fillcolor('blue')
    t.penup()
    t.setpos(x,y-50)            # 設定繪圓起點      
    t.begin_fill()
    t.circle(50)
    t.end_fill()

t = turtle.Pen()
t.screen.onclick(drawSignal)
t.screen.mainloop()



