"""
PhotoImage


可能有圖片 目前還不能搬走


"""

import sys
'''
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("ImageTk 12")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
img = Image.open(filename)
# PIL影像 => ImageTk影像
tk_image = ImageTk.PhotoImage(img)

text = tk.Text()
text.image_create(tk.END, image=tk_image)
text.insert(tk.END, "\n")
text.insert(tk.END, "牡丹亭")
text.insert(tk.END, "還魂記")
text.pack(fill=tk.BOTH, expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

window = tk.Tk()
window.geometry("600x800")
window.title("ImageTk 15")

poem_text = """
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

label1 = tk.Label(window, image=tk_image).pack(side="right")
label1 = tk.Label(window, text=poem_text, bg="lightyellow", padx=10).pack(side="left")
label1 = tk.Label(
    window, text=poem_text, bg="lightyellow", justify=tk.LEFT, padx=10
).pack(side="left")
label1 = tk.Label(
    window, text=poem_text, image=tk_image, bg="lightyellow", compound="left"
)
label1 = tk.Label(
    window,
    text=poem_text,
    image=tk_image,
    bg="lightyellow",
    justify="left",
    compound="right",
)
label1 = tk.Label(
    window, text=poem_text, image=tk_image, bg="lightyellow", compound="center"
)

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/python-logo.png"

window = tk.Tk()
window.geometry("600x800")
window.title("ImageTk 16")

print("tk 顯示圖片 在 label 上")

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

the_label = tk.Label(
    window,
    text="LENA",
    justify=tk.LEFT,  # 字符串进行左对齐
    image=tk_image,
    compound=tk.CENTER,  # 混合模式,文字在图片的正上方显示
    font=("方正粗黑宋简体", 24),  # 字体和大小
    fg="red",  # 前景颜色，就是字体颜色
)

the_label.pack()  # 这句不可少呀

window.mainloop()

print("------------------------------------------------------------")  # 60個

# album.py
# 只能用png ?

filename1 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work1.png"
filename2 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work2.png"
filename3 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work3.png"
filename4 = "C:/_git/vcs/_1.data/______test_files1/__pic/_work/work4.png"


def fnSet(img):
    lblPhoto.config(image=img)


window = tk.Tk()
window.geometry("1000x900")
window.title("ImageTk 17")

imgPhoto1 = tk.PhotoImage(file=filename1)
imgPhoto2 = tk.PhotoImage(file=filename2)
imgPhoto3 = tk.PhotoImage(file=filename3)
imgPhoto4 = tk.PhotoImage(file=filename4)

imgPhoto1_s = imgPhoto1.subsample(4, 4)
imgPhoto2_s = imgPhoto2.subsample(4, 4)
imgPhoto3_s = imgPhoto3.subsample(4, 4)
imgPhoto4_s = imgPhoto4.subsample(4, 4)

lblPhoto = tk.Label(window, image=imgPhoto1)
lblPhoto.pack()
lfrmSet = tk.LabelFrame(window, text="選擇照片", relief="raised", borderwidth=2)
lfrmSet.pack()

button1 = tk.Button(lfrmSet, image=imgPhoto1_s, command=lambda: fnSet(imgPhoto1))
button1.pack(side="left", padx=5)
button2 = tk.Button(lfrmSet, image=imgPhoto2_s, command=lambda: fnSet(imgPhoto2))
button2.pack(side="left", padx=5)
button3 = tk.Button(lfrmSet, image=imgPhoto3_s, command=lambda: fnSet(imgPhoto3))
button3.pack(side="left", padx=5)
button4 = tk.Button(lfrmSet, image=imgPhoto4_s, command=lambda: fnSet(imgPhoto4))
button4.pack(side="left", padx=5)

window.mainloop()

print("------------------------------")  # 60個

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

# 檔案 => PIL影像
image_original = Image.open("__new/raccoon.jpg")

image_ratio = image_original.size[0] / image_original.size[1]
print(image_ratio)
image_tk = ImageTk.PhotoImage(image_original)

# 檔案 => PIL影像
python_dark = Image.open("__new/python_dark.png").resize((30, 30))

python_dark_tk = ImageTk.PhotoImage(python_dark)

img_ctk = ctk.CTkImage(
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
    button_frame, text="A button", image=img_ctk, compound="left"
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

#from tkinter.ttk import *

#from tkinter import ttk

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 25")

ttk.Style().configure("Treeview", rowheight=35)  # 格式化擴充row高度

info = ["鳳凰新聞App可以獲得中國各地最新消息", "瑞士國家鐵路App提供全瑞士火車時刻表", "可口可樂App是一個娛樂的軟件"]

# 檔案 => PIL影像
img1 = Image.open("__new/news.jpg")  # 插入鳳凰新聞App圖示
img2 = Image.open("__new/sbb.jpg")  # 插入瑞士國家鐵路App圖示
img3 = Image.open("__new/coca.jpg")  # 插入可口可樂App圖示

tk_image1 = ImageTk.PhotoImage(img1)
tk_image2 = ImageTk.PhotoImage(img2)
tk_image3 = ImageTk.PhotoImage(img3)

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


def printInfo():  # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (entry1.get(), entry2.get()))
    print('清除 entry1 entry2 的資料')
    entry1.delete(0, tk.END)  # 刪除account文字方塊的帳號內容
    entry2.delete(0, tk.END)  # 刪除pwd文字方塊的密碼內容


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 26")

label1 = tk.Label(window, text="Account")  # account標籤
label1.grid(row=1)

label2 = tk.Label(window, text="Password")  # pwd標籤
label2.grid(row=2)

entry1 = tk.Entry(window)  # 文字方塊account
entry2 = tk.Entry(window, show="*")  # 文字方塊pwd
entry1.insert(0, "Kevin")  # 預設Account內容
entry2.insert(0, "pwd")  # 預設pwd內容
entry1.grid(row=1, column=1)  # 定位文字方塊account
entry2.grid(row=2, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
button1 = tk.Button(window, text="Login", command=printInfo)
button1.grid(row=3, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 27")

label1 = tk.Label(window, text="Account")  # account標籤
label1.grid(row=1)

label2 = tk.Label(window, text="Password")  # pwd標籤
label2.grid(row=2)

entry1 = tk.Entry(window)  # 文字方塊account
entry2 = tk.Entry(window, show="*")  # 文字方塊pwd
entry1.insert(1, "Kevin")  # 預設Account內容
entry2.insert(1, "pwd")  # 預設pwd內容
entry1.grid(row=1, column=1)  # 定位文字方塊account
entry2.grid(row=2, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
button1 = tk.Button(window, text="Login", command=printInfo)
button1.grid(row=3, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 28")

# 以下是 LabelFrame 標籤框架
labelframe1 = tk.LabelFrame(window, text="資料驗證")  # 建立標籤框架
labelframe1.pack(padx=10, pady=5, ipadx=5, ipady=5)  # 包裝與定位標籤框架

label1 = tk.Label(labelframe1, text="Account")  # account標籤
label1.grid(row=0, column=0)

label2 = tk.Label(labelframe1, text="Password")  # pwd標籤
label2.grid(row=1, column=0)

entry1 = tk.Entry(labelframe1)  # 文字方塊account
entry1.grid(row=0, column=1)  # 定位文字方塊account
entry2 = tk.Entry(labelframe1, show="*")  # 文字方塊pwd
entry2.grid(row=1, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
button1 = tk.Button(labelframe1, text="Login", command=printInfo)
button1.grid(row=2, column=0, sticky=tk.W, pady=5)

window.mainloop()

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
window.geometry("640x480")
window.title("ImageTk 34")

text1 = tk.Text(window, width=100, height=30)
text1.pack()
photo = tk.PhotoImage(file="__new/bg1.gif")

def show():
    # 添加圖片用image_create
    text1.image_create(tk.END, image=photo)


b1 = tk.Button(text1, text="點我點我", command=show)
# 添加插件用window_create
text1.window_create(tk.INSERT, window=b1)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("200x200")
window.title("ImageTk 35")

canvas = tk.Canvas(window, height=150, width=500)
canvas.grid(row=1, column=1)
image_file = tk.PhotoImage(file="__new/bg1.gif")
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

"""
tk.Label(window, text='1').pack(side='top')
tk.Label(window, text='1').pack(side='bottom')
tk.Label(window, text='1').pack(side='left')
tk.Label(window, text='1').pack(side='right')
"""

for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

tk.Label(window, text=1).place(x=20, y=10, anchor="nw")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 36")

canvas = tk.Canvas(window, bg="blue", height=100, width=200)
image_file = tk.PhotoImage(file="__new/bg1.gif")
image = canvas.create_image(10, 10, anchor="nw", image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill="red")
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
canvas.pack()


def moveit():
    canvas.move(rect, 0, 2)


b = tk.Button(window, text="move", command=moveit).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")
window.title("ImageTk 37")

# Create PhotoImage objects
caImage = tk.PhotoImage(file="__new/ca.gif")
chinaImage = tk.PhotoImage(file="__new/china.gif")
leftImage = tk.PhotoImage(file="__new/left.gif")
rightImage = tk.PhotoImage(file="__new/right.gif")
usImage = tk.PhotoImage(file="__new/usIcon.gif")
ukImage = tk.PhotoImage(file="__new/ukIcon.gif")
crossImage = tk.PhotoImage(file="__new/x.gif")
circleImage = tk.PhotoImage(file="__new/o.gif")

# frame1 to contain label and canvas
frame1 = tk.Frame(window)
frame1.pack()
tk.Label(frame1, image=caImage).pack(side=tk.LEFT)
canvas = tk.Canvas(frame1)
canvas.create_image(90, 50, image=chinaImage)
canvas["width"] = 200
canvas["height"] = 100
canvas.pack(side=tk.LEFT)

# frame2 to contain buttons, check buttons, and radio buttons
frame2 = tk.Frame(window)
frame2.pack()
tk.Button(frame2, image=leftImage).pack(side=tk.LEFT)
tk.Button(frame2, image=rightImage).pack(side=tk.LEFT)

tk.Checkbutton(frame2, image=usImage).pack(side=tk.LEFT)
tk.Checkbutton(frame2, image=ukImage).pack(side=tk.LEFT)

tk.Radiobutton(frame2, image=crossImage).pack(side=tk.LEFT)
tk.Radiobutton(frame2, image=circleImage).pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)  # Logo影像檔

msg = "庭院深深深幾許，楊柳堆煙，簾幕無重數。"
logo = tk.Label(window, image=tk_image, text=msg, compound=tk.BOTTOM)
logo.pack()
logo.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
"""


window = tk.Tk()
window.geometry("600x920")
window.title("ImageTk tk顯示圖片 在label上 1")

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
window.geometry("600x950")
window.title("ImageTk tk顯示圖片 在label上 2")

filename = "C:/_git/vcs/_4.python/_data/tigers.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

# PIL影像 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(image)

tk.Label(window, image=tk_image1).pack()


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/python-logo.png"

# 檔案 => ImageTk影像
tk_image2 = ImageTk.PhotoImage(file=filename)

tk.Label(window, image=tk_image2).pack()


print("------------------------------------------------------------")  # 60個

#只能用gif
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'
   
photo = tk.PhotoImage(file = filename)
tk.Label(window, text = "Blue", image = photo, bg = "blue").pack(fill = tk.BOTH, expand = 1)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x800")
window.title("ImageTk tk顯示圖片 在 button 上 1")

filename = "C:/_git/vcs/_4.python/_data/python-logo.png"

# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file=filename)

tk.Button(window, image=tk_image1).pack()


tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x900")
window.title("ImageTk tk顯示圖片 在 button 上 2")

filename = "C:/_git/vcs/_4.python/_data/tigers.jpg"

# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file=filename)
tk_image2 = tk_image1
tk_image3 = tk_image1
tk_image4 = tk_image1
tk_image5 = tk_image1

tk.Button(window, image=tk_image1).pack()
tk.Button(window, image=tk_image2, text="按鈕", compound=tk.TOP).pack()
tk.Button(window, image=tk_image3, text="按鈕", compound=tk.CENTER).pack()
tk.Button(window, image=tk_image4, text="按鈕", compound=tk.LEFT).pack()

# 含影像的按鈕  # star外形
tk.Button(window, image=tk_image5, cursor="star").pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/tigers.jpg"

window = tk.Tk()
window.geometry("600x900")
window.title("將圖片貼在 Canvas 上")

# 檔案 => PIL影像
image0 = Image.open(filename)
# PIL影像 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(image0)

canvas1 = tk.Canvas(window, width=image0.size[0] + 40, height=image0.size[1] + 30)
canvas1.create_image(50, 50, anchor=tk.NW, image=tk_image1)
canvas1.pack(fill=tk.BOTH, expand=True)


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/python-logo.png"
tk_image2 = tk.PhotoImage(file=filename)
print("W = ", tk_image2.width())
print("H = ", tk_image2.height())

"""
print('影像放大 zoom, 寬高, 整數倍')
tk_image2 = tk_image2.zoom(2, 1)

print('影像縮小 subsample, 寬高, 整數倍')
tk_image2 = tk_image2.subsample(2, 1)
"""
# tk_image2.blank()#移除圖片元件tk_image2的影像

gs = tk.Canvas(window, width=512, height=512)  # 整個畫布
gs.create_image(256, 100, image=tk_image2)
gs.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個



"""
使用 canvas 顯示圖片 gif
"""

window = tk.Tk()
window.geometry("600x800")
#window.title("Canvas 測試 2 Display Image")
window.title("ImageTk 29")

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival-2024.gif"

photo = tk.PhotoImage(file=filename)
tk.Label(window, text="Blue", image=photo, bg="gray").pack(fill=tk.BOTH, expand=1)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival-2024.gif"
caImage = tk.PhotoImage(file=filename)

x = 90
y = 50
width = 400
height = 200

canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()
canvas.create_image(x, y, image=caImage)

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
使用 canvas 顯示圖片 全部 與 部分 jpg
"""

window = tk.Tk()
window.geometry("600x800")
window.title("Canvas 測試 3 使用 canvas 顯示圖片 全部 與 部分")
window.title("ImageTk 30")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

width = 700
height = 700
canvas = tk.Canvas(window, bg="pink", width=width, height=height)
canvas.pack()

# create_image 繪製影像
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/train.gif'

image1 = Image.open(filename)
image2 = ImageTk.PhotoImage(image1)
# image2 = tk.PhotoImage(file = filename)   #gif專用

# 將全圖顯示在某處1
x_st = 0
y_st = 0
canvas.create_image(x_st, y_st, anchor=tk.NW, image=image2)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image3 = Image.open(filename)
if image3.mode != "RGB":
    print("圖片非RGB模式, 要轉成RGB格式")
    image3 = image3.convert("RGB")  # 轉換成RGB圖像
image4 = ImageTk.PhotoImage(image3)

# 將全圖顯示在某處2
x_st = 250
y_st = 250
canvas.create_image(x_st, y_st, anchor=tk.NW, image=image4)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

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

canvas.create_image(x, y, image=tile, anchor=tk.NW)


# 將圖片的一小塊裁出顯示在某處
box = (101, 133, 201, 233)
tile2 = ImageTk.PhotoImage(image.crop(box))

x_st = 50
y_st = 450
canvas.create_image(x_st, y_st, image=tile2, anchor=tk.NW)

"""
self.bitmap = c.create_bitmap(width//2, height//2,
                bitmap=bitmap,
                foreground='blue')
"""

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 31")

#只能開啟 gif 檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

tkimage = tk.PhotoImage(file=filename)# 使用PhotoImage開啟圖片

#canvas = tk.Canvas(window, width = 600, height = 600)
canvas = tk.Canvas(window, width = 600, height = 480, bg = 'white')
canvas.pack()
canvas.create_image(300, 250, image = tkimage)# 使用create_image將圖片新增到Canvas元件中

window.mainloop()

print("------------------------------------------------------------")  # 60個

'''

import tkinter as tk

window = tk.Tk()
window.geometry("600x920")
window.title("ImageTk tk顯示圖片 在label上 new")


from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img = ImageTk.PhotoImage(Image.open(filename))
label1 = tk.Label(window, image=img).pack()


print("Label使用圖片")
filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cloud.gif"
image = tk.PhotoImage(file=filename)
tk.Label(window, image=image).place(x=0, y=150, width=150, height=150)



window.mainloop()

print("------------------------------------------------------------")  # 60個


"""
使用 label 顯示圖片 jpg + gif
"""

from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("700x900")
window.title("Label 5")

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_書畫字圖/_peony3/原來奼紫嫣紅開遍.jpg"
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

image2 = Image.open(filename)
image2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(window, image=image2)  # 用Label顯示圖片
label2.image = image
label2.pack()

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

print("------------------------------------------------------------")  # 60個

