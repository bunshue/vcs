#CH11-15 三到十邊形  用雙層函式(引數為list[[邊數 角度]]與 [顏色]與 [順序] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0], [9, 40.0], [10, 36.0]]
listC1 = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
listC2 = ['black', 'purple', 'cyan', 'blue', 'green', 'yellow', 'orange', 'red']
listN1 = [3,4,5,6,7,8,9,10]
listN2 = [10,9,8,7,6,5,4,3]
def fun(i, listName, listNameC):
    t.color(listNameC[i-3])
    for j in range(1, listName[i-3][0]+1):
        t.forward(100);  t.left(listName[i-3][1])         
def fun1(listName1, listName2, listName3):
    for i in listName2:
        fun(i, listName1, listName3)
fun1(list1, listN1, listC1)

