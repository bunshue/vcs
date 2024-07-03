import sys
import time
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 1")

def get_slider_data1():
    print(scale1.get())
    print(scale3.get())
    print(scale4.get())
    print(scale5.get())
    print("垂直捲軸值 = %d, 水平捲軸值 = %d" % (scale_V.get(), scale_H.get()))
    print(scale11.get(), scale12.get())

scale1 = tk.Scale(window, label="scale1", orient=tk.HORIZONTAL, from_=0, to=100, length=150)
scale1.pack()
scale1.set(60)  # 預設值

scale3 = tk.Scale(window, label="scale3", orient=tk.HORIZONTAL, from_=0, to=100, length=150, resolution=0.1)
scale3.pack()

scale4 = tk.Scale(window, label="scale4", orient=tk.HORIZONTAL, from_=0, to=100)
scale4.pack()

scale5 = tk.Scale(window, label="scale5", orient=tk.HORIZONTAL, from_=0, to=100, length=150)
scale5.pack(pady=10)


scale_V = tk.Scale(window, label="垂直", from_=0, to=100)  # 建立垂直卷軸
scale_V.set(5)  # 設定垂直卷軸初值是5
scale_V.pack()

scale_H = tk.Scale(
    window, label="水平", from_=0, to=100, length=150, orient=tk.HORIZONTAL  # 建立水平卷軸
)
scale_H.set(3)  # 設定水平捲軸初值是3
scale_H.pack()



scale11 = tk.Scale(window, from_=0, to=100)
scale11.pack()

scale12 = tk.Scale(window, from_=0, to=100, length=150, orient=tk.HORIZONTAL)
scale12.set(3)  # 設定水平尺度值
scale12.pack()

button1 = tk.Button(window, text="取值", command=get_slider_data1)
button1.pack(pady=20)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個



window.mainloop()

sys.exit()

print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

scale15 = tk.Scale(window, from_=0, to=100).pack()

scale16 = tk.Scale(window, from_=0, to=100, length=150, orient=tk.HORIZONTAL).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 3")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

scale_float = tk.DoubleVar(value=15)
scale5 = ttk.Scale(
    window,
    command=lambda value: progress.stop(),
    from_=0,
    to=100,
    length=150,
    orient=tk.HORIZONTAL,
    variable=scale_float,
)
scale5.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

progress = ttk.Progressbar(
    window,
    variable=scale_float,
    maximum=100,
    orient=tk.HORIZONTAL,
    mode="indeterminate",
    length=150,
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

label5 = ttk.Label(window, textvariable=exercise_int)
label5.pack()

scale6 = ttk.Scale(window, variable=exercise_int, from_=0, to=100)
scale6.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 4")

scale8 = tk.Scale(
    window,
    from_=0,  # 起點值
    to=100,  # 終點值
    troughcolor="yellow",  # 槽的顏色
    width="30",  # 槽的高度
    tickinterval=2,  # 刻度
    label="scale8",  # Scale標籤
    length=150,  # Scale長度
    orient=tk.HORIZONTAL,
)  # 水平
scale8.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, bg="yellow", width=20, text="empty")
label1.pack()


def print_selection1(v):
    label1.config(text="you have selected " + v)


scale17 = tk.Scale(
    window,
    label="try me",
    from_=5,
    to=11,
    orient=tk.HORIZONTAL,
    length=150,
    showvalue=0,
    tickinterval=2,
    resolution=0.01,
    command=print_selection1,
)
scale17.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


label2 = tk.Label(window, bg="yellow", width=20, height=2, text="未選擇")
label2.pack()


def print_selection2(V):
    label2.config(text="你已選擇" + V)

scale18 = tk.Scale(
    window,
    label="scale18",
    from_=5,
    to=11,
    orient=tk.HORIZONTAL,
    length=150,
    showvalue=1,
    tickinterval=3,
    resolution=0.01,
    command=print_selection2,
)
scale18.pack()  # 顯示名字,條方向;長度（像素），是否直接顯示值，標簽的單位長度，保留精度，定義功能

window.mainloop()

print("------------------------------------------------------------")  # 60個

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
scale_R = tk.Scale(
    frmRGB, label="紅：", orient=tk.HORIZONTAL, variable=r, from_=0, to=255, command=fnBg
)
r.set(255)  # 用set()方法設定刻度值
scale_R.pack()

g = tk.IntVar()
scale_G = tk.Scale(
    frmRGB, label="綠：", orient=tk.HORIZONTAL, variable=g, from_=0, to=255, command=fnBg
)
scale_G.pack()
g.set(255)

b = tk.IntVar()
scale_B = tk.Scale(
    frmRGB, label="藍：", orient=tk.HORIZONTAL, variable=b, from_=0, to=255, command=fnBg
)
scale_B.pack()
b.set(255)

window.mainloop()

print("------------------------------------------------------------")  # 60個

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
window.title("Scale 測試 更改視窗背景顏色 1")


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
window.title("Scale 測試 更改視窗背景顏色 2")

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
window.title("Scale 測試 更改視窗背景顏色 3")

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



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


