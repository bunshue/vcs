import tkinter
import random
import time

masu = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
shirushi = 0
kachi = 0
FNT = ("Times New Roman", 60)

def masume():
    cvs.delete("all")
    for i in range(1, 3):
        cvs.create_line(200*i, 0, 200*i, 600, fill="gray", width=8)
        cvs.create_line(0, i*200, 600, i*200, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(X+20, Y+20, X+180, Y+180, outline="blue", width=12)
            if masu[y][x] == 2:
                cvs.create_line(X+20, Y+20, X+180, Y+180, fill="red", width=12)
                cvs.create_line(X+180, Y+20, X+20, Y+180, fill="red", width=12)
    if shirushi == 0:
        cvs.create_text(300, 300, text="遊戲開始！", fill="navy", font=FNT)
    cvs.update()

def click(e):
    global shirushi
    if shirushi == 9:
        replay()
        return
    if shirushi==1 or shirushi==3 or shirushi==5 or shirushi==7:
        return
    mx = int(e.x/200)
    my = int(e.y/200)
    if mx>2: mx = 2
    if my>2: my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi = shirushi + 1
        masume()
        time.sleep(0.5)
        hantei()
        syouhai()
        if shirushi < 9:
            computer()
            masume()
            time.sleep(0.5)
            hantei()
            syouhai()

def computer():
    global shirushi
    #有沒有連成一線的符號
    for y in range(3):
        for x in range(3):
            if masu[y][x] == 0:
                masu[y][x] = 2
                hantei()
                if kachi==2:
                    shirushi = shirushi + 1
                    return
                masu[y][x] = 0
    #阻止玩家連成一線
    for y in range(3):
        for x in range(3):
            if masu[y][x] == 0:
                masu[y][x] = 1
                hantei()
                if kachi==1:
                    masu[y][x] = 2
                    shirushi = shirushi + 1
                    return
                masu[y][x] = 0
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if masu[y][x] == 0:
            masu[y][x] = 2
            shirushi = shirushi + 1
            break

def hantei():
    global kachi
    kachi = 0
    for n in range(1, 3):
        #判斷垂直方向是否連成一線
        if masu[0][0]==n and masu[1][0]==n and masu[2][0]==n:
            kachi = n
        if masu[0][1]==n and masu[1][1]==n and masu[2][1]==n:
            kachi = n
        if masu[0][2]==n and masu[1][2]==n and masu[2][2]==n:
            kachi = n
        #判斷水平方向是否連成一線
        if masu[0][0]==n and masu[0][1]==n and masu[0][2]==n:
            kachi = n
        if masu[1][0]==n and masu[1][1]==n and masu[1][2]==n:
            kachi = n
        if masu[2][0]==n and masu[2][1]==n and masu[2][2]==n:
            kachi = n
        #判斷傾斜方向是否連成一線
        if masu[0][0]==n and masu[1][1]==n and masu[2][2]==n:
            kachi = n
        if masu[0][2]==n and masu[1][1]==n and masu[2][0]==n:
            kachi = n

def syouhai():
    global shirushi
    if kachi == 1:
        cvs.create_text(300, 300, text="玩家獲勝！", font=FNT, fill="cyan")
        shirushi = 9
    if kachi == 2:
        cvs.create_text(300, 300, text="電腦\n獲勝！", font=FNT, fill="gold")
        shirushi = 9
    if kachi == 0 and shirushi == 9:
        cvs.create_text(300, 300, text="平手", font=FNT, fill="lime")

def replay():
    global shirushi
    shirushi = 0
    for y in range(3):
        for x in range(3):
            masu[y][x] = 0
    masume()

root = tkinter.Tk()
root.title("井字遊戲")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()
