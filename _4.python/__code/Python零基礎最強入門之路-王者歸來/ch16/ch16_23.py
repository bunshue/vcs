# ch16_23.py
import turtle,time

t = turtle.Pen()
width = t.screen.window_width()
height = t.screen.window_height()
print("視窗width  = ", width)
print("視窗height = ", height)
time.sleep(3)
t.screen.setup(600, 480)            # 更改視窗寬和高
width = t.screen.window_width()
height = t.screen.window_height()
print("新視窗width  = ", width)
print("新視窗height = ", height)



