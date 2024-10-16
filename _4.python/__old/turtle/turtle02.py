"""
運算思維與T同遊Python-邏輯運算與程式設計

"""

print("------------------------------------------------------------")  # 60個

#CH01_06
import turtle
t = turtle.Pen()
t.speed(1)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)



#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-01.py

#CH01-01
import turtle
t = turtle.Pen()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-02.py

#CH01-02
import turtle
t = turtle.Pen()
t.forward(100)
#t.left(90)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-03.py

#CH01-03   陳一斌改寫（一）
import turtle
t = turtle.Pen()
t.forward(100)
t.left(90)

#t.forward(100); t.left(90)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-04.py

#CH01-04   陳一斌改寫（二）
import turtle
t = turtle.Pen()
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-05.py

#CH01-05   Created: 2020/1/1
import turtle
t = turtle.Pen()
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-06.py

#CH01-06   錯的六邊形，Modified: 2020/12/31
import turtle
t = turtle.Pen()
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-07.py

#CH01-07  Version: 1.01  六邊形
import turtle
t = turtle.Pen()
t.forward(100); t.left(60)
t.forward(100); t.left(60)
t.forward(100); t.left(60)
t.forward(100); t.left(60)
t.forward(100); t.left(60)
t.forward(100); t.left(60)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-08.py

#CH01-08  六邊形
# 引入變數
import turtle
t = turtle.Pen()
a = 60
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-09.py

#CH01-09  八邊形
import turtle
t = turtle.Pen()
a = 45
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 01\CH01-10.py

#CH01-10  四六八邊形 三程式合併（一次只能執行其中之一） 
import turtle
t = turtle.Pen()
a=90   #四=90度, 六=60度, 八=45度,
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
t.forward(100); t.left(a)
#t.forward(100); t.left(a)
#t.forward(100); t.left(a)
#t.forward(100); t.left(a)
#t.forward(100); t.left(a)

print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-01.py

#CH02-01  迴圈   四邊形
import turtle
t = turtle.Pen()
a=90   #四=90度, 六=60度, 八=45度,
for i in range(1,5):
    t.forward(100); t.left(a)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-02.py

# CH02-02  指令：迴圈
i = 7
print(i)
for i in [1, 2, 3, 4]:
print(i)
for i in range(1,5):
print(i)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-03.py

# CH02-02  指令：迴圈
i = 7
print(i)
for i in [1, 2, 3, 4]:
    print(i)
for i in range(1,5):
    print(i)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-04.py

# CH02-04  指令：迴圈
for i in [1, 2, 3, 4]:
    print(i)
for i in range(1,5):
    print(i)
    print('+')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-05.py

#CH02-05  指令：迴圈
for i in [1, 2, 3, 4]:
    print(i)
for i in range(1,5):
    print(i)
print('+')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-06.py

#CH02-06  指令：迴圈
for i in [1, 2, 3, 4]:
    print(i)
print('+')
for i in range(1,5):
    print(i)
print('+')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-07.py

#CH02-07  迴圈   四六八邊形
import turtle
t = turtle.Pen()
a=90   #四邊形
for i in range(1,5):
    t.forward(100); t.left(a)
a=60   #六邊形
for i in range(1,7):
    t.forward(100); t.left(a)
a=45   #八邊形
for i in range(1,9):
    t.forward(100); t.left(a)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-08.py

#CH02-08   more level
import turtle
t = turtle.Pen()
t.speed(5)
for sides in range(3,9):
    ang = 360/sides
    for i in range(1,sides+1): t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-09.py

#CH02-09   三層for迴圈  往右三個
import turtle
t = turtle.Pen()
t.speed(0)
for j in range(1,4):   #做3次
    for sides in range(3,5):   #做2次
        ang=360/sides   
        for i in range(1,sides+1): t.forward(100); t.left(ang)
    t.forward(100)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-10.py

#CH02-10   三層for迴圈  部分重疊
import turtle
t = turtle.Pen()
t.speed(0)
for j in range(1,4):   #做三次
    for sides in range(3,6):   #做三次
        ang=360/sides   
        for i in range(1,sides+1): t.forward(100); t.left(ang)
    t.forward(100)







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-11.py

#CH02-11  三層for迴圈  3~8
import turtle
t = turtle.Pen()
t.speed(0)
for j in range(1,3):
    for sides in range(3,9):
        ang=360/sides   
        for i in range(1,sides+1): t.forward(50); t.left(ang)
    t.forward(120.72)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-12.py

#CH02-12  四層for迴圈（一）  3~8
import turtle
t = turtle.Pen()
t.speed(0)
for k in range(1,2):
    for j in range(1,3):
        for sides in range(3,9):
            ang=360/sides   
            for i in range(1,sides+1): t.forward(50); t.left(ang)
        t.forward(120.72)
    t.left(180)
    t.forward(2*120.72)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-13.py

#CH02-13  四層for迴圈（二）
import turtle
t = turtle.Pen()
t.speed(0)
for k in range(1,3):
    for j in range(1,3):
        for sides in range(3,9):
            ang=360/sides   
            for i in range(1,sides+1): t.forward(50); t.left(ang)
        t.forward(120.72)
    t.left(180)
    t.forward(2*120.72)
    t.left(270)
    t.forward(120.72)
    t.left(270)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-14.py

#CH02-14 四層for迴圈（三）
import turtle
t = turtle.Pen()
t.speed(0)
for k in range(1,3):
    for j in range(1,3):
        for sides in range(3,9):
            ang=360/sides 
            for i in range(1,sides+1): t.forward(50); t.left(ang)
        t.penup()
        t.forward(120.72)
        t.pendown()
    t.penup()
    t.left(180)
    t.forward(2*120.72)
    t.left(270)
    t.forward(120.72)
    t.left(270)
    t.pendown()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-15.py

#CH02-15  四層for迴圈（四）   復原
import turtle
t = turtle.Pen()
t.speed(0)
for k in range(1,3):
    for j in range(1,3):
        for sides in range(3,9):
            ang=360/sides 
            for i in range(1,sides+1): t.forward(50); t.left(ang)
        t.penup()
        t.forward(120.72)
        t.pendown()
    t.penup()
    t.left(180)
    t.forward(2*120.72)
    t.left(270)
    t.forward(120.72)
    t.left(270)
    t.pendown()
t.penup()
t.left(270)
t.forward(2*120.72)
t.left(90)
t.pendown()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 02\CH02-16.py

#CH02-16   demo 
import turtle
t = turtle.Pen()
t.speed(0)
for k in range(1,3):
    for j in range(1,3):
        for sides in range(3,9):
            ang = 360/sides
            for i in range(1,sides+1): t.forward(50); t.left(ang)
        t.penup(); t.forward(120.72); t.pendown()
    t.penup(); t.left(180); t.forward(2*120.72); t.left(270); t.forward(120.72); t.left(270); t.pendown()
t.penup(); t.left(270); t.forward(2*120.72); t.left(90); t.pendown()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-01.py

#CH03-01   四邊形 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(0)
sides = 4
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100); t.left(90)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-02.py

#CH03-02  長度連續變大 三邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(0)
for j in range(1,11):
    t.forward(10+j*20);  t.left(120)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-03.py

#CH03-03  連續變大&線變寬三邊形 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 1
for j in range(1,11):
    t.width(tWidth)
    tWidth += 1
    t.forward(10+j*20);  t.left(120)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-04.py

#CH03-04   固定寬度   三四五邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
for j in range(1,7):
    t.forward(10+j*20);  t.left(120)
for j in range(1,9):
    t.forward(130+j*10);  t.left(90)
for j in range(1,11):
    t.forward(210+j*6);  t.left(72)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-05.py

#CH03-05   多邊形不同的固定寬度   三四五邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 1
t.width(tWidth)
tWidth += 3
for j in range(1,7):
    t.forward(10+j*20);  t.left(120)
t.width(tWidth)
tWidth += 3
for j in range(1,9):
    t.forward(130+j*10);  t.left(90)
t.width(tWidth)
tWidth += 3
for j in range(1,11):
    t.forward(210+j*6);  t.left(72)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-06.py

#CH03-06  線連續變寬   三四五邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 1
for j in range(1,7):
    t.width(tWidth)
    tWidth += 3
    t.forward(10+j*20);  t.left(120)
for j in range(1,9):
    t.width(tWidth)
    tWidth += 3
    t.forward(130+j*10);  t.left(90)
for j in range(1,11):
    t.width(tWidth)
    tWidth += 3
    t.forward(210+j*6);  t.left(72)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-07.py

