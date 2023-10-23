#CH11-09 三到十邊形  用雙層函數(參數為list[[邊數 角度 顏色]] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0,'red'], [4,90.0,'orange'], [5,72.0,'yellow'], [6,60.0,'green'], [7,51.43,'blue'], [8,45.0,'cyan'], [9, 40.0,'purple'], [10, 36.0,'black']]
def fun(i, listName):
    t.color(listName[i-1][2])
    for j in range(1, listName[i-1][0]+1):
        t.forward(100);  t.left(listName[i-1][1])
def fun1(n, listName):
    for i in range(1, n+1):
        fun(i, listName)
fun1(8, list1)
 
