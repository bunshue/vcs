"""
PhotoImage


可能有圖片 目前還不能搬走


"""

import sys

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

print("------------------------------------------------------------")  # 60個
'''
filename = "image/chicken4.jpg"

window = tk.Tk()
window.geometry("600x800")
window.title("ImageTk tk顯示圖片 在label上 1")

poem_text = """
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""

filename = "image/chicken4.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

# PIL影像 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(image)
tk.Label(window, image=tk_image1).pack()

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

#無字
tk.Label(window, image=tk_image).pack()

#圖在左
tk.Label(window, text=poem_text, image=tk_image, bg="lightpink", compound="left").pack()

#圖在右
tk.Label(window, text=poem_text, image=tk_image, bg="lightpink",justify="left",compound="right").pack()

#圖在中
tk.Label(window, text=poem_text, image=tk_image, bg="lightpink", compound="center").pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個



filename = "C:/_git/vcs/_4.python/_data/python-logo.png"

# 檔案 => ImageTk影像
tk_image2 = ImageTk.PhotoImage(file=filename)
tk.Label(window, image=tk_image2).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("ImageTk tk顯示圖片 在label上 2")

print("------------------------------------------------------------")  # 60個

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

msg = "庭院深深深幾許，楊柳堆煙，簾幕無重數。"
tk.Label(window, image=tk_image, text=msg, compound=tk.BOTTOM).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("600x800")
window.title("ImageTk tk顯示圖片 在label上 3")

filename = "C:/_git/vcs/_4.python/_data/tigers.jpg"

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

# 標籤載入圖片
tk.Label(window, image=tk_image).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 標籤載入圖片 + 邊框處理
tk.Label(window, image=tk_image, relief="sunken", bd=5, width=320, height=200).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/tigers.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

W, H = image.size
print(W)
print(H)

# Image影像 => ImageTk影像
tk_image2 = ImageTk.PhotoImage(image)  # 轉換為 tk 圖片物件

tk.Label(window, image=tk_image2, width=300//2, height=180//2).pack()#裁剪正中一塊

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 檔案 => ImageTk影像
tk_image3 = ImageTk.PhotoImage(file=filename)

tk.Label(window, image=tk_image3).pack()

print("tk 顯示圖片 在 label 上")
filename = "C:/_git/vcs/_4.python/_data/tigers.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

# PIL影像 => ImageTk影像
image = ImageTk.PhotoImage(image)

label1 = tk.Label(image=image)
label1.image = image
label1.pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("ImageTk tk顯示圖片 在 Text 上")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

# PIL影像 => ImageTk影像
tk_image = ImageTk.PhotoImage(image)

text1 = tk.Text(window, bg = 'pink', width=100, height=40)
text1.pack()

text1.image_create(tk.END, image=tk_image)
text1.insert(tk.END, "\n")
text1.insert(tk.END, "庭院深深深幾許\n")
text1.insert(tk.END, "楊柳堆煙\n")
text1.insert(tk.END, "簾幕無重數\n")

window.mainloop()

print("------------------------------------------------------------")  # 60個

import customtkinter as ctk

def stretch_image(event):
    global resized_tk

    # size
    width = event.width
    height = event.height

    # create an image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on the canvas
    canvas.create_image(0, 0, image=resized_tk, anchor="nw")


def fill_image(event):
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # get coordinates
    if canvas_ratio > image_ratio:  # canvas is wider than the image
        width = int(event.width)
        height = int(width / image_ratio)
    else:  # canvas is narrower than the image
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event.width / 2), int(event.height / 2), anchor="center", image=resized_tk
    )


def show_full_image(event):
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # get coordinates
    if canvas_ratio > image_ratio:  # canvas is wider than the image
        height = int(event.height)
        width = int(height * image_ratio)
    else:  # canvas is narrower than the image
        width = int(event.width)
        height = int(width / image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event.width / 2), int(event.height / 2), anchor="center", image=resized_tk
    )


# exercise:
# create a third scaling behaviour to always show the full image without cutting off parts

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("ImageTk 24")

# grid layout
window.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
window.rowconfigure(0, weight=1)

filename = "__new/raccoon.jpg"

# 檔案 => PIL影像
image_original = Image.open(filename)

image_ratio = image_original.size[0] / image_original.size[1]
print(image_ratio)
image_tk = ImageTk.PhotoImage(image_original)

filename = "__new/python_dark.png"
# 檔案 => PIL影像
python_dark = Image.open(filename).resize((30, 30))

python_dark_tk = ImageTk.PhotoImage(python_dark)

image_ctk = ctk.CTkImage(
    light_image=Image.open("__new/python_dark.png"),
    dark_image=Image.open("__new/python_light.png"),
)

# widget
# label = ttk.Label(window, text = 'raccoon', image = image_tk)
# label.pack()
button_frame = ttk.Frame(window)
button = ttk.Button(
    button_frame, text="   A button", image=python_dark_tk, compound="left"
)
button.pack(pady=10)

button_ctk = ctk.CTkButton(
    button_frame, text="A button", image=image_ctk, compound="left"
)
button_ctk.pack(pady=10)

button_frame.grid(column=0, row=0, sticky="nsew")

# canvas -> image
canvas = tk.Canvas(
    window, background="black", bd=0, highlightthickness=0, relief="ridge"
)
canvas.grid(column=1, columnspan=3, row=0, sticky="nsew")

canvas.bind("<Configure>", show_full_image)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 25")

ttk.Style().configure("Treeview", rowheight=35)  # 格式化擴充row高度

info = ["鳳凰新聞App可以獲得中國各地最新消息", "瑞士國家鐵路App提供全瑞士火車時刻表", "可口可樂App是一個娛樂的軟件"]

filename1 = "__new/news.jpg"
filename2 = "__new/sbb.jpg"
filename3 = "__new/coca.jpg"

# 檔案 => PIL影像
image1 = Image.open(filename1)  # 插入鳳凰新聞App圖示
image2 = Image.open(filename2)  # 插入瑞士國家鐵路App圖示
image3 = Image.open(filename3)  # 插入可口可樂App圖示

tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)
tk_image3 = ImageTk.PhotoImage(image3)

treeview1 = ttk.Treeview(window, columns=("說明"))
treeview1.heading("#0", text="App")  # 圖標欄位icon column
treeview1.heading("#1", text="功能說明")
treeview1.column("#1", width=300)  # 格式化欄標題
treeview1.insert("", index=tk.END, text="鳳凰新聞", image=tk_image1, values=info[0])
treeview1.insert("", index=tk.END, text="瑞士鐵路", image=tk_image2, values=info[1])
treeview1.insert("", index=tk.END, text="可口可樂", image=tk_image3, values=info[2])
treeview1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""

print("全圖640X480, 每160X160裁一塊出來")
W = 640
H = 480
w = 160
h = 160

for(y = 0; y < H; y += h)
  for(x = 0; x < W; x += w)

for y in range(0, H, h):
    for x in range(0, W, w):
        box = x, y, min(W, x + w), min(H, y + h)
        print(box)
        # tile = ImageTk.PhotoImage(image.crop(box))
        # canvas.create_image(x, y, image = tile, anchor = NW)
        # print(x, y)
        # print(box)





"""
"""
import tkinter.font
default_font = tkinter.font.nametofont('TkDefaultFont')
default_font.configure(size=15)
#然後沒用到
"""


print("------------------------------------------------------------")  # 60個


""" 缺檔案
def more():
    if variable_int.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        print("cattle的簡介 :", str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        print("deer的簡介 :", str2)
    
lb=tk.Label(window,text="請點選想了解的動物簡介:").pack()
variable_int.set(0)  # 預設選項
pic1=ImageTk.PhotoImage(file="image/cattle.gif")
pic2=ImageTk.PhotoImage(file="image/deer.gif")
tk.Radiobutton(window,image=pic1,variable=variable_int,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=variable_int,value=1).pack()
tk.Button(window,text="進一步了解", command=more).pack()
"""

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x800")
window.title("ImageTk tk顯示圖片 在 button 上 1")

filename = "C:/_git/vcs/_4.python/_data/python-logo.png"

# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file=filename)

tk.Button(window, image=tk_image1).pack()

tk.mainloop()
'''
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x900")
window.title("ImageTk tk顯示圖片 在 button 上 2")