#CH03-07  連續變大&線變窄三邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
for j in range(1,11):
    t.width(tWidth)
    tWidth -= 1
    t.forward(10+j*20);  t.left(120)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-08.py

#CH03-08  連續變大&線變窄三邊形   不完善
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
for j in range(1,11):
    t.width(tWidth)
    tWidth -= 1.5
    t.forward(10+j*20);  t.left(120)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-09.py

#CH03-09  指令：if
for i in [1, 2, 3, 4]:
    #if (i > 1):
    print(i)
print('+')
for i in range(1,5):
    print(i)
print('+')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-10.py

#CH03-10  指令：if
for i in [1, 2, 3, 4]:
    if (i > 1):
        print(i)
print('+')
for i in range(1,5):
    if (i > 2):
        print(i)
print('+')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-11.py

#CH03-11  連續變大&線變窄三邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
for j in range(1,11):
    t.width(tWidth)
    tWidth -= 1.5
    if (tWidth > 0):
        t.forward(10+j*20);  t.left(120)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-12.py

#CH03-12  連續變大&線變窄三邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
for j in range(1,11):
    t.width(tWidth)
    tWidth -= 1.5
    if (tWidth < 0): break
    else: t.forward(10+j*20);  t.left(120)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-13.py

#CH03-13  指令：while迴圈
i = 2
while (i in [1, 2, 3, 4]):
    print(i)
    i += 1
print('+')
i = 3
while (i in range(1,5)):
    print(i)
    i += 1
print('+')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-14.py

#CH03-14  連續變大&線變窄三邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
j = 1
while ((1<=j) and (j<=10)):
    j += 1
    t.width(tWidth)
    tWidth -= 1.5
    if (tWidth >= 0):
        t.forward(10+j*20);  t.left(120)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-15.py

#CH03-15  連續變大&線變窄三邊形  需小修正
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
j = 1
while ((1<=j) and (j<=10) and (tWidth >= 0)):
    j += 1
    t.width(tWidth)
    tWidth -= 1.5
    #if (tWidth >= 0):
    t.forward(10+j*20);  t.left(120)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 03\CH03-16.py

#CH03-16  連續變大&線變窄三邊形  更正
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
j = 1
while ((1<=j) and (j<=10) and (tWidth >= 1.5)):
    j += 1
    t.width(tWidth)
    tWidth -= 1.5
    t.forward(10+j*20);  t.left(120)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-01.py

#CH04-01
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
t.color('red')
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-02.py

#CH04-02
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
t.color('red')
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    t.color('green')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-03.py

#CH04-03    用toggle
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
toggle = True
t.color('red')
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (toggle == True):
        t.color('green')
        toggle = False
    else:
        t.color('red')
        toggle = True

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-04.py

#CH04-04    用toggle
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
toggle = True
for sides in range(3,9):
    ang = 360/sides   
    if (toggle == True):
        t.color('red')
        toggle = False
    else:
        t.color('green')
        toggle = True
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-05.py

#CH04-05    用code
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 1
t.color('red')
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 1):
        code = 2
        t.color('green')
    else:
        code = 1
        t.color('red')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-06.py

#CH04-06    用code
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 'red'
t.color(code)
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 'red'):
        code = 'green'
    else:
        code = 'red'
    t.color(code)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-07.py

#CH04-07    用code RGB
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 'red'
t.color(code)
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 'red'): code = 'green'
    else:
        if (code == 'green'): code = 'blue'
        else: code = 'red'
    t.color(code)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-08.py

#CH04-08    用code RGB   錯
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 'red'
t.color(code)
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 'red'): code = 'green'
    if (code == 'green'): code = 'blue'
    if (code == 'blue'): code = 'red'
    t.color(code)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-09.py

#CH04-09    用code RGB   錯
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 'red'
t.color(code)
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 'blue'): code = 'red'    
    if (code == 'green'): code = 'blue'
    if (code == 'red'): code = 'green'
    t.color(code)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-10.py

#CH04-10    用code RGB   OK
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 'red'
t.color(code)
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 'red'): code = 'green'
    elif (code == 'green'): code = 'blue'
    elif (code == 'blue'): code = 'red'
    else: code = 'error'
    t.color(code)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 04\CH04-11.py

#CH04-11    用code RGB   OK
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 'red'
t.color(code)
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 'red'): code = 'green'
    else:
        if (code == 'green'): code = 'blue'
        else:
            if (code == 'blue'): code = 'red'
            else: code = 'error'
    t.color(code)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-01.py

#CH05-01  指令：list
for i in range(1, 4):
    print(i)
print('+')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-02.py

#CH05-02  指令：list   錯
for i in range('red', 'green'):
    print(i)
print('+')




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-03.py

#CH05-03  指令：list
for i in ['red', 'green', 'blue']:
    print(i)
print('+')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-04.py

#CH05-04  指令：list   仍有錯
colors3List = ['red', 'green', 'blue']
for i in range(1, 4):
    print(colors3List[i])
print('+')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-05.py

#CH05-05  指令：list  驗證為何錯
colors3List = ['red', 'green', 'blue']
print(colors3List[1])
print(colors3List[2])
print(colors3List[3])
print('+')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-06.py

#CH05-06  指令：list  驗證錯處
colors3List = ['red', 'green', 'blue']
print(colors3List[0])
print(colors3List[1])
print(colors3List[2])
print(colors3List[3])
print('+')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-07.py

#CH05-07   RGB  錯
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue']
colorsIndex = 0
sides = 3
ang = 360/sides
t.color(colors3List[colorsIndex])
colorsIndex += 1
for i in range(1,sides+1):
    t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-08.py

#CH05-08    RGB
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue']
colorsIndex = 0
sides = 3
ang = 360/sides
for i in range(1,sides+1):
    t.color(colors3List[colorsIndex])
    colorsIndex += 1
    t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-09.py

#CH05-09   四邊形   有錯
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue']
colorsIndex = 0
sides = 4
ang = 360/sides
for i in range(1,sides+1):
    t.color(colors3List[colorsIndex])
    colorsIndex += 1
    t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-10.py

#CH05-10    RGBGr
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue', 'gray']
colorsIndex = 0
sides = 4
ang = 360/sides
for i in range(1,sides+1):
    t.color(colors3List[colorsIndex])
    colorsIndex += 1
    t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-11.py

#CH05-11    %
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue']
colorsIndex = 0
sides = 5
ang = 360/sides
for i in range(1,sides+1):
    t.color(colors3List[colorsIndex % 3])
    colorsIndex += 1
    t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-12.py

#CH05-12    讓每個多邊形各有其不同顏色
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
colorsIndex = 0
for sides in range(3,9):
    ang = 360/sides   
    t.color(colorsList[colorsIndex % 8])
    colorsIndex += 1
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 05\CH05-13.py

#CH05-13　　讓每個多邊形各有其不同顏色
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
for sides in range(3,9):
    ang = 360/sides   
    t.color(colorsList[(sides-3) % 8])
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 06\CH06-01.py

#CH06-01   線條不同顏色。多邊形重新開始 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
for sides in range(3,9):
    ang = 360/sides
    t.color(colorsList[(sides-3) % 8])
    for i in range(1,sides+1):
        t.color(colorsList[(i-1)%8])
        t.forward(100); t.left(ang)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 06\CH06-02.py

#CH06-02   線條不同顏色。接續原來的順序
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
colorInd=0
for sides in range(3,9):
    ang = 360/sides
    for i in range(1,sides+1):
        t.color(colorsList[colorInd])
        t.forward(100); t.left(ang)
        colorInd = (colorInd+1)%8

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 06\CH06-03.py

#CH06-03    線條不同顏色。多邊形不同的重新開始
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
for sides in range(3,9):
    ang = 360/sides
    colorInd = sides-3
    for i in range(1, sides+1):
        t.color(colorsList[colorInd])
        colorInd = (colorInd+1)%8
        t.forward(100); t.left(ang) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-01.py

#CH07-01   五邊形    
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides  = 5
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100)
    t.left(ang)
t.hideturtle()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-02.py

#CH07-02   五邊形內縮為10
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides  = 5
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100)
    t.left(180)
    t.forward(90)
    t.left(180)
    t.left(ang)
t.hideturtle()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-03.py

#CH07-03   五邊形內縮為1 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides  = 5
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100)
    t.left(180)
    t.forward(99)
    t.left(180)
    t.left(ang)
t.hideturtle()






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-04.py

