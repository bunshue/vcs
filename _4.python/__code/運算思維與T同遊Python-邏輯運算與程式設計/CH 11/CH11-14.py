#CH11-14 三到十邊形  用三層函數(參數為list[[邊數 角度]] [顏色] [順序] )  未完全
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0], [9, 40.0], [10, 36.0]]
listC = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
listN = [3,4,5,6,7,8,9,10]
def fun1(i, listName, color):
...
def fun2(i, listName, listNameC):
    color = listNameC[i-3] 
    fun1(i, listName, color)
def fun3(listName1, listName2, listName3):
    for i in listName2:
        fun2(i, listName1, listName3)
fun3(list1, listN, listC)

