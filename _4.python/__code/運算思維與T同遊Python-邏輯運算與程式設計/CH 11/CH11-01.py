#CH11-01 三到八邊形  兩層函式  誇張例子
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
def fun1(aug1, aug2):
    for j in range(1, aug1+1):
        t.forward(100);  t.left(aug2)
def fun66(aug1, aug2, aug3, aug4, aug5, aug6, aug7, aug8, aug9, aug10, aug11, aug12):
    fun1(aug1, aug7)
    fun1(aug2, aug8)
    fun1(aug3, aug9)
    fun1(aug4, aug10)
    fun1(aug5, aug11)
    fun1(aug6, aug12)
fun66(3, 4, 5, 6, 7, 8, 120.0, 90.0, 72.0, 60.0, 51.43, 45.0)