#CH07-04   五邊形內縮為0 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides  = 5
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.left(180)
    t.left(ang)
t.hideturtle()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-05.py

#CH07-05   七邊形的示範 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides  = 7
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100)
    t.left(180)
    t.forward(90)
    t.left(180)
    t.left(ang)
t.hideturtle()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-06.py

#CH07-06: try-and-error 五邊形   方法一
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5);
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(65)   #手調
t.hideturtle()
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-07.py

#CH07-07: try-and-error 五邊形   方法一
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5);
sides = 5
for ang in [65,70,75,80,85]:
    for j in range(1, sides+1):
        t.forward(100); t.left(ang)
    t.penup()
    t.home()
    t.pendown()
t.hideturtle()
  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-08.py

#CH07-08: try-and-error 五邊形 color   方法一
import turtle
t = turtle.Pen(); 
t.shape('turtle'); t.width(2); t.speed(5)
sides = 5
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
colorInd = 0
for ang in [65,70,75,80,85]:
    t.color(colorsList[(colorInd)%5]); colorInd += 1
    for j in range(1, sides+1):
        t.forward(100); t.left(ang)
    t.penup()
    t.home()
    t.pendown()
t.hideturtle()
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-09.py

#CH07-09: try-and-error 五邊形 color   方法一
import turtle
t = turtle.Pen(); 
t.shape('turtle'); t.width(2); t.speed(5)
sides = 5
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
colorInd = 0
for ang in [71,72,73,74]:
    t.color(colorsList[(colorInd)%4]); colorInd += 1
    for j in range(1, sides+1):
        t.forward(100); t.left(ang)
    t.penup()
    t.home()
    t.pendown()
t.hideturtle()
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-10.py

#CH07-10: try-and-error 五邊形   方法二a
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides = 5
for j in range(1,sides+1):
    t.forward(100); t.left(75)   #手調
t.hideturtle()
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 07\CH07-11.py

#CH07-10: TAE 五邊 累積位置值   方法二a
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
SL = 100; ang = 75    #手調
accumAng = 0; accumPX = 0; accumPY = 0
print(accumAng, accumPX, accumPY)
for sides in range(5,6):
    for j in range(1, sides+1):
        t.forward(100); t.left(ang)
        accumPX += SL *np.cos(accumAng*np.pi/180) 
        accumPY += SL *np.sin(accumAng*np.pi/180)
        accumAng += ang
        print(accumAng, accumPX, accumPY)
t.hideturtle()
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 08\CH08-01.py

#CH08-01    不同三角形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(5); t.speed(5)

for i in range(1,4):
    t.forward(+100); t.left(+120)

'''
for i in range(1,4):
    t.forward(+100); t.right(+120)
'''
'''
for i in range(1,4):
    t.backward(+100); t.left(+120)
'''
'''
for i in range(1,4):
    t.backward(+100); t.right(+120)
'''

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 08\CH08-02.py

#CH08-02    變數
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(5); t.speed(5)
dist = +100
ang = +120
for i in range(1,4): t.forward(dist); t.left(ang)
#for i in range(1,4): t.forward(dist); t.right(ang)
#for i in range(1,4): t.backward(dist); t.left(ang)
#for i in range(1,4): t.backward(dist); t.right(ang)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 08\CH08-03.py

#CH08-03     變數
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(5); t.speed(5)
dist = +100
ang = +120
for i in range(1,4):
    t.forward(dist); t.left(ang)
    #t.forward(dist); t.right(ang)
    #t.backward(dist); t.left(ang)
    #t.backward(dist); t.right(ang)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 09\CH09-01.py

#CH09-01 三到八邊形  用list[角度]  雙層迴圈
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5);
list1 = [120.0, 90.0, 72.0, 60.0, 51.43, 45.0]
for i in range(3,9):
    for j in range(1,i+1):
        t.forward(100) ;  t.left(list1[i-3])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 09\CH09-02.py

#CH09-02 三到八邊形  用二list[邊數] [角度]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [3, 4, 5, 6, 7, 8]
list2 = [120.0, 90.0, 72.0, 60.0, 51.43, 45.0]
for i in range(1, 7):
    for j in range(1, list1[i-1]+1):
        t.forward(100);  t.left(list2[i-1])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 09\CH09-03.py

#CH09-03 三到八邊形  用三list: [邊數] [角度] [筆畫色]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [3, 4, 5, 6, 7, 8]
list2 = [120.0, 90.0, 72.0, 60.0, 51.43, 45.0]
list3 = ['red', 'orange','yellow','green','blue', 'cyan']
for i in range(1, 7):
    t.color(list3[i-1])
    for j in range(1, list1[i-1]+1):
        t.forward(100)
        t.left(list2[i-1])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 09\CH09-04.py

#CH09-04 三到八邊形  用list: [[邊數 角度]]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0]]
for i in range(1, 7):
    for j in range(1, list1[i-1][0]+1):
        t.forward(100)
        t.left(list1[i-1][1])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 09\CH09-05.py

#CH09-05 三到八邊形  用兩list[[邊數 角度]] [筆畫色] 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0]]
list2 = ['red','orange','yellow','green','blue','cyan']
for i in range(1, 7):
    t.color(list2[i-1])
    for j in range(1, list1[i-1][0]+1):
        t.forward(100);  t.left(list1[i-1][1])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 09\CH09-06.py

#CH09_06 三到八邊形  用list[[邊數 角度 筆畫色]]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [[3,120.0,'red'], [4,90.0,'orange'], [5,72.0,'yellow'], [6,60.0,'green'], [7,51.43,'blue'], [8,45.0,'cyan']]
for i in range(1, 7):
    t.color(list1[i-1][2])
    for j in range(1, list1[i-1][0]+1):
        t.forward(100);  t.left(list1[i-1][1])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 10\CH10-01.py

#CH10-01 三到八邊形 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
for j in range(1, 3+1):
    t.forward(100);  t.left(120.0)
for j in range(1, 4+1):
    t.forward(100);  t.left(90.0)
for j in range(1, 5+1):
    t.forward(100);  t.left(72.0)
for j in range(1, 6+1):
    t.forward(100);  t.left(60.0)
for j in range(1, 7+1):
    t.forward(100);  t.left(51.43)
for j in range(1, 8+1):
    t.forward(100);  t.left(45.0)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 10\CH10-02.py

#CH10-02 三到八邊形 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def fun(aug1, aug2):
    for j in range(1, aug1+1):
        t.forward(100);  t.left(aug2)
fun(3, 120.0)
for j in range(1, 4+1):
    t.forward(100);  t.left(90.0)
for j in range(1, 5+1):
    t.forward(100);  t.left(72.0)
for j in range(1, 6+1):
    t.forward(100);  t.left(60.0)
for j in range(1, 7+1):
    t.forward(100);  t.left(51.43)
for j in range(1, 8+1):
    t.forward(100);  t.left(45.0)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 10\CH10-03.py

#CH10-03 三到八邊形   中文函式名稱
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def 畫多邊形(par1, par2):
    for j in range(1, par1+1):
        t.forward(100)
        t.left(par2)
畫多邊形(3, 120.0)
畫多邊形(4, 90.0)
畫多邊形(5, 72.0)
畫多邊形(6, 60.0)
畫多邊形(7, 51.43)
畫多邊形(8, 45.0)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 10\CH10-04.py

#CH10-04 三到八邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def funDraw(sides, ang):
    for j in range(1, sides+1):
        t.forward(100);  t.left(ang)
funDraw(3, 120.0)
funDraw(4, 90.0)
funDraw(5, 72.0)
funDraw(6, 60.0)
funDraw(7, 51.43)
funDraw(8, 45.0)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 10\CH10-05.py

#CH10-05 三到八邊形   顏色
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def funExt(sides, ang, color):
    t.color(color)
    for j in range(1, sides+1):
        t.forward(100);  t.left(ang)
funExt(3, 120.0, 'red')
funExt(4, 90.0, 'orange')
funExt(5, 72.0, 'yellow')
funExt(6, 60.0, 'green')
funExt(7, 51.43, 'blue')
funExt(8, 45.0, 'cyan')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-01.py

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

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-02.py

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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-03.py

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

 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-04.py

#CH11-04 三到八邊形  用函數(參數為list1[[邊數 角度]] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0]]
list2 = [[6,60.0], [7,51.43], [8,45.0]]
def fun(listName):
    for i in range(1, 4):
        for j in range(1, listName[i-1][0]+1):
            t.forward(100);  t.left(listName[i-1][1])
