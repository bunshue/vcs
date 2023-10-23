#CH11-02 三到八邊形  兩層函式  誇張例子
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
def fun(aug1, aug2):
    for j in range(1, aug1+1):
        t.forward(100);  t.left(aug2)
def fun16(aug1, aug7, aug8, aug9, aug10, aug11, aug12):
    fun(aug1, aug7)
    fun(aug1+1, aug8)
    fun(aug1+2, aug9)
    fun(aug1+3, aug10)
    fun(aug1+4, aug11)
    fun(aug1+5, aug12)
fun16(3, 120.0, 90.0, 72.0, 60.0, 51.43, 45.0)

