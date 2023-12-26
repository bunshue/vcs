# ch31_21.py
import turtle

def printStr(x, y):
    print(x, y)

t = turtle.Pen()
t.screen.onclick(printStr)
t.screen.mainloop()