fun(list1)
fun(list2)
 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-05.py

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

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-06.py

#CH11-06 三到八邊形  用函數(參數為list[[邊數 角度]] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0]]
list2 = [[6,60.0], [7,51.43], [8,45.0]]
list0 = list1 + list2
def fun(listName):
    for i in range(1, 7):
        for j in range(1, listName[i-1][0]+1):
            t.forward(100);  t.left(listName[i-1][1])
fun(list0)

 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-07.py

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

 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-08.py

#CH11-08 三到十邊形  用函式(引數為list[[邊數 角度 顏色]] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0,'red'], [4,90.0,'orange'], [5,72.0,'yellow'], [6,60.0,'green'], [7,51.43,'blue'], [8,45.0,'cyan'], [9, 40.0,'purple'], [10, 36.0,'black']]
def fun(listName):
    for i in range(1, 9):
        t.color(listName[i-1][2])
        for j in range(1, listName[i-1][0]+1):
            t.forward(100);  t.left(listName[i-1][1])
fun(list1)

 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-09.py

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
 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-10.py

#CH11-10 三到八邊形  可指定是要畫第幾個到第幾個多邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0,'red'], [4,90.0,'orange'], [5,72.0,'yellow'], [6,60.0,'green'], [7,51.43,'blue'], [8,45.0,'cyan'], [9, 40.0,'purple'], [10, 36.0,'black']]
def fun(i, listName):
    t.color(listName[i-1][2])
    for j in range(1, listName[i-1][0]+1):
        t.forward(100);  t.left(listName[i-1][1])         
def fun1(n1, n2, listName):
    for i in range(n1, n2+1):
        fun(i, listName)
fun1(1, 8, list1)
 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-11.py

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
 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-12.py

#CH11-12 三到十邊形  用雙層函式(引數為list[[邊數 角度]]與 [顏色]與 [順序] )
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0], [9, 40.0], [10, 36.0]]
listC = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
listN = [3,4,5,6,7,8,9,10]
def fun(i, listName, listNameC):
    t.color(listNameC[i-3])
    for j in range(1, listName[i-3][0]+1):
        t.forward(100);  t.left(listName[i-3][1])         
def fun1(listName1, listName2, listName3):
    for i in listName2:
        fun(i, listName1, listName3)
fun1(list1, listN, listC)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-13.py

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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-14.py

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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 11\CH11-15.py

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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-01.py

#CH12-01:   原點圓心  逆時針 五邊形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
t.up(); t.goto(0.0, -85.08); t.down()
t.circle(85.08)
t.up(); t.goto(-50.0, -68.82); t.down() #p0
t.goto(50.0, -68.82)    #p1
t.goto(80.9, 26.28)   #p2
t.goto(0.0, 85.08)      #p3
t.goto(-80.9, 26.28)  #p4
t.goto(-50.0, -68.82)   #p0

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-02.py

#CH12-02:   原點圓心  逆時針 五角形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
t.up(); t.goto(0.0, -85.08); t.down()
t.circle(85.08)
t.up(); t.goto(-50.0, -68.82); t.down() #p0
t.goto(80.9, 26.28)   #p2
t.goto(-80.9, 26.28)  #p4
t.goto(50.0, -68.82)    #p1
t.goto(0.0, 85.08)      #p3
t.goto(-50.0, -68.82)   #p0


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-03.py

#CH12-03:   原點圓心  逆時針 五邊型  用串列
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50.0, -68.82], [50.0, -68.82], [80.9, 26.28], [0.0, 85.08], [-80.9, 26.28]]
t.up(); t.goto(0, -R); t.down()  #move only
t.circle(R)
x = list[0][0]; y = list[0][1]
t.up(); t.goto(x, y); t.down() #p0
x = list[1][0]; y = list[1][1]
t.goto(x, y)    #p1
x = list[2][0]; y = list[2][1]
t.goto(x, y)    #p2
x = list[3][0]; y = list[3][1]
t.goto(x, y)    #p3
x = list[4][0]; y = list[4][1]
t.goto(x, y)    #p4
x = list[0][0]; y = list[0][1]
t.goto(x, y)    #p0


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-04.py

#CH12-04:   原點圓心  逆時針 五邊  用串列
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50.0, -68.82], [50.0, -68.82], [80.9, 26.28], [0.0, 85.08], [-80.9, 26.28]]
t.up(); t.goto(0.0, -R); t.down()  #move only
t.circle(R)
x = list[0][0]; y = list[0][1]
t.up(); t.goto(x, y); t.down() #p0
for i in range(1,6):
    x = list[i%5][0]; y = list[i%5][1]
    t.goto(x, y)    #pn

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-05.py

#CH12-05:   原點圓心  五邊  迴圈用串列
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50.0, -68.82], [50.0, -68.82], [80.9, 26.28], [0.0, 85.08], [-80.9, 26.28]]
t.up(); t.goto(0.0, -R); t.down()
t.circle(R)
x = list[0][0]; y = list[0][1]
t.up(); t.goto(x, y); t.down() #p0
for i in [1, 2, 3, 4, 0]:
    x = list[i][0]; y = list[i][1]
    t.goto(x, y)    #pn


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-06.py

#CH12-06:   原點圓心  五邊形 用listSeq
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50.0, -68.82], [50.0, -68.82], [80.9, 26.28], [0.0, 85.08], [-80.9, 26.28]]
listSeq = [0, 1, 2, 3, 4, 0]
t.up(); t.goto(0.0, -R); t.down()
t.circle(R)
x = list[0][0]; y = list[0][1]
t.up(); t.goto(x, y); t.down() #p0  由listSeq定的起點
for i in range(1, 6):
    k = listSeq[i]
    ex = list[k][0]; ey = list[k][1]
    t.goto(ex, ey)    #draw to end point
    sx = ex; sy = ey
    t.up(); t.goto(sx, sy); t.down()   #move to start point
   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-07.py

