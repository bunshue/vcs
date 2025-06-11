# The Python Imaging Library

try:
    from tkinter import Tk, Canvas, NW
except ImportError:
    from Tkinter import Tk, Canvas, NW

from PIL import Image, ImageTk
import sys

# painter widget


class PaintCanvas(Canvas):
    def __init__(self, master, image):
        Canvas.__init__(self, master, width=image.size[0], height=image.size[1])

        # fill the canvas
        self.tile = {}
        self.tilesize = tilesize = 32
        xsize, ysize = image.size
        for x in range(0, xsize, tilesize):
            for y in range(0, ysize, tilesize):
                box = x, y, min(xsize, x + tilesize), min(ysize, y + tilesize)
                tile = ImageTk.PhotoImage(image.crop(box))
                self.create_image(x, y, image=tile, anchor=NW)
                self.tile[(x, y)] = box, tile

        self.image = image

        self.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        xy = event.x - 10, event.y - 10, event.x + 10, event.y + 10
        im = self.image.crop(xy)

        # process the image in some fashion
        im = im.convert("L")  # 轉換成灰階圖像

        self.image.paste(im, xy)
        self.repair(xy)

    def repair(self, box):
        # update canvas
        dx = box[0] % self.tilesize
        dy = box[1] % self.tilesize
        for x in range(box[0] - dx, box[2] + 1, self.tilesize):
            for y in range(box[1] - dy, box[3] + 1, self.tilesize):
                try:
                    xy, tile = self.tile[(x, y)]
                    tile.paste(self.image.crop(xy))
                except KeyError:
                    pass  # outside the image
        self.update_idletasks()


window = Tk()
filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
im = Image.open(filename)
if im.mode != "RGB":
    print("圖片非RGB模式, 要轉成RGB格式")
    im = im.convert("RGB")  # 轉換成RGB圖像

PaintCanvas(window, im).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk


class MyButton:  # 定義按鈕類別
    def __init__(self, root, canvas, label, type):  # 類別起始化
        self.root = root  # 儲存參考值
        self.canvas = canvas
        self.label = label
        if type == 0:  # 根據型態建立按鈕
            button = tk.Button(root, text="DrawLine", command=self.DrawLine)
        elif type == 1:
            button = tk.Button(root, text="DrawArc", command=self.DrawArc)
        elif type == 2:
            button = tk.Button(root, text="DrawRec", command=self.DrawRec)
        else:
            button = tk.Button(root, text="DrawOval", command=self.DrawOval)
        button.pack(side="left")

    def DrawLine(self):  # DrawLine按鈕事件處理函數
        self.label.text.set("Draw Line")
        self.canvas.SetStatus(0)

    def DrawArc(self):  # DrawArc按鈕事件處理函數
        self.label.text.set("Draw Arc")
        self.canvas.SetStatus(1)

    def DrawRec(self):  # DrawRec按鈕事件處理函數
        self.label.text.set("Draw Rectangle")
        self.canvas.SetStatus(2)

    def DrawOval(self):  # DrawOval按鈕事件處理函數
        self.label.text.set("Draw Oval")
        self.canvas.SetStatus(3)


class MyCanvas:  # 定義Canvas類別
    def __init__(self, root):
        self.status = 0  # 儲存參考值
        self.draw = 0
        self.root = root
        self.canvas = tk.Canvas(root, bg="white", width=600, height=480)  # 產生Canvas元件
        self.canvas.pack()
        self.canvas.bind("<ButtonRelease-1>", self.Draw)  # 綁定事件到左鍵
        self.canvas.bind("<Button-2>", self.Exit)  # 綁定事件到中鍵
        self.canvas.bind("<Button-3>", self.Del)  # 綁定事件到右鍵
        self.canvas.bind_all("<Delete>", self.Del)  # 綁定事件到Delete鍵
        self.canvas.bind_all("<KeyPress-d>", self.Del)  # 綁定事件到d鍵
        self.canvas.bind_all("<KeyPress-e>", self.Exit)  # 綁定事件到e鍵

    def Draw(self, event):  # 繪圖事件處理函數
        if self.draw == 0:  # 判斷是否繪圖
            self.x = event.x
            self.y = event.y
            self.draw = 1
        else:  # 根據self.status繪制不同圖形
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

    def Del(self, event):  # 當按下右鍵或d鍵則移除圖形
        items = self.canvas.find_all()
        for item in items:
            self.canvas.delete(item)

    def Exit(self, event):  # 當按下中鍵或e鍵則離開
        self.root.quit()

    def SetStatus(self, status):  # 設定繪制的圖形
        self.status = status


class MyLabel:  # 定義標簽類別
    def __init__(self, root):  # 類別起始化
        self.root = root  # 儲存參考
        self.canvas = canvas
        self.text = tk.StringVar()  # 產生標簽參考變數
        self.text.set("Draw Line")
        self.label = tk.Label(root, textvariable=self.text, fg="red", width=50)  # 產生標簽
        self.label.pack(side="left")


root = tk.Tk()  # 產生主視窗
canvas = MyCanvas(root)  # 產生繪圖元件
label = MyLabel(root)  # 產生標簽
MyButton(root, canvas, label, 0)  # 產生按鈕
MyButton(root, canvas, label, 1)
MyButton(root, canvas, label, 2)
MyButton(root, canvas, label, 3)

root.mainloop()  # 進入訊息循環


print("------------------------------------------------------------")  # 60個
