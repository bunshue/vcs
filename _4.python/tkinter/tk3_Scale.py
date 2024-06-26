import sys
import time
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 1")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

slider = tk.Scale(window, from_=0, to=10)
slider.pack()

label = tk.Label(window)
label.pack()

# slider.set(clicks)
# label.config(text="Time: " + str(score))

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

slider = tk.Scale(window, from_=0, to=100)
slider.pack()

slider = tk.Scale(window, from_=0, to=100, resolution=0.1)
slider.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

slider = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL)
slider.pack()
print(slider.get())

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    window,
    command=lambda value: progress.stop(),
    from_=0,
    to=25,
    length=300,
    orient="horizontal",
    variable=scale_float,
)
scale.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

progress = ttk.Progressbar(
    window,
    variable=scale_float,
    maximum=25,
    orient="horizontal",
    mode="indeterminate",
    length=400,
)
progress.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

# progress.start(1000)

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=5)
scrolled_text.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar
exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, orient="vertical", variable=exercise_int)
exercise_progress.pack()
exercise_progress.start()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

label = ttk.Label(window, textvariable=exercise_int)
label.pack()

exercise_scale = ttk.Scale(window, variable=exercise_int, from_=0, to=100)
exercise_scale.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def fnRead():
    n = str(sclNum.get())
    print(n)


print("讀數值")

sclNum = tk.Scale(window, label="數值：", orient="horizontal", from_=1, to=99, length=200)
sclNum.pack(pady=10)
btnRead = tk.Button(window, text=" 確定 ", command=fnRead)
btnRead.pack(pady=20)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("調色盤")
# palette.py


def fnBg(e):
    red = r.get()  # 用get()方法讀取刻度值
    green = g.get()
    blue = b.get()
    color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    frmColor.config(bg=color)


window = tk.Tk()
window.geometry("250x200")
window.title("調色盤")

frmColor = tk.Frame(
    window, width=100, height=180, relief="raised", borderwidth=3, bg="white"
)
frmColor.pack(side="left", padx=10)
frmRGB = tk.Frame(window, width=200, height=200)
frmRGB.pack(side="left")
r = tk.IntVar()
sclR = tk.Scale(
    frmRGB, label="紅：", orient="horizontal", variable=r, from_=0, to=255, command=fnBg
)
r.set(255)  # 用set()方法設定刻度值
sclR.pack()
g = tk.IntVar()
sclG = tk.Scale(
    frmRGB, label="綠：", orient="horizontal", variable=g, from_=0, to=255, command=fnBg
)
sclG.pack()
g.set(255)
b = tk.IntVar()
sclB = tk.Scale(
    frmRGB, label="藍：", orient="horizontal", variable=b, from_=0, to=255, command=fnBg
)
sclB.pack()
b.set(255)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 4")

slider = tk.Scale(
    window,
    from_=0,  # 起點值
    to=10,  # 終點值
    troughcolor="yellow",  # 槽的顏色
    width="30",  # 槽的高度
    tickinterval=2,  # 刻度
    label="My Scale",  # Scale標籤
    length=300,  # Scale長度
    orient=tk.HORIZONTAL,
)  # 水平
slider.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


def get_slider_data2():
    print("垂直捲軸值 = %d, 水平捲軸值 = %d" % (sV.get(), sH.get()))


window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 5")

sV = tk.Scale(window, label="垂直", from_=0, to=10)  # 建立垂直卷軸
sV.set(5)  # 設定垂直卷軸初值是5
sV.pack()

sH = tk.Scale(
    window, label="水平", from_=0, to=10, length=300, orient=tk.HORIZONTAL  # 建立水平卷軸
)
sH.set(3)  # 設定水平捲軸初值是3
sH.pack()

tk.Button(window, text="取得Slider資料2", command=get_slider_data2).pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def get_slider_data1():
    print(slider1.get(), slider2.get())


slider1 = tk.Scale(window, from_=0, to=10)
slider1.pack()
slider2 = tk.Scale(window, from_=0, to=10, length=300, orient=tk.HORIZONTAL)
slider2.set(3)  # 設定水平尺度值
slider2.pack()
tk.Button(window, text="取得Slider資料1", command=get_slider_data1).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