#CH12-07:   原點圓心  五邊  用listPair
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50, -68.82], [50, -68.82], [80.9, 26.28], [0, 85.08], [-80.9, 26.28]]
listPair = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 5):
    s = listPair[i][0]; e = listPair[i][1]
    sx = list[s][0]; sy = list[s][1]
    ex = list[e][0]; ey = list[e][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 12\CH12-08.py

#CH12-08:   原點圓心  五邊形  用listPair(非連續)
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50, -68.82], [50, -68.82], [80.9, 26.28], [0, 85.08], [-80.9, 26.28]]
listPair = [[0, 1], [2, 3], [4, 0], [1, 2], [3, 4]]
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 5):
    s = listPair[i][0]; e = listPair[i][1]
    sx = list[s][0]; sy = list[s][1]
    ex = list[e][0]; ey = list[e][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-01.py

#CH13-01: 五邊型 累積位置值 round
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
SL = 100.0; ang = 360/5
accumAng = 0.0; accumPX = 0.0; accumPY = 0.0
print(accumAng, accumPX, accumPY)
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(ang)
    accumPX += SL *np.cos(accumAng*np.pi/180) 
    accumPY += SL *np.sin(accumAng*np.pi/180)
    accumAng += ang
    print(accumAng, accumPX, accumPY)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-02.py

#CH13-02  指令：round
for i in range(1,5):
    j= round(i)
    print(i)
print('+')
for i in [9.4, 9.5, 9.6, 9.7]:
    j= round(i)
    print(j)
print('+')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-03.py

#CH13-03  指令：round
for i in [9.4, 9.5, 9.6, 9.7]:
    j= round(i, 0)
    print(j)
print('+')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-04.py

#CH13-04  指令：round
for i in [9.4, 9.5, 9.6, 9.7]:
    j= round(i, 1)
    print(j)
print('+')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-05.py

#CH13-05  指令：round
for i in [0.94, 0.95, 0.96, 0.97]:
    j= round(i, 1)
    print(j)
print('+')
for i in [0.84, 0.85, 0.86, 0.87]:
    j= round(i, 1)
    print(j)
print('+')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-06.py

#CH13-06  指令：round
for i in [0.94, 0.95, 0.96, 0.97]:
    j= round(i, 2)
    print(j)
print('+')
for i in [0.84, 0.85, 0.86, 0.87]:
    j= round(i, 2)
    print(j)
print('+')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-07.py

#CH13-07  指令：round
k = 0.05
for i in range(1, 10):
    i = k+i/10 
    j= round(i, 1)
    print(i, j)
print('+')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-08.py

#CH13-08: 五邊形 累積位置值 round
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
SL = 100.0; ang = 360/5
accumAng = 0.0; accumPX = 0.0; accumPY = 0.0
print(accumAng, accumPX, accumPY)
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(ang)
    accumPX += SL *np.cos(accumAng*np.pi/180) 
    accumPY += SL *np.sin(accumAng*np.pi/180)
    accumAng += ang
    roundAccumAng = round(accumAng, 1)
    roundAccumPX = round(accumPX, 1)
    roundAccumPY = round(accumPY, 1)
    print(roundAccumAng, roundAccumPX, roundAccumPY)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-09.py

#CH13-09: 五邊形 累積位置值 round  有錯
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
SL = 100.0; ang = 360/5
accumAng = 0.0; accumPX = 0.0; accumPY = 0.0
print('['+accumPX+ ','+accumPY+']')
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(ang)
    accumPX += SL *np.cos(accumAng*np.pi/180) 
    accumPY += SL *np.sin(accumAng*np.pi/180)
    accumAng += ang
    roundAccumPX = round(accumPX, 1)
    roundAccumPY = round(accumPY, 1)
    print('['+accumPX+ ','+accumPY+']')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-10.py

#CH13-10: 五邊型 累積位置值 round
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
SL = 100.0; ang = 360/5
accumAng = 0.0; accumPX = 0.0; accumPY = 0.0
print('['+str(accumPX)+ ','+str(accumPY)+']')
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(ang)
    accumPX += SL *np.cos(accumAng*np.pi/180) 
    accumPY += SL *np.sin(accumAng*np.pi/180)
    accumAng += ang
    roundAccumPX = round(accumPX, 1)
    roundAccumPY = round(accumPY, 1)
    print('['+str(roundAccumPX)+ ','+str(roundAccumPY)+']')

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-11.py

#CH13-11: 五邊型 累積位置值 round 雙層串列
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
SL = 100.0; ang = 360/5
accumAng = 0.0; accumPX = 0.0; accumPY = 0.0
listStr = "["
listStr +='['+str(accumPX)+ ','+str(accumPY)+']'
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(ang)
    accumPX += SL *np.cos(accumAng*np.pi/180) 
    accumPY += SL *np.sin(accumAng*np.pi/180)
    accumAng += ang
    roundAccumPX = round(accumPX, 1)
    roundAccumPY = round(accumPY, 1)
    listStr += ', ['+str(roundAccumPX)+ ','+str(roundAccumPY)+']'
listStr += ']'
print(listStr)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-12.py

#CH13-12:   原點圓心 listA
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(1)

listA5 = [[0.0, 0.0], [100.0, 0.0], [130.9, 95.1], [50, 153.9], [-30.9, 95.1]]
listA6 = [[0.0, 0.0], [100.0, 0.0], [150.0, 86.6], [100.0, 173.2], [0.0, 173.2], [-50.0, 86.6]]
listA7 = [[0.0, 0.0], [100.0, 0.0], [162.3, 78.2], [140.1, 175.7], [50.0, 219.1], [-40.1, 175.7], [-62.3, 78.2]]
listA8 = [[0.0, 0.0], [100.0, 0.0], [170.7, 70.7], [170.7, 170.7], [100.0, 241.4], [0.0, 241.4], [-70.7, 170.7], [-70.7, 70.7]]
listA9 = [[0.0, 0.0], [100.0, 0.0], [176.6, 64.3], [194.0, 162.8], [144.0, 249.4], [50.0, 283.6], [-44.0, 249.4], [-94.0, 162.8], [-76.6, 64.3]]
listA10 = [[0.0, 0.0], [100.0, 0.0], [180.9, 58.8], [211.8, 153.9], [180.9, 249], [100.0, 307.8], [0.0, 307.8], [-80.9, 249.0], [-111.8, 153.9], [-80.9, 58.8]]
listA11 = [[0.0, 0.0], [100.0, 0.0], [184.1, 54.1], [225.7, 145.0], [211.4, 244.0], [145.9, 319.6], [50.0, 347.8], [-45.9, 319.6], [-111.4, 244.0], [-125.7, 145.0], [-84.1, 54.1]]
listA12 = [[0.0, 0.0], [100.0, 0.0], [186.6, 50.0], [236.6, 136.6], [236.6, 236.6], [186.6, 323.2], [100.0, 373.2], [0.0, 373.2], [-86.6, 323.2], [-136.6, 236.6], [-136.6, 136.6], [-86.6, 50.0]]
listA13 = [[0.0, 0.0], [100.0, 0.0], [188.5, 46.5], [245.4, 128.8], [257.4, 228.0], [221.9, 321.5], [147.1, 387.9], [50.0, 411.8], [-47.1, 387.9], [-121.9, 321.5], [-157.4, 228.0], [-145.4, 128.8], [-88.5, 46.5]]
listA14 = [[0.0, 0.0], [100.0, 0.0], [190.1, 43.4], [252.4, 121.6], [274.7, 219.1], [252.4, 316.6], [190.1, 394.7], [100.0, 438.1], [0.0, 438.1], [-90.1, 394.7], [-152.4, 316.6], [-174.7, 219.1], [-152.4, 121.6], [-90.1, 43.4]]




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-13.py

#CH13-13:   原點圓心  dX dY
import turtle
import numpy as np
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
Rad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dX =  [ 50.0, -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0]
dY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SL = 100
for i in range(5, 15):
    ang = 360/i
    Rad[i-5] = round(-1*SL/(2*np.sin(ang*np.pi/360)), 1)
    dY[i-5] = round(-1*SL/(2*np.tan(ang*np.pi/360)), 1)
print(Rad)
print(dY)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-14.py

#CH13-14:   原點圓心 五邊形起  由A轉C
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)

listA5 = [[0.0, 0.0], [100.0, 0.0], [130.9, 95.1], [50, 153.9], [-30.9, 95.1]]
listA6 = [[0.0, 0.0], [100.0, 0.0], [150.0, 86.6], [100.0, 173.2], [0.0, 173.2], [-50.0, 86.6]]
listA7 = [[0.0, 0.0], [100.0, 0.0], [162.3, 78.2], [140.1, 175.7], [50.0, 219.1], [-40.1, 175.7], [-62.3, 78.2]]
listA8 = [[0.0, 0.0], [100.0, 0.0], [170.7, 70.7], [170.7, 170.7], [100.0, 241.4], [0.0, 241.4], [-70.7, 170.7], [-70.7, 70.7]]
listA9 = [[0.0, 0.0], [100.0, 0.0], [176.6, 64.3], [194.0, 162.8], [144.0, 249.4], [50.0, 283.6], [-44.0, 249.4], [-94.0, 162.8], [-76.6, 64.3]]
listA10 = [[0.0, 0.0], [100.0, 0.0], [180.9, 58.8], [211.8, 153.9], [180.9, 249], [100.0, 307.8], [0.0, 307.8], [-80.9, 249.0], [-111.8, 153.9], [-80.9, 58.8]]
listA11 = [[0.0, 0.0], [100.0, 0.0], [184.1, 54.1], [225.7, 145.0], [211.4, 244.0], [145.9, 319.6], [50.0, 347.8], [-45.9, 319.6], [-111.4, 244.0], [-125.7, 145.0], [-84.1, 54.1]]
listA12 = [[0.0, 0.0], [100.0, 0.0], [186.6, 50.0], [236.6, 136.6], [236.6, 236.6], [186.6, 323.2], [100.0, 373.2], [0.0, 373.2], [-86.6, 323.2], [-136.6, 236.6], [-136.6, 136.6], [-86.6, 50.0]]
listA13 = [[0.0, 0.0], [100.0, 0.0], [188.5, 46.5], [245.4, 128.8], [257.4, 228.0], [221.9, 321.5], [147.1, 387.9], [50.0, 411.8], [-47.1, 387.9], [-121.9, 321.5], [-157.4, 228.0], [-145.4, 128.8], [-88.5, 46.5]]
listA14 = [[0.0, 0.0], [100.0, 0.0], [190.1, 43.4], [252.4, 121.6], [274.7, 219.1], [252.4, 316.6], [190.1, 394.7], [100.0, 438.1], [0.0, 438.1], [-90.1, 394.7], [-152.4, 316.6], [-174.7, 219.1], [-152.4, 121.6], [-90.1, 43.4]]

Rad = [85.1, 100.0, 115.2, 130.7, 146.2, 161.8, 177.5, 193.2, 208.9, 224.7]
dX =  [ -50.0, -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0]
dY =  [-68.8, -86.6, -103.8, -120.7, -137.4, -153.9, -170.3, -186.6, -202.9, -219.1]