filename = "image/chicken4.jpg"

# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file=filename)
tk_image2 = tk_image1
tk_image3 = tk_image1
tk_image4 = tk_image1
tk_image5 = tk_image1

tk.Button(window, image=tk_image1).pack()
tk.Button(window, image=tk_image2, text="按鈕, 圖在上", compound=tk.TOP).pack()
tk.Button(window, image=tk_image3, text="按鈕, 圖在中", compound=tk.CENTER).pack()
tk.Button(window, image=tk_image4, text="按鈕, 圖在左", compound=tk.LEFT).pack()

# 含影像的按鈕  # star外形
tk.Button(window, image=tk_image5, cursor="star").pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x900")
window.title("將圖片貼在 Canvas 上")

filename = "C:/_git/vcs/_4.python/_data/tigers.jpg"

# 檔案 => PIL影像
image0 = Image.open(filename)

# PIL影像 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(image0)

canvas1 = tk.Canvas(window, width=image0.size[0] + 40, height=image0.size[1] + 30)
canvas1.create_image(50, 50, anchor=tk.NW, image=tk_image1)
canvas1.pack(fill=tk.BOTH, expand=True)

"""
print("------------------------------------------------------------")  # 60個

#使用 canvas 顯示圖片 全部 與 部分 jpg


window = tk.Tk()
window.geometry("600x800")
window.title("Canvas 測試 3 使用 canvas 顯示圖片 全部 與 部分")
window.title("ImageTk 30")
"""

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

