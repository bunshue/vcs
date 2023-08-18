# ch19_20_7.py
from tkinter import *
from random import *
def display():
    if Flag:       
        if ball.get() == "1":
            raceResult.set("恭喜你贏了, Ball 1勝利")
        else:
            raceResult.set("抱歉你輸了, Ball 1勝利")
    else:
        if ball.get() == "1":
            raceResult.set("抱歉你輸了, Ball 2勝利")
        else:
            raceResult.set("恭喜你贏了, Ball 2勝利")
    startBtn.set("重置")

def running():
    global Flag
    if startBtn.get() == "重置":
        startBtn.set("開始")
        raceResult.set("")
        canvas.delete('all')
        canvas.create_text(10,50,text="1")
        id1 = canvas.create_oval(20,50,70,100,fill='yellow')
        canvas.create_text(10,150,text="2")
        id2 = canvas.create_oval(20,150,70,200,fill='aqua')
        return
    canvas.delete('all')
    canvas.create_text(10,50,text="1")
    id1 = canvas.create_oval(20,50,70,100,fill='yellow')
    canvas.create_text(10,150,text="2")
    id2 = canvas.create_oval(20,150,70,200,fill='aqua')
    id1Loc, id2Loc = 0, 0
    for x in range(0, 100):
        if ball.get() == '1':
            weight = 40
            raceResult.set("")
        elif ball.get() == '2':
            weight = 60
            raceResult.set("")
        else:
            raceResult.set("輸入錯誤!")
            return
        if randint(1,100) > weight:
            canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
            id2Loc += 1
        else:
            canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素
            id1Loc += 1
        tk.update()                 # 強制tkinter重繪
        canvas.after(50)
    if id1Loc > id2Loc:
        Flag = True
    else:
        Flag = False
    display()

tk = Tk()
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
canvas.create_text(10,50,text="1")
canvas.create_oval(20,50,70,100,fill='yellow')
canvas.create_text(10,150,text="2")
canvas.create_oval(20,150,70,200,fill='aqua')

Flag = True                         # 判斷那一球勝利

frame = Frame(tk)                   # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入獲勝的球, 按鈕Button
Label(frame, text="那一個球獲勝 : ").pack(side=LEFT)
ball = StringVar()
ball.set("1or2")
entry = Entry(frame, textvariable=ball).pack(side=LEFT,padx=3)
startBtn = StringVar()
startBtn.set("開始")
Button(frame, textvariable=startBtn,command=running).pack(side=LEFT)
raceResult = StringVar()

Label(frame,width=16,textvariable=raceResult).pack(side=LEFT,padx=3)

tk.mainloop()


