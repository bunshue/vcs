#CH11-13 三到十邊形  用三層函數(參數為list[[邊數 角度]] [顏色] [順序] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0], [9, 40.0], [10, 36.0]]
listC = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
listN = [3,4,5,6,7,8,9,10]
def fun(i, listName):
    for j in range(1, listName[i-3][0]+1):
        t.forward(100);  t.left(listName[i-3][1]) 
def fun1(i, listName, listNameC):
    t.color(listNameC[i-3])
    fun(i, listName)
def fun2(listName1, listName2, listName3):
    for i in listName2:
        fun1(i, listName1, listName3)
fun2(list1, listN, listC)

