"""

綁定鍵盤滑鼠事件 .bind

"""

import tkinter as tk



print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個



def handler(event, a, b, c):
    # 事件處理函數
    print(event)
    print("handler", a, b, c)


def handlerAdaptor(fun, **kwds):
    # 事件處理函數的適配器，相當于中介，那個event是從那里來的呢，我也納悶，這也許就是python的偉大之處吧
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


window = tk.Tk()

btn = tk.Button(text="按鈕")
# 通過中介函數handlerAdaptor進行事件綁定
btn.bind("<Button-1>", handlerAdaptor(handler, a=1, b=2, c=3))
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個



"""自定義函數"""


def init(data):
    # 數據從run函數中預置寬度和高度
    data.circleSize = min(data.width, data.height) / 10
    data.circleX = data.width / 2
    data.circleY = data.height / 2
    data.charText = ""
    data.keysymText = ""


"""跟蹤并響應鼠標點擊"""


def mousePressed(event, data):
    data.circleX = event.x
    data.circleY = event.y


"""跟蹤和響應按鍵"""


def keyPressed(event, data):
    data.charText = event.char
    data.keysymText = event.keysym


"""通常使用redrawAll繪制圖形"""


def redrawAll(canvas, data):
    canvas.create_oval(
        data.circleX - data.circleSize,
        data.circleY - data.circleSize,
        data.circleX + data.circleSize,
        data.circleY + data.circleSize,
    )
    if data.charText != "":
        canvas.create_text(
            data.width / 10, data.height / 3, text="char: " + data.charText
        )
    if data.keysymText != "":
        canvas.create_text(
            data.width / 10, data.height * 2 / 3, text="keysym: " + data.keysymText
        )