width = 700
height = 700
canvas1 = tk.Canvas(window, bg="pink", width=width, height=height)
canvas1.pack()

# create_image 繪製影像
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/train.gif'

# 檔案 => PIL影像
image1 = Image.open(filename)

image2 = ImageTk.PhotoImage(image1)

# 將全圖顯示在某處1
x_st = 0
y_st = 0
canvas1.create_image(x_st, y_st, anchor=tk.NW, image=image2)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
image3 = Image.open(filename)
if image3.mode != "RGB":
    print("圖片非RGB模式, 要轉成RGB格式")
    image3 = image3.convert("RGB")  # 轉換成RGB圖像
image4 = ImageTk.PhotoImage(image3)

# 將全圖顯示在某處2
x_st = 250
y_st = 250
canvas1.create_image(x_st, y_st, anchor=tk.NW, image=image4)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

if image.mode != "RGB":
    print("圖片非RGB模式, 要轉成RGB格式")
    image = image.convert("RGB")  # 轉換成RGB圖像

x_st = 50
y_st = 50
w = 100
h = 100
box = x_st, y_st, x_st + w, y_st + h

tile = ImageTk.PhotoImage(image.crop(box))
x = 350
y = 100

canvas1.create_image(x, y, image=tile, anchor=tk.NW)


# 將圖片的一小塊裁出顯示在某處
box = (101, 133, 201, 233)
tile2 = ImageTk.PhotoImage(image.crop(box))

x_st = 50
y_st = 450
canvas1.create_image(x_st, y_st, image=tile2, anchor=tk.NW)

"""
self.bitmap = c.create_bitmap(width//2, height//2,
                bitmap=bitmap,
                foreground='blue')
"""

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x920")
window.title("ImageTk tk顯示圖片 在label上 new")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# 檔案 => PIL影像
image1 = ImageTk.PhotoImage(Image.open(filename))

tk.Label(window, image=image1).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

# 使用 label 顯示圖片 jpg + gif

from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("700x900")
window.title("Label 5")

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_書畫字圖/_peony3/原來奼紫嫣紅開遍.jpg"
# 檔案 => PIL影像
im = Image.open(filename)

"""
#case 1 bitmap image
# bitmap image
image = ImageTk.BitmapImage(im, foreground = "white")
tk.Label(window, image = image, bg = "blue", bd = 0).pack()
"""

# case 2 picture image
# photo image
image = ImageTk.PhotoImage(im)

label1 = tk.Label(window, text="多人圖片", image=image, bd=20, bg="red")
label1.pack()
# tk.Label(window, text = '多人圖片', image = image, bd = 0, bg = 'red', width = 1200).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

print("用 Label 顯示一張圖片")
filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_書畫字圖/_peony3/原來奼紫嫣紅開遍.jpg"

# 檔案 => PIL影像
image2 = Image.open(filename)

image2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(window, image=image2)  # 用Label顯示圖片
label2.image = image
label2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("使用 tk.PhotoImage 只能用 gif")

