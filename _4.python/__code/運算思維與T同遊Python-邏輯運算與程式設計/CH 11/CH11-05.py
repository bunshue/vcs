#CH11-05 三到八邊形  用函數(參數為list[[邊數 角度]] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0]]
list2 = [[6,60.0], [7,51.43], [8,45.0]]
def fun(listNameA, listNameB):
    for i in range(1, 4):
        for j in range(1, listNameA[i-1][0]+1):
            t.forward(100);  t.left(listNameA[i-1][1])
    for i in range(1, 4):
        for j in range(1, listNameB[i-1][0]+1):
            t.forward(100);  t.left(listNameB[i-1][1])
fun(list1, list2)
