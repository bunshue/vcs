#CH11-11 三到十邊形  用雙層函數(參數為list[[邊數 角度 顏色]]與 [順序] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0,'red'], [4,90.0,'orange'], [5,72.0,'yellow'], [6,60.0,'green'], [7,51.43,'blue'], [8,45.0,'cyan'], [9, 40.0,'purple'], [10, 36.0,'black']]
listN1 = [3,4,5,6,7,8,9,10]
listN2 = [10,9,8,7,6,5,4,3]
def fun(i, listName):
    t.color(listName[i-3][2])
    for j in range(1, listName[i-3][0]+1):
        t.forward(100);  t.left(listName[i-3][1])         
def fun1(listName1, listName2):
    for i in listName2:
        fun(i, listName1)
fun1(list1, listN2)
 