tk_photoimage1 = tk.PhotoImage(file="__new/ca.gif")
tk_photoimage2 = tk.PhotoImage(file="__new/china.gif")
tk_photoimage3 = tk.PhotoImage(file="__new/left.gif")
tk_photoimage4 = tk.PhotoImage(file="__new/right.gif")
tk_photoimage5 = tk.PhotoImage(file="__new/usIcon.gif")
tk_photoimage6 = tk.PhotoImage(file="__new/ukIcon.gif")
tk_photoimage7 = tk.PhotoImage(file="__new/x.gif")
tk_photoimage8 = tk.PhotoImage(file="__new/o.gif")

print("顯示圖片在 Label 上")
tk.Label(window, image=tk_photoimage1).pack()


filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cloud.gif"
tk_photoimage9 = tk.PhotoImage(file=filename)
tk.Label(window, image=tk_photoimage9, bg="pink").place(
    x=0, y=20, width=150, height=150
)


print("顯示圖片在 Canvas 上")
canvas1 = tk.Canvas(window, bg="pink", width=200, height=10)
canvas1.create_image(90, 50, image=tk_photoimage2)
canvas1["width"] = 200
canvas1["height"] = 100
canvas1.pack()

print("顯示圖片在 Button 上")
tk.Button(window, image=tk_photoimage3).pack()
tk.Button(window, image=tk_photoimage4).pack()

print("顯示圖片在 Checkbutton 上")
tk.Checkbutton(window, image=tk_photoimage5).pack()
tk.Checkbutton(window, image=tk_photoimage6).pack()

print("顯示圖片在 Radiobutton 上")
tk.Radiobutton(window, image=tk_photoimage7).pack()
tk.Radiobutton(window, image=tk_photoimage8).pack()


# 只能用gif
filename = "image/us-map.gif"
tk_photoimage10 = tk.PhotoImage(file=filename)  # gif專用
tk.Label(window, text="Blue", image=tk_photoimage10, bg="blue").pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

# 只能用gif ?

window = tk.Tk()
window.geometry("640x480")
# window.title("ImageTk 34")
window.title("ImageTk tk顯示圖片 在 Text 上")

text2 = tk.Text(window, bg="pink", width=100, height=40)
text2.pack()

tk_photoimage = tk.PhotoImage(file="__new/bg1.gif")


def show():
    # 添加圖片用image_create
    text2.image_create(tk.END, image=tk_photoimage)


button1 = tk.Button(text2, text="點我點我", command=show)
# 添加插件用window_create
text2.window_create(tk.INSERT, window=button1)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# 只能用png ?

filename1 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work1.png"
filename2 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work2.png"
filename3 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work3.png"
filename4 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work4.png"


def fnSet(image):
    lblPhoto.config(image=image)


window = tk.Tk()
window.geometry("1000x900")
window.title("ImageTk 17")

tk_photoimage1 = tk.PhotoImage(file=filename1)
tk_photoimage2 = tk.PhotoImage(file=filename2)
tk_photoimage3 = tk.PhotoImage(file=filename3)
tk_photoimage4 = tk.PhotoImage(file=filename4)

tk_photoimage1_s = tk_photoimage1.subsample(4, 4)
tk_photoimage2_s = tk_photoimage2.subsample(4, 4)
tk_photoimage3_s = tk_photoimage3.subsample(4, 4)
tk_photoimage4_s = tk_photoimage4.subsample(4, 4)

lblPhoto = tk.Label(window, image=tk_photoimage1)
lblPhoto.pack()
lfrmSet = tk.LabelFrame(window, text="選擇照片", relief="raised", borderwidth=2)
lfrmSet.pack()

button1 = tk.Button(
    lfrmSet, image=tk_photoimage1_s, command=lambda: fnSet(tk_photoimage1)
)
button1.pack(side="left", padx=5)
button2 = tk.Button(
    lfrmSet, image=tk_photoimage2_s, command=lambda: fnSet(tk_photoimage2)
)
button2.pack(side="left", padx=5)
button3 = tk.Button(
    lfrmSet, image=tk_photoimage3_s, command=lambda: fnSet(tk_photoimage3)
)
button3.pack(side="left", padx=5)
button4 = tk.Button(
    lfrmSet, image=tk_photoimage4_s, command=lambda: fnSet(tk_photoimage4)
)
button4.pack(side="left", padx=5)