listB = listA8
for i in range(0, 8):
    listB[i][0] = round(listA8[i][0]+dX[3], 1)
    listB[i][1] = round(listA8[i][1]+dY[3], 1)
print(listB)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 13\CH13-sample.py

#CH13-sample:   原點圓心 listC5~C14 
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)

listC5 = [[-50.0, -68.8], [50.0, -68.8], [80.9, 26.3], [0.0, 85.1], [-80.9, 26.3]]
listC6 = [[-50.0, -86.6], [50.0, -86.6], [100.0, 0.0], [50.0, 86.6], [-50.0, 86.6], [-100.0, 0.0]]
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listC8 = [[-50.0, -120.7], [50.0, -120.7], [120.7, -50.0], [120.7, 50.0], [50.0, 120.7], [-50.0, 120.7], [-120.7, 50.0], [-120.7, -50.0]]
listC9 = [[-50.0, -137.4], [50.0, -137.4], [126.6, -73.1], [144.0, 25.4], [94.0, 112.0], [0.0, 146.2], [-94.0, 112.0], [-144.0, 25.4], [-126.6, -73.1]]
listC10 = [[-50.0, -153.9], [50.0, -153.9], [130.9, -95.1], [161.8, 0.0], [130.9, 95.1], [50.0, 153.9], [-50.0, 153.9], [-130.9, 95.1], [-161.8, 0.0], [-130.9, -95.1]]
listC11 = [[-50.0, -170.3], [50.0, -170.3], [134.1, -116.2], [175.7, -25.3], [161.4, 73.7], [95.9, 149.3], [0.0, 177.5], [-95.9, 149.3], [-161.4, 73.7], [-175.7, -25.3], [-134.1, -116.2]]
listC12 = [[-50.0, -186.6], [50.0, -186.6], [136.6, -136.6], [186.6, -50.0], [186.6, 50.0], [136.6, 136.6], [50.0, 186.6], [-50.0, 186.6], [-136.6, 136.6], [-186.6, 50.0], [-186.6, -50.0], [-136.6, -136.6]]
listC13 = [[-50.0, -202.9], [50.0, -202.9], [138.5, -156.4], [195.4, -74.1], [207.4, 25.1], [171.9, 118.6], [97.1, 185.0], [0.0, 208.9], [-97.1, 185.0], [-171.9, 118.6], [-207.4, 25.1], [-195.4, -74.1], [-138.5, -156.4]]
listC14 = [[-50.0, -219.1], [50.0, -219.1], [140.1, -175.7], [202.4, -97.5], [224.7, 0.0], [202.4, 97.5], [140.1, 175.6], [50.0, 219.0], [-50.0, 219.0], [-140.1, 175.6], [-202.4, 97.5], [-224.7, 0.0], [-202.4, -97.5], [-140.1, -175.7]]


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-01.py

#CH14-01:   原點圓心  七邊形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]
R = 115.2
SL = 100
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i][0]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = listPair[i][1]
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-02.py

#CH14-02:   原點圓心  七角形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [[0, 2], [2, 4], [4, 6], [6, 1], [1, 3], [3, 5], [5, 0]]
R = 115.2
SL = 100
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i][0]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = listPair[i][1]
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-03.py

#CH14-03:   原點圓心  七角形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [[0, 3], [3, 6], [6, 2], [2, 5], [5, 1], [1, 4], [4, 0]]
R = 115.2
SL = 100
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i][0]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = listPair[i][1]
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-04.py

#CH14-04:   原點圓心  七角形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [[0, 4], [4, 1], [1, 5], [5, 2], [2, 6], [6, 3], [3, 0]]
R = 115.2
SL = 100
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i][0]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = listPair[i][1]
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-05.py

#CH14-05:   原點圓心  七邊形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [0, 1, 2, 3, 4, 5, 6]
R = 115.2
SL = 100
toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s+toEnd
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-06.py

#CH14-06:   原點圓心  七邊形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [0, 2, 4, 6, 1, 3, 5]
R = 115.2
SL = 100
toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s+toEnd
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-07.py

#CH14-07:   原點圓心  七邊形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
R = 115.2
SL = 100
start = 0; newStart = 2; toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
s = start
for i in range(0, 7):
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s + toEnd
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point
    s = s + newStart



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-08.py

#CH14-08:   原點圓心  多邊形  雙層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)

listC5 = [[-50.0, -68.8], [50.0, -68.8], [80.9, 26.3], [0.0, 85.1], [-80.9, 26.3]]
listC6 = [[-50.0, -86.6], [50.0, -86.6], [100.0, 0.0], [50.0, 86.6], [-50.0, 86.6], [-100.0, 0.0]]
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listC8 = [[-50.0, -120.7], [50.0, -120.7], [120.7, -50.0], [120.7, 50.0], [50.0, 120.7], [-50.0, 120.7], [-120.7, 50.0], [-120.7, -50.0]]
listC9 = [[-50.0, -137.4], [50.0, -137.4], [126.6, -73.1], [144.0, 25.4], [94.0, 112.0], [0.0, 146.2], [-94.0, 112.0], [-144.0, 25.4], [-126.6, -73.1]]
listC10 = [[-50.0, -153.9], [50.0, -153.9], [130.9, -95.1], [161.8, 0.0], [130.9, 95.1], [50.0, 153.9], [-50.0, 153.9], [-130.9, 95.1], [-161.8, 0.0], [-130.9, -95.1]]
listC11 = [[-50.0, -170.3], [50.0, -170.3], [134.1, -116.2], [175.7, -25.3], [161.4, 73.7], [95.9, 149.3], [0.0, 177.5], [-95.9, 149.3], [-161.4, 73.7], [-175.7, -25.3], [-134.1, -116.2]]
listC12 = [[-50.0, -186.6], [50.0, -186.6], [136.6, -136.6], [186.6, -50.0], [186.6, 50.0], [136.6, 136.6], [50.0, 186.6], [-50.0, 186.6], [-136.6, 136.6], [-186.6, 50.0], [-186.6, -50.0], [-136.6, -136.6]]
listC13 = [[-50.0, -202.9], [50.0, -202.9], [138.5, -156.4], [195.4, -74.1], [207.4, 25.1], [171.9, 118.6], [97.1, 185.0], [0.0, 208.9], [-97.1, 185.0], [-171.9, 118.6], [-207.4, 25.1], [-195.4, -74.1], [-138.5, -156.4]]
listC14 = [[-50.0, -219.1], [50.0, -219.1], [140.1, -175.7], [202.4, -97.5], [224.7, 0.0], [202.4, 97.5], [140.1, 175.6], [50.0, 219.0], [-50.0, 219.0], [-140.1, 175.6], [-202.4, 97.5], [-224.7, 0.0], [-202.4, -97.5], [-140.1, -175.7]]

listComb = [listC5, listC6, listC7, listC8, listC9, listC10, listC11, listC12, listC13, listC14]
Rad = [85.1, 100.0, 115.2, 130.7, 146.2, 161.8, 177.5, 193.2, 208.9, 224.7]
start = 0; newStart = 1; toEnd = 1
for sides in range(5, 9):
    listCC = listComb[sides-5]  #
    R = Rad[sides-5]
    t.up(); t.goto(0, -R); t.down()
    t.circle(R)
    s = start
    for i in range(0, sides):
        sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
        t.up(); t.goto(sx, sy); t.down()   #move to start point
        e = s + toEnd
        ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
        t.goto(ex, ey)    #draw to end point
        s = s + newStart
t.up(); t.goto(-50, 150); t.down()
t.goto(-50, -150)
t.up(); t.goto(50, 150); t.down()
t.goto(50, -150)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-09.py

#CH14-09:   原點圓心  針對六邊形  兩個單層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 6
listC6 = [[-50.0, -86.6], [50.0, -86.6], [100.0, 0.0], [50.0, 86.6], [-50.0, 86.6], [-100.0, 0.0]]
listCC = listC6
Rad = [85.1, 100.0, 115.2, 130.7, 146.2, 161.8, 177.5, 193.2, 208.9, 224.7]
R = 100
start = 0; newStart = 2; toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
s = start
for i in range(0, int(sides/2)):   #Notice
    sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s + toEnd
    ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
    t.goto(ex, ey)    #draw to end point
    s = s + newStart
s = start+1
for i in range(0, int(sides/2)):   #Notice
    sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s + toEnd
    ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
    t.goto(ex, ey)    #draw to end point
    s = s + newStart



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-10.py

