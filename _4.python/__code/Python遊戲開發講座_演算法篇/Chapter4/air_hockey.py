import tkinter

FNT = ("Times New Roman", 60)
mx = 0
my = 0
mc = 0
proc = 0
tmr = 0
you_x = 750
you_y = 300
you_vx = 0
you_vy = 0
com_x = 250
com_y = 300
com_vx = 0
com_vy = 0
pu_x = 500
pu_y = 300
pu_vx = 10
pu_vy = 5
level = 0
point_you = 0
point_com = 0
POINT_WIN = 5
goal = [0, 0]


def click(e):
    global mc
    mc = 1


def move(e):
    global mx, my
    mx = e.x
    my = e.y


def draw_table():
    cvs.delete("all")
    for i in range(2):
        if goal[i] > 0:
            goal[i] -= 1
            if goal[i] % 2 == 0:
                cvs.create_rectangle(980 * i, 180, 980 * i + 20, 420, fill="yellow")
    cvs.create_image(500, 300, image=img_table)
    cvs.create_image(pu_x, pu_y, image=img_puck)
    cvs.create_image(you_x, you_y, image=img_sma_b)
    cvs.create_image(com_x, com_y, image=img_sma_r)
    cvs.create_text(
        500, 40, text=str(point_com) + " - " + str(point_you), font=FNT, fill="white"
    )
    if proc == 0:
        cvs.create_image(500, 160, image=img_title)
        cvs.create_text(250, 440, text="Normal", font=FNT, fill="lime")
        cvs.create_text(750, 440, text="Hard", font=FNT, fill="gold")
    if proc == 2:
        if point_you == POINT_WIN:
            cvs.create_text(
                1000 - tmr * 10, 300, text="YOU WIN!", font=FNT, fill="cyan"
            )
        else:
            cvs.create_text(tmr * 10, 300, text="COM WIN!", font=FNT, fill="red")


def smasher_you():
    global you_x, you_y, you_vx, you_vy
    you_vx = mx - you_x
    you_vy = my - you_y
    you_x = mx
    you_y = my


def smasher_com():
    global com_x, com_y, com_vx, com_vy
    dots = 20 + level * 10
    x = com_x
    y = com_y
    if get_dis(com_x, com_y, pu_x, pu_y) < 50 * 50:
        com_x -= dots
    elif pu_vx < 4 and com_x < 900:
        if com_y < pu_y - dots:
            com_y += dots
        if com_y > pu_y + dots:
            com_y -= dots
        if com_x < pu_x - dots:
            com_x += dots
        if com_x > pu_x + dots:
            com_x -= dots
    else:
        com_x += (60 - com_x) / (16 - level * 6)
        com_y += (300 - com_y) / (16 - level * 6)
    com_vx = com_x - x
    com_vy = com_y - y


def puck_comeout():
    global pu_x, pu_y, pu_vx, pu_vy
    pu_x = 500
    pu_y = 0
    pu_vx = 0
    pu_vy = 20


def puck():
    global pu_x, pu_y, pu_vx, pu_vy
    r = 20  # 碟盤的半徑
    pu_x += pu_vx
    pu_y += pu_vy
    if pu_y < r and pu_vy < 0:
        pu_vy = -pu_vy
    if pu_y > 600 - r and pu_vy > 0:
        pu_vy = -pu_vy
    if pu_x < r and pu_vx < 0:
        pu_vx = -pu_vx
    if pu_x > 1000 - r and pu_vx > 0:
        pu_vx = -pu_vx
    if pu_y < 0:
        pu_y = 0
    if pu_y > 600:
        pu_y = 600
    if pu_x < 0:
        pu_x = 0
    if pu_x > 1000:
        pu_x = 1000
    pu_vx = pu_vx * 0.95
    pu_vy = pu_vy * 0.95
    if get_dis(pu_x, pu_y, you_x, you_y) < 50 * 50:
        pu_vx = you_vx * 1.2
        pu_vy = you_vy * 1.2
    if get_dis(pu_x, pu_y, com_x, com_y) < 50 * 50:
        pu_vx = com_vx * 1.2
        pu_vy = com_vy * 1.2


def get_dis(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def judge():
    global point_you, point_com
    if pu_x < 20 and 200 < pu_y and pu_y < 400:
        point_you += 1
        goal[0] = 60
        return True
    if pu_x > 980 and 200 < pu_y and pu_y < 400:
        point_com += 1
        goal[1] = 60
        return True
    return False


def main():
    global mc, proc, tmr, level, point_you, point_com
    tmr += 1
    draw_table()
    if proc == 0 and mc == 1:  # 標題畫面
        mc = 0
        level = 0
        if mx > 500:
            level = 1
        point_you = 0
        point_com = 0
        puck_comeout()
        proc = 1
    if proc == 1:  # 遊戲進行中
        puck()
        smasher_you()
        smasher_com()
        if judge() == True:
            puck_comeout()
            if point_you == POINT_WIN or point_com == POINT_WIN:
                proc = 2
                tmr = 0
    if proc == 2 and tmr == 100:  # 勝負結果
        mc = 0
        proc = 0
    root.after(33, main)


root = tkinter.Tk()
img_title = tkinter.PhotoImage(file="title.png")
img_table = tkinter.PhotoImage(file="table.png")
img_puck = tkinter.PhotoImage(file="puck.png")
img_sma_r = tkinter.PhotoImage(file="smasher_r.png")
img_sma_b = tkinter.PhotoImage(file="smasher_b.png")
root.title("Python☆冰上曲棍球")
root.resizable(False, False)
root.bind("<Button>", click)
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=1000, height=600, bg="black")
cvs.pack()
main()
root.mainloop()