window.mainloop()

print("------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x900")
window.title("ImageTk 35")

canvas1 = tk.Canvas(window, bg="pink", height=150, width=500)
canvas1.pack()

tk_photoimage1 = tk.PhotoImage(file="__new/bg1.gif")
image = canvas1.create_image(0, 0, anchor="nw", image=tk_photoimage1)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

canvas2 = tk.Canvas(window, bg="blue", height=300, width=300)
canvas2.pack()

tk_photoimage2 = tk.PhotoImage(file="__new/bg1.gif")
image = canvas2.create_image(10, 10, anchor="nw", image=tk_photoimage2)

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas2.create_line(x0, y0, x1, y1)
oval = canvas2.create_oval(x0, y0, x1, y1, fill="red")
arc = canvas2.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas2.create_rectangle(100, 30, 100 + 20, 30 + 20)


def moveit():
    canvas2.move(rect, 0, 2)


tk.Button(window, text="move", command=moveit).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/python-logo.png"
tk_photoimage3 = tk.PhotoImage(file=filename)
print("W = ", tk_photoimage3.width())
print("H = ", tk_photoimage3.height())

"""
print('影像放大 zoom, 寬高, 整數倍')
tk_photoimage3 = tk_photoimage3.zoom(2, 1)

print('影像縮小 subsample, 寬高, 整數倍')
tk_photoimage3 = tk_photoimage3.subsample(2, 1)
"""
# tk_photoimage3.blank()#移除圖片元件tk_photoimage3的影像

canvas3 = tk.Canvas(window, width=600, height=250, bg="pink")  # 整個畫布
canvas3.create_image(256, 100, image=tk_photoimage3)
canvas3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

import random


# Choose four random cards
def shuffle():
    random.shuffle(imageList)
    for i in range(4):
        labelList[i]["image"] = imageList[i]


imageList = []  # Store images for cards
for i in range(1, 53):
    imageList.append(
        tk.PhotoImage(
            file="C:/_git/vcs/_1.data/______test_files1/__pic/_poker_card/card/"
            + str(i)
            + ".gif"
        )
    )

frame = tk.Frame(window)  # Hold four labels for cards
frame.pack()

labelList = []  # A list of four labels
for i in range(4):
    labelList.append(tk.Label(frame, image=imageList[i]))
    labelList[i].pack(side=tk.LEFT)

tk.Button(window, text="任選四張牌", command=shuffle).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x900")
window.title("ImageTk 37")

print("------------------------------------------------------------")  # 60個

# 使用 canvas 顯示圖片 gif

filename = (
    "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival-2024.gif"
)
tk_photoimage1 = tk.PhotoImage(file=filename)
tk.Label(window, text="Blue", image=tk_photoimage1, bg="gray").pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

filename = (
    "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival-2024.gif"
)
tk_photoimage2 = tk.PhotoImage(file=filename)

x = 90
y = 50
width = 400
height = 200

canvas2 = tk.Canvas(window, width=width, height=height)
canvas2.pack()

canvas2.create_image(x, y, image=tk_photoimage2)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 只能開啟 gif 檔
filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif"

tk_photoimage = tk.PhotoImage(file=filename)  # 使用PhotoImage開啟圖片

canvas2 = tk.Canvas(window, width=600, height=550, bg="pink")
canvas2.pack()

canvas2.create_image(300, 250, image=tk_photoimage)  # 使用create_image將圖片新增到Canvas元件中

window.mainloop()

print("------------------------------------------------------------")  # 60個


"""  準備移出

label1 = tk.Label(window, text=poem_text, bg="lightyellow", padx=10).pack(side="left")
label1 = tk.Label(window, text=poem_text, bg="lightyellow", justify=tk.LEFT, padx=10).pack(side="left")

#text1.pack(fill=tk.BOTH, expand=True)

tk.Label(window, text = "Blue", bg = "blue").pack(fill = tk.BOTH, expand = 1)

tk.Label(window, text = 'AAAAA', bg = 'pink').place(x=0, y=200, width=150, height=50)

tk.Label(window, text='1').pack(side='top')
tk.Label(window, text='1').pack(side='bottom')
tk.Label(window, text='1').pack(side='left')
tk.Label(window, text='1').pack(side='right')


"""