#CH14-10:   原點圓心  八邊形  二層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 8
listC8 = [[-50.0, -120.7], [50.0, -120.7], [120.7, -50.0], [120.7, 50.0], [50.0, 120.7], [-50.0, 120.7], [-120.7, 50.0], [-120.7, -50.0]]
listCC = listC8
Rad = [85.1, 100.0, 115.2, 130.7, 146.2, 161.8, 177.5, 193.2, 208.9, 224.7]
R = 130.7
start = 0; newStart = 2; toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for j in range(start, start+2):
    s = j
    for i in range(0, int(sides/2)):   #Notice
        sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
        t.up(); t.goto(sx, sy); t.down()   #move to start point
        e = s + toEnd
        ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
        t.goto(ex, ey)    #draw to end point
        s = s + newStart


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-11.py

#CH14-11:   原點圓心  十二邊形  二層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 12
listC12 = [[-50.0, -186.6], [50.0, -186.6], [136.6, -136.6], [186.6, -50.0], [186.6, 50.0], [136.6, 136.6], [50.0, 186.6], [-50.0, 186.6], [-136.6, 136.6], [-186.6, 50.0], [-186.6, -50.0], [-136.6, -136.6]]
listCC = listC12
R = 193.2
start = 0; newStart = 2; toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for j in range(start, start+2):
    s = j
    for i in range(0, int(sides/2)):
        sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
        t.up(); t.goto(sx, sy); t.down()   #move to start point
        e = s + toEnd
        ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
        t.goto(ex, ey)    #draw to end point
        s = s + newStart


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-12.py

#CH14-12:   原點圓心  十二邊形  二層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 12
listC12 = [[-50.0, -186.6], [50.0, -186.6], [136.6, -136.6], [186.6, -50.0], [186.6, 50.0], [136.6, 136.6], [50.0, 186.6], [-50.0, 186.6], [-136.6, 136.6], [-186.6, 50.0], [-186.6, -50.0], [-136.6, -136.6]]
listCC = listC12
R = 193.2
start = 0; newStart = 3; toEnd = 3
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for j in range(start, start+3):
    s = j
    for i in range(0, int(sides/2)):
        sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
        t.up(); t.goto(sx, sy); t.down()   #move to start point
        e = s + toEnd
        ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
        t.goto(ex, ey)    #draw to end point
        s = s + newStart

       


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 14\CH14-13.py

#CH14-13:   原點圓心  十二邊形  二層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 12
listC12 = [[-50.0, -186.6], [50.0, -186.6], [136.6, -136.6], [186.6, -50.0], [186.6, 50.0], [136.6, 136.6], [50.0, 186.6], [-50.0, 186.6], [-136.6, 136.6], [-186.6, 50.0], [-186.6, -50.0], [-136.6, -136.6]]
listCC = listC12
R = 193.2
start = 0; newStart = 4; toEnd = 4
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for j in range(start, start+4):
    s = j
    for i in range(0, int(sides/4)):
        sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
        t.up(); t.goto(sx, sy); t.down()   #move to start point
        e = s + toEnd
        ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
        t.goto(ex, ey)    #draw to end point
        s = s + newStart

       


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-01.py

#CH15-01: : 等角平分線   第一回
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1= 161.7 
sides = 5
ang =360/sides
t.color("black")
for i in range(1,sides+1):
    t.forward(100);  t.left(ang)
t.color("red")
t.left(0)
t.forward(SL1);  t.backward(SL1);
t.left(ang/2)
t.forward(SL1);  t.backward(SL1);
t.left(ang/2)
t.forward(SL1);  t.backward(SL1);
t.left(ang/2)
t.forward(SL1);  t.backward(SL1);
t.left(ang/2)
t.forward(SL1);  t.backward(SL1);
t.left(ang/2)
t.forward(SL1);  t.backward(SL1);
t.left(180)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-02.py

#CH15-02:等角平分線   第二回
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1= 161.7
sides = 5
ang =360/sides
t.color("black")
for i in range(1,sides+1):
    t.forward(100);  t.left(ang)
t.color("green")
t.width(5)
t.left(ang/2)
t.forward(SL1)
t.color("red")
t.width(3)
t.left(3*ang/2)
t.forward(SL1);  t.backward(SL1)
for j in range(1,6):
    t.left(ang/2)
    t.forward(SL1);  t.backward(SL1)
t.left(180)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-03.py

#CH15-03: 等角平分線   第三回
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1= 161.7 
sides = 5
ang =360/sides
t.color("black")
for i in range(1,sides+1):
    t.forward(100);  t.left(ang)
t.color("green")
t.width(5)
t.left(ang/2)
t.forward(SL1)
t.left(4*ang/2)
t.forward(SL1)
t.color("red")
t.width(3)
t.left(3*ang/2)
t.forward(SL1);  t.backward(SL1);
for i in range(1,sides+1):
    t.left(ang/2)
    t.forward(SL1);  t.backward(SL1);
t.left(180)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-04.py

#CH15-04:  五角形 兩個單層迴圈
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1 = 161.7; R = 85.08 
sides = 5
ang =360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.goto(0, -R); t.down()  #move only
t.circle(R)
t.up(); t.goto(-50, -68.82); t.down()  #move only
t.color(colorsList[0])
t.left(0*ang/2)
for j in range(1,sides+1):    #第一個五邊形
    t.forward(SL);  t.left(1*ang)
t.left(0*ang/2)
t.color(colorsList[1])
t.left(1*ang/2)
for j in range(1,sides+1):    #第一個五角形
    t.forward(SL1);  t.left(2*ang)
