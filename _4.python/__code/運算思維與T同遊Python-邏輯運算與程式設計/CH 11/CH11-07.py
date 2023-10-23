#CH11-07 三到八邊形  用函數(參數為list[[邊數 角度]])  錯誤位置
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0]]
list2 = [[6,60.0], [7,51.43], [8,45.0]]
def fun(listName):
    list0 = list1 + list2
    for i in range(1, 7):
        for j in range(1, listName[i-1][0]+1):
            t.forward(100);  t.left(listName[i-1][1])
fun(list0)

 