slider1 = tk.Scale(window, from_=0, to=10).pack()
slider2 = tk.Scale(window, from_=0, to=10, length=300, orient=tk.HORIZONTAL).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

slider1 = tk.Scale(window, from_=0, to=10).pack()
slider2 = tk.Scale(window, from_=0, to=10, length=300, orient=tk.HORIZONTAL).pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個


def bgUpdate(source):
    # 更改視窗背景顏色
    red = rSlider.get()  # 讀取red值
    green = gSlider.get()  # 讀取green值
    blue = bSlider.get()  # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))  # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)  # 將顏色轉成16進位字串
    window.config(bg=myColor)  # 設定視窗背景顏色


window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 6")

rSlider = tk.Scale(window, from_=0, to=255, command=bgUpdate)
gSlider = tk.Scale(window, from_=0, to=255, command=bgUpdate)
bSlider = tk.Scale(window, from_=0, to=255, command=bgUpdate)
gSlider.set(125)  # 設定green初值是125
rSlider.grid(row=0, column=0)  # row=0, col=0
gSlider.grid(row=0, column=1)  # row=0, col=1
bSlider.grid(row=0, column=3)  # row=0, col=2

window.mainloop()

print("------------------------------------------------------------")  # 60個


def bgUpdate(source):
    # 更改視窗背景顏色
    red = rSlider.get()  # 讀取red值
    green = gSlider.get()  # 讀取green值
    blue = bSlider.get()  # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))  # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)  # 將顏色轉成16進位字串
    window.config(bg=myColor)  # 設定視窗背景顏色


window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 7")

frame1 = tk.Frame(window)  # 建立框架
frame1.pack()  # 自動安置在上方中央

rSlider = tk.Scale(frame1, from_=0, to=255, command=bgUpdate)
gSlider = tk.Scale(frame1, from_=0, to=255, command=bgUpdate)
bSlider = tk.Scale(frame1, from_=0, to=255, command=bgUpdate)
gSlider.set(125)  # 設定green初值是125
rSlider.grid(row=0, column=0)  # row=0, col=0
gSlider.grid(row=0, column=1)  # row=0, col=1
bSlider.grid(row=0, column=3)  # row=0, col=2

window.mainloop()


print("------------------------------------------------------------")  # 60個


def bgUpdate(source):
    # 更改畫布背景顏色
    red = rSlider.get()  # 讀取red值
    green = gSlider.get()  # 讀取green值
    blue = bSlider.get()  # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))  # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)  # 將顏色轉成16進位字串
    canvas.config(bg=myColor)  # 設定畫布背景顏色


window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 3")

canvas = tk.Canvas(window, width=640, height=240)  # 初始化背景
rSlider = tk.Scale(window, from_=0, to=255, command=bgUpdate)
gSlider = tk.Scale(window, from_=0, to=255, command=bgUpdate)
bSlider = tk.Scale(window, from_=0, to=255, command=bgUpdate)
gSlider.set(125)  # 設定green是125
rSlider.grid(row=1, column=1)  # 第一行第一欄
gSlider.grid(row=1, column=2)  # 第一行第二欄
bSlider.grid(row=1, column=3)  # 第一行第三欄
canvas.grid(row=2, column=1, columnspan=3)  # 第二行全部

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()


def print_selection(v):
    l.config(text="you have selected " + v)


s = tk.Scale(
    window,
    label="try me",
    from_=5,
    to=11,
    orient=tk.HORIZONTAL,
    length=200,
    showvalue=0,
    tickinterval=2,
    resolution=0.01,
    command=print_selection,
)
s.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()  # 實例化一個窗口
window.title("Scale組件")  # 定義窗口標題
window.geometry("400x600")  # 定義窗口大小

l = tk.Label(window, bg="yellow", width=20, height=2, text="未選擇")
l.pack()


def print_selection(V):
    l.config(text="你已選擇" + V)


s = tk.Scale(
    window,
    label="進行選擇",
    from_=5,
    to=11,
    orient=tk.HORIZONTAL,
    length=200,
    showvalue=1,
    tickinterval=3,
    resolution=0.01,
    command=print_selection,
)
s.pack()  # 顯示名字,條方向;長度（像素），是否直接顯示值，標簽的單位長度，保留精度，定義功能

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