t.right(1*ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-05.py

#CH15-05:  五角形 三個單層迴圈
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1 = 161.7; R = 85.08 
sides = 5
ang =360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.setheading(-90); t.forward(R); t.setheading(0); t.down()  #move only
t.circle(R)
t.up(); t.home(); t.setheading(-90-ang/2); t.forward(R); t.setheading(0); t.down()  #move onlyt
t.color(colorsList[0])
t.left(0*ang/2)
for j in range(1,sides+1):    #第一個五邊形
    t.forward(SL);  t.left(1*ang)
t.right(0*ang/2)
t.color(colorsList[1])
t.left(1*ang/2)
for j in range(1,sides+1):    #第一個五角形
    t.forward(SL1);  t.left(2*ang)
t.right(1*ang/2)
t.color(colorsList[2])
t.left(2*ang/2)
for j in range(1,sides+1):    #第二個五角形
    t.forward(SL1);  t.left(3*ang)
t.right(2*ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-06.py

#CH15-06: 五角形 四個單層迴圈 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1 = 161.7; R = 85.08 
sides = 5
ang =360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
t.circle(R)
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
t.color(colorsList[0])
t.left(0*ang/2)
for j in range(1,sides+1):    #第一個五邊形
    t.forward(SL);  t.left(1*ang)
t.right(0*ang/2)
t.color(colorsList[1])
t.left(1*ang/2)
for j in range(1,sides+1):    #第一個五角形
    t.forward(SL1);  t.left(2*ang)
t.right(1*ang/2)
t.color(colorsList[2])
t.left(2*ang/2)
for j in range(1,sides+1):    #第二個五角形
    t.forward(SL1);  t.left(3*ang)
t.right(2*ang/2)
t.color(colorsList[3])
t.left(3*ang/2)
for j in range(1,sides+1):    #第二個五邊形
    t.forward(SL);  t.left(4*ang)
t.right(3*ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-07.py

#CH15-07: 五角形 一個兩層迴圈
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 5
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang =360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
t.circle(R)
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
for i in range(1,sides+1):
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    for j in range(1,sides+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-08.py

#CH15-08: 同外接圓不同九角形 show數值
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3)
SL = 100
sides = 9
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
t.circle(R)
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
for i in range(1, sides+1):
    if (i == sides): t.speed(5)
    else: t.speed(0)
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    for j in range(1,sides+1):
        t.forward(SLn);  t.left(i*ang)
    print(i, i*ang, SLn)
    t.left(ang/2) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 15\CH15-09.py

#CH15-09: 同外接圓不同九角形 最後一圈不執行
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 9
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
t.circle(R)
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
for i in range(1, sides+1):
    if (i != sides): #留意!
        t.color(colorsList[(i-1)%8])
        SLn = np.sin(i*np.pi/sides)*2*R
        t.left((i-1)*ang/2)
        for j in range(1,sides+1):
            t.forward(SLn);  t.left(i*ang)
        t.right((i-1)*ang/2)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 16\CH16-01.py

#CH16-01: 同外接圓不同八角形 黑白
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 8
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
#t.up(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
#t.circle(R)
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
for i in [1,2,3,4,5,6,7]:
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    for j in range(1,sides+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 16\CH16-02.py

#CH16-02: 同外接圓不同八角形 彩色
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 8
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
for i in [1,2,3,4,5,6,7]:
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    for j in range(1,sides+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 16\CH16-03.py

#CH16-03: 同外接圓不同八角形 專注於個別的多角形
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 8
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
for i in [1]:
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    for j in range(1,sides+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 16\CH16-04.py

#CH16-04: 同外接圓不同八角形 把偶數多角形調為上下尖   有錯
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(0)
SL = 100
sides = 8
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
t.left(ang/2)
for i in [1,2,3,4,5,6,7]:
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    for j in range(1,sides+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)
t.right(ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 16\CH16-05.py

#CH16-05: 同外接圓不同八角形 上下尖  減少重複性
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 8
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
modiList = [[1,sides], [2,4], [3,sides], [4,2], [5,sides], [6,4], [7,sides], [8,sides]]
t.up(); t.home(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
t.left(ang/2)
for i in [1,2,3,4,5,6,7]:
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    k = modiList[i-1]
    for j in range(1,k[1]+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)
t.right(ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 16\CH16-06.py

#CH16-06: 同外接圓不同十二角形 上下尖  減少重複性
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 12
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
modiList = [[1,sides], [2,6], [3,4], [4,3], [5,sides], [6,2], [7,sides], [8,3], [9,4], [10,6], [11,sides], [12,sides]]
t.up(); t.home(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
t.left(ang/2)
for i in [1,2,3,4,5,6,7,8,9,10,11]:
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    k = modiList[i-1]
    for j in range(1,k[1]+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)
t.right(ang/2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-01.py

#CH17-01: input= 48659117103  非正確結果
listInput = [[4, 90], [8, 45], [6, 60], [5, 75], [9, 40], [11, 32.72], [7, 51.43], [3, 120]]
listSort = []
listSort.append(listInput[0])
print(listSort)
listSort.append(listInput[1])
print(listSort)
listSort.append(listInput[2])
print(listSort)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-02.py

#CH17-02: input= 48659117103
listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listSort = []
listSort.append(listInput[0])
listSort.append(listInput[1])
i = 1
listSortLeft = listSort[0]   #不周全
listSortRight = listSort[1]   #不周全
print(listSortLeft, listSortRight)
listSort = []
listSort.append(listSortLeft)
listSort.append(listInput[2])
listSort.append(listSortRight)
print(listSort)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-03.py

#CH17-03: input= 48659117103
inputData = [7, 51.43]
listSortTemp = [[4, 90.0], [5, 72.0], [6, 60.0], [8, 45.0], [9, 40.0], [11, 32.72]]
i = 3
listSort = []
for i in range(0, 3):
    listSort.append(listSortTemp[i])
print(listSort)
listSort.append(inputData)
print(listSort)
for i in range(4, 6):
    listSort.append(listSortTemp[i])
print(listSort)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-04.py

#CH17-04: input= 48659117103
listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listSort = []
listSort.insert(0, listInput[0])  #4
listSort.insert(1, listInput[1])  #8
listSort.insert(1, listInput[2])  #6
listSort.insert(1, listInput[3])  #5
listSort.insert(5, listInput[4])  #9
listSort.insert(6, listInput[5])  #11
print(listSort)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-05.py

#CH17-05: input= 48659117103
listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listSort = []
listSort.insert(0, listInput[0])  #4
listSort.insert(1, listInput[1])  #8
listSort.insert(1, listInput[2])  #6
listSort.insert(1, listInput[3])  #5
listSort.insert(5, listInput[4])  #9
listSort.insert(6, listInput[5])  #11
listSort.insert(3, listInput[6])  #7
listSort.insert(6, listInput[7])  #10
listSort.insert(0, listInput[8])  #3
print(listSort)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-06.py

#CH17-06: input= 48659117103
listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listSort = [listInput[0]]
def fun(length, k):
    j = 0
    for i in range(0, length):
        print(listSort[i][0], listInput[k][0])
        if (listSort[i][0] <= listInput[k][0]):
            j = i
    return(j+1)
m = fun(len(listSort), 1)
listSort.insert(m, listInput[1])
m = fun(len(listSort), 2)
listSort.insert(m, listInput[2])
print(listSort)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-07.py

#CH17-07: input= 48659117103   有錯的
listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listSort = [listInput[0]]
def fun(length, k):
    j = 0
    for i in range(0, length):
        if (listSort[i][0] <= listInput[k][0]):
            j = i
    return(j+1)
for n in range(1, len(listInput)):
    m = fun(len(listSort), n)
    listSort.insert(m, listInput[n])
print(listSort)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-08.py

#CH17-08: input= 48659117103
#listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listInput = [[11, 32.72], [10, 36.0], [9, 40.0], [8, 45.0], [7, 51.43], [6, 60.0], [5, 72.0], [4, 90.0], [3, 120.0]]
listSort = [listInput[0]]
def fun(length, k):
    j = 0
    for i in range(0, length):
        if (listSort[i][0] > listInput[k][0])and(i == 0):
            j = -1
        elif (listSort[i][0] <= listInput[k][0]):
            j = i
    return(j+1)
for n in range(1, len(listInput)):
    m = fun(len(listSort), n)
    listSort.insert(m, listInput[n])
print(listSort)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-09.py

#CH17-09: input= 48659117103 
listInput = [[4, 90], [8, 45], [6, 60], [5, 75], [9, 40], [11, 32.72], [7, 51.43], [3, 120]]
listSort = listInput
listSortTemp = listSort[0]
listSort[0] = listSort[1]
listSort[1] = listSortTemp
print(listSort)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-10.py

#CH17-10: input= 48659117103 
listInput = [[4, 90], [8, 45], [6, 60], [5, 75], [9, 40], [11, 32.72], [7, 51.43], [10, 36], [3, 120]]
listSort = listInput
for i in range(0, 8):
    if (listSort[i]<listSort[i+1]):
        listSortTemp = listSort[i]
        listSort[i] = listSort[i+1]
        listSort[i+1] = listSortTemp
        print(listSort)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\CH 17\CH17-11.py

#CH17-11: input= 48659117103 
listInput = [[4, 90], [8, 45], [6, 60], [5, 75], [9, 40], [11, 32.72], [7, 51.43], [10, 36], [3, 120]]
listSort = listInput
for j in range(8, 0, -1):
    for i in range(0, j):
        if (listSort[i]<listSort[i+1]):
            listSortTemp = listSort[i]
            listSort[i] = listSort[i+1]
            listSort[i+1] = listSortTemp
            print(listSort, i)

print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\others\CH09A01.py

#CH09A01 三到八邊形  用兩list[[筆畫色 角度]] [邊數]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [['red', 120.0], ['orange', 90.0], ['yellow', 72.0], ['green', 60.0], ['blue', 51.43], ['cyan', 45.0]]
list2 = [3,4,5,6,7,8]
for i in range(1, 7):
    t.color(list1[i-1][0])
    for j in range(1, list2[i-1]+1):
        t.forward(100);  t.left(list1[i-1][1]) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\others\CH10-A1.py

#CH10-A1 三到八邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def fun(par1, par2):
    for j in range(1, par1+1):
        t.forward(100);  t.left(par2)
fun(3, 120.0)
for j in range(1, 4+1):
    t.forward(100);  t.left(90.0)
for j in range(1, 5+1):
    t.forward(100);  t.left(72.0)
for j in range(1, 6+1):
    t.forward(100);  t.left(60.0)
for j in range(1, 7+1):
    t.forward(100);  t.left(51.43)
fun(8, 45.0)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\運算思維與T同遊Python-邏輯運算與程式設計\others\CH10-A2.py

#CH10-A2 三到八邊形   顏色
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
def funDraw(sides, ang):
    for j in range(1, sides+1):
        t.forward(100);  t.left(ang)
def funExt(sides, ang, color):
    t.color(color)
    funDraw(sides, ang)
def funExt1(sides, ang, color, width):
    t.width(width)
    funExt(sides, ang, color)
funExt1(3, 120.0, 'red', 1)
funExt1(4, 90.0, 'orange', 3)
funExt1(5, 72.0, 'yellow', 1)
funExt1(6, 60.0, 'green', 3)
funExt1(7, 51.43, 'blue', 1)
funExt1(8, 45.0, 'cyan', 3)

print("------------------------------------------------------------")  # 60個


