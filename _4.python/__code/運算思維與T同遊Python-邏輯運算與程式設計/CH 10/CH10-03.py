#CH10-03 三到八邊形   中文函式名稱
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def 畫多邊形(par1, par2):
    for j in range(1, par1+1):
        t.forward(100)
        t.left(par2)
畫多邊形(3, 120.0)
畫多邊形(4, 90.0)
畫多邊形(5, 72.0)
畫多邊形(6, 60.0)
畫多邊形(7, 51.43)
畫多邊形(8, 45.0)

