import tkinter
import tkinter.messagebox
import random

score = [0]*3 # 對奕結果
match = 0 # 對奕次數

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 60)
BLACK = 1
WHITE = 2
proc = 0
turn = 0
msg = ""
space = 0
color = [0]*2
board = []
back = []
for y in range(8):
    board.append([0]*8)
    back.append([0]*8)

def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x*80
            Y = y*80
            cvs.create_rectangle(X, Y, X+80, Y+80, outline="black")
            if board[y][x]==BLACK:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="black", width=0)
            if board[y][x]==WHITE:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="white", width=0)
    cvs.update()

def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE

# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break

# 計算在這個位置下棋，對手的棋子會有幾顆翻面
def kaeseru(x, y, iro):
    if board[y][x]>0:
        return -1 # 不能落子的棋格
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    total += k
                    break
    return total

# 確認有沒有可以落子的棋格
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0:
                return True
    return False

# 計算黑棋與白棋各有幾顆
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x]==BLACK: b += 1
            if board[y][x]==WHITE: w += 1
    return b, w

#電腦的思考邏輯
def computer_0(iro): # 隨機落子
    while True:
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        if kaeseru(rx, ry, iro)>0:
            return rx, ry

point = [
    [6,2,5,4,4,5,2,6],
    [2,1,3,3,3,3,1,2],
    [5,3,3,3,3,3,3,5],
    [4,3,3,0,0,3,3,4],
    [4,3,3,0,0,3,3,4],
    [5,3,3,3,3,3,3,5],
    [2,1,3,3,3,3,1,2],
    [6,2,5,4,4,5,2,6]
]
def computer_1(iro): # 選擇該優先落子的棋格
    sx = 0
    sy = 0
    p = 0
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0 and point[y][x]>p:
                    p = point[y][x]
                    sx = x
                    sy = y
    return sx, sy

# 以蒙地卡羅演算法撰寫的思考邏輯
def save():
    for y in range(8):
        for x in range(8):
            back[y][x] = board[y][x]

def load():
    for y in range(8):
        for x in range(8):
            board[y][x] = back[y][x]

def uchiau(iro):
    while True:
        if uteru_masu(BLACK)==False and uteru_masu(WHITE)==False:
            break
        iro = 3-iro
        if uteru_masu(iro)==True:
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if kaeseru(x, y, iro)>0:
                    ishi_utsu(x, y, iro)
                    break

def computer_2(iro, loops):
    global msg
    win = [0]*64
    save()
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0:
                msg += "."
                banmen()
                win[x+y*8] = 1
                for i in range(loops):
                    ishi_utsu(x, y, iro)
                    uchiau(iro)
                    b, w = ishino_kazu()
                    if iro==BLACK and b>w:
                        win[x+y*8] += 1
                    if iro==WHITE and w>b:
                        win[x+y*8] += 1
                    load()
    m = 0
    n = 0
    for i in range(64):
        if win[i]>m:
            m = win[i]
            n = i
    x = n%8
    y = int(n/8)
    return x, y

def main():
    global proc, turn, msg, space, match
    banmen()
    if proc==0: # 標題畫面
        cvs.create_text(320, 200, text="Reversi AUTO", fill="gold", font=FL)
        ban_syokika()
        color[0] = BLACK
        color[1] = WHITE
        turn = 0
        proc = 1
    elif proc==1: # 顯示換誰下棋的訊息
        msg = "演算法 "+str(turn)+" 思考中"
        proc = 2
    elif proc==2: # 決定落子的棋格
        if turn==0: # 演算法 先攻
            cx, cy = computer_1(color[turn])
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
        else: # 演算法 後攻
            cx, cy = computer_2(color[turn], 30)
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
    elif proc==3: # 換邊下棋
        msg = ""
        turn = 1-turn
        proc = 4
    elif proc==4: # 確認有沒有可以落子的棋格
        if space==0:
            proc = 5
        elif uteru_masu(BLACK)==False and uteru_masu(WHITE)==False:
            msg = "雙方皆無處落子，對奕結束"
            proc = 5
        elif uteru_masu(color[turn])==False:
            msg = "COM"+str(turn)+"沒有可落子之處，換邊下棋"
            proc = 3
        else:
            proc = 1
    elif proc==5: # 判斷勝負
        b, w = ishino_kazu()
        if (color[0]==BLACK and b>w) or (color[0]==WHITE and w>b):
            score[0] += 1
        elif (color[1]==BLACK and b>w) or (color[1]==WHITE and w>b):
            score[1] += 1
        else:
            score[2] += 1

        # 顯示結果
        match += 1
        print("--------------------")
        print("對奕次數", match)
        print("黑", b, "　白", w)
        print("COM(先攻) WIN", score[0])
        print("COM(後攻) WIN", score[1])
        print("DRAW", score[2]) 
        if match%100==0:
            tkinter.messagebox.showinfo("", "每對奕100次，程式就暫停執行")
        proc = 0
    root.after(0, main) # 演算法的對戰 將100msec設定為1msec

root = tkinter.Tk()
root.title("黑白棋")
root.resizable(False, False)
cvs = tkinter.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()