"""按原樣使用run函數"""


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # 設置數據并調用init
    class Struct(object):
        pass

    data = Struct()
    data.width = width
    data.height = height
    window = tk.Tk()
    init(data)
    # 創建根和畫布
    canvas = tk.Canvas(window, width=data.width, height=data.height)
    canvas.pack()
    # 設置事件
    window.bind("<Button-1>", lambda event: mousePressedWrapper(event, canvas, data))
    window.bind("<Key>", lambda event: keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # 然后啟動應用程序
    window.mainloop()  # 塊，直到窗口關閉
    print("bye!")


run(400, 200)

print("------------------------------------------------------------")  # 60個



class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.expr = None

    def initWidgets(self):
        # 創建一個輸入組件
        self.show = tk.Label(
            relief=tk.SUNKEN,
            font=("Courier New", 24),
            width=25,
            bg="white",
            anchor=tk.E,
        )
        # 對該輸入組件使用Pack布局，放在容器頂部
        self.show.pack(side=tk.TOP, pady=10)
        p = tk.Frame(self.master)
        p.pack(side=tk.TOP)
        # 定義字符串的元組
        names = (
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "+",
            "-",
            "*",
            "/",
            ".",
            "=",
        )
        # 遍歷字符串元組
        for i in range(len(names)):
            # 創建Button，將Button放入p組件中
            b = tk.Button(p, text=names[i], font=("Verdana", 20), width=6)
            b.grid(row=i // 4, column=i % 4)
            # 為鼠標左鍵的單擊事件綁定事件處理方法
            b.bind("<Button-1>", self.click)
            # 為鼠標左鍵的雙擊事件綁定事件處理方法
            if b["text"] == "=":
                b.bind("<Double-1>", self.clean)

    def click(self, event):
        # 如果用戶單擊的是數字鍵或點號
        if event.widget["text"] in (
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ".",
        ):
            self.show["text"] = self.show["text"] + event.widget["text"]
        # 如果用戶單擊了運算符
        elif event.widget["text"] in ("+", "-", "*", "/"):
            # 如果當前表達式為None，直接用show組件的內容和運算符進行連接
            if self.expr is None:
                self.expr = self.show["text"] + event.widget["text"]
            # 如果當前表達式不為None，用表達式、show組件的內容和運算符進行連接
            else:
                self.expr = self.expr + self.show["text"] + event.widget["text"]
            self.show["text"] = ""
        elif event.widget["text"] == "=" and self.expr is not None:
            self.expr = self.expr + self.show["text"]
            print(self.expr)
            # 使用eval函數計算表達式的值
            self.show["text"] = str(eval(self.expr))
            self.expr = None

    # 雙擊=按鈕時，程序清空計算結果、將表達式設為None
    def clean(self, event):
        self.expr = None
        self.show["text"] = ""


window = tk.Tk()
window.title("計算器")
App(window)
window.mainloop()

print("------------------------------------------------------------")  # 60個



class mybutton:  # 定義按鈕類
    # 類初始化canvas1，label1是MyCanvals，mylabel的實例，因此可以使用類中的方法
    def __init__(self, root, canvas1, label1, type):
        self.root = root  # 保存引用值
        self.canvas1 = canvas1
        self.label1 = label1
        if type == 0:  # 根據類型創建按鈕
            button = tk.Button(root, text="畫線", command=self.DrawLine)
        elif type == 1:
            button = tk.Button(root, text="畫扇形", command=self.DrawArc)
        elif type == 2:
            button = tk.Button(root, text="畫矩形", command=self.DrawRec)
        else:
            button = tk.Button(root, text="畫橢圓", command=self.DrawOval)
        button.pack(side="left")

    def DrawLine(self):  # DrawLine按鈕事件處理函數
        self.label1.text.set("畫直線")
        self.canvas1.SetStatus(0)  # 把status賦值，便于根據status的值進行畫圖

    def DrawArc(self):
        self.label1.text.set("畫弧")
        self.canvas1.SetStatus(1)

    def DrawRec(self):
        self.label1.text.set("畫矩形")
        self.canvas1.SetStatus(2)

    def DrawOval(self):
        self.label1.text.set("畫橢圓")
        self.canvas1.SetStatus(3)


class MyCanvals:
    def __init__(self, root):
        self.status = 0
        self.draw = 0
        self.root = root
        self.canvas = tk.Canvas(root, bg="yellow", width=600, height=480)  # 生成canvas組件
        self.canvas.pack()
        self.canvas.bind("<ButtonRelease-1>", self.Draw)  # 綁定事件到左鍵
        self.canvas.bind("<Button-2>", self.Exit)  # 綁定事件到中鍵
        self.canvas.bind("<Button-3>", self.Del)  # 綁定事件到右鍵
        self.canvas.bind_all("<Delete>", self.Del)  # 綁定事件到delete鍵
        self.canvas.bind_all("<KeyPress-d>", self.Del)  # 綁定事件到d鍵
        self.canvas.bind_all("<KeyPress-e>", self.Exit)  # 綁定事件到e鍵

    def Draw(self, event):  # 繪圖事件處理函數
        if self.draw == 0:  # 判斷是否繪圖，先記錄起始位置
            self.x = event.x
            self.y = event.y
            self.draw = 1
        else:  # 根據self.status繪制不同的圖形
            if self.status == 0:
                self.canvas.create_line(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 1:
                self.canvas.create_arc(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 2:
                self.canvas.create_rectangle(self.x, self.y, event.x, event.y)
                self.draw = 0
            else:
                self.canvas.create_oval(self.x, self.y, event.x, event.y)
                self.draw = 0

    def Del(self, event):  # 按下右鍵或者d鍵刪除圖形
        items = self.canvas.find_all()
        for i in items:
            self.canvas.delete(i)

    def Exit(self, event):  # 按下中鍵或者e鍵退出
        self.root.quit()

    def SetStatus(self, status):  # 設置繪制的圖形
        self.status = status


class mylabel:  # 定義標簽類
    def __init__(self, root):
        self.root = root
        self.canvas1 = canvas1
        self.text = tk.StringVar()  # 生成標簽引用變量
        self.text.set("畫線")
        self.label = tk.Label(root, textvariable=self.text, fg="blue", width=50)  # 生成標簽
        self.label.pack(side="left")


window = tk.Tk()

canvas1 = MyCanvals(window)  # 生成實例
label1 = mylabel(window)  # 生成實例
mybutton(window, canvas1, label1, 0)
mybutton(window, canvas1, label1, 1)
mybutton(window, canvas1, label1, 2)
mybutton(window, canvas1, label1, 3)

window.mainloop()

print("------------------------------------------------------------")  # 60個



from tkinter import messagebox
import threading

GAME_WIDTH = 450
GAME_HEIGHT = 650
BOARD_X = 220
BOARD_Y = 600
BOARD_WIDTH = 80
BALL_RADIUS = 9


class App:
    def __init__(self, master):
        self.master = master
        # 記錄小球動畫的第幾幀
        self.ball_index = 0
        # 記錄游戲是否失敗的旗標
        self.is_lose = False
        # 初始化記錄小球位置的變量
        self.curx = 260
        self.cury = 30
        self.boardx = BOARD_X
        self.init_widgets()
        self.vx = random.randint(3, 6)  # x方向的速度
        self.vy = random.randint(5, 10)  # y方向的速度
        # 通過定時器指定0.1秒之后執行moveball函數
        self.t = threading.Timer(0.1, self.moveball)
        self.t.start()

    # 創建界面組件
    def init_widgets(self):
        self.cv = tk.Canvas(
            root, background="white", width=GAME_WIDTH, height=GAME_HEIGHT
        )
        self.cv.pack()
        # 讓畫布得到焦點，從而可以響應按鍵事件
        self.cv.focus_set()
        self.cv.bms = []
        # 初始化小球的動畫幀
        for i in range(8):
            self.cv.bms.append(PhotoImage(file="images/ball_" + str(i + 1) + ".gif"))
        # 繪制小球
        self.ball = self.cv.create_image(
            self.curx, self.cury, image=self.cv.bms[self.ball_index]
        )
        self.board = self.cv.create_rectangle(
            BOARD_X,
            BOARD_Y,
            BOARD_X + BOARD_WIDTH,
            BOARD_Y + 20,
            width=0,
            fill="lightblue",
        )
        # 為向左箭頭按鍵綁定事件，擋板左移
        self.cv.bind("<Left>", self.move_left)
        # 為向右箭頭按鍵綁定事件，擋板右移
        self.cv.bind("<Right>", self.move_right)

    def move_left(self, event):
        if self.boardx <= 0:
            return
        self.boardx -= 5
        self.cv.coords(
            self.board, self.boardx, BOARD_Y, self.boardx + BOARD_WIDTH, BOARD_Y + 20
        )

    def move_right(self, event):
        if self.boardx + BOARD_WIDTH >= GAME_WIDTH:
            return
        self.boardx += 5
        self.cv.coords(
            self.board, self.boardx, BOARD_Y, self.boardx + BOARD_WIDTH, BOARD_Y + 20
        )

    def moveball(self):
        self.curx += self.vx
        self.cury += self.vy
        # 小球到了右邊墻壁，轉向
        if self.curx + BALL_RADIUS >= GAME_WIDTH:
            self.vx = -self.vx
        # 小球到了左邊墻壁，轉向
        if self.curx - BALL_RADIUS <= 0:
            self.vx = -self.vx
        # 小球到了上邊墻壁，轉向
        if self.cury - BALL_RADIUS <= 0:
            self.vy = -self.vy
        # 小球到了擋板處
        if self.cury + BALL_RADIUS >= BOARD_Y:
            # 如果在擋板范圍內
            if self.boardx <= self.curx <= (self.boardx + BOARD_WIDTH):
                self.vy = -self.vy
            else:
                messagebox.showinfo(title="失敗", message="您已經輸了")
                self.is_lose = True
        self.cv.coords(self.ball, self.curx, self.cury)
        self.ball_index += 1
        self.cv.itemconfig(self.ball, image=self.cv.bms[self.ball_index % 8])
        # 如果游戲還未失敗，讓定時器繼續執行
        if not self.is_lose:
            # 通過定時器指定0.1秒之后執行moveball函數
            self.t = threading.Timer(0.1, self.moveball)
            self.t.start()


window = tk.Tk()
window.title("彈球游戲")
window.geometry("%dx%d" % (GAME_WIDTH, GAME_HEIGHT))
# 禁止改變窗口大小
window.resizable(width=False, height=False)
App(window)
window.mainloop()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個
