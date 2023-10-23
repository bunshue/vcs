#CH11-03 三到八邊形  用函式(無引數)  以外部參數list[[邊數 角度]]代替引數．
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0]]
def fun():
    for i in range(1, 7):
        for j in range(1, list1[i-1][0]+1):
            t.forward(100);  t.left(list1[i-1][1])
fun()

 
