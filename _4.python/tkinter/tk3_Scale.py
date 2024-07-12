import sys
import time
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Scale 測試 1")

label_mesg = tk.Label(window, bg="yellow", width=20, height=6, text="未選擇")
label_mesg.pack()

def get_slider_data():
    print(scale1.get())
    print(scale2.get())
    print(scale3.get())
    print(scale4.get())
    mesg = str(scale1.get())+"\n"+str(scale2.get())+"\n"+str(scale3.get())+"\n"+str(scale4.get())
    label_mesg.config(text=mesg)

def scale_event(V):
    mesg = "控件值 :" + V + "\n"
    mesg += str(scale1.get())+"\n"+str(scale2.get())+"\n"+str(scale3.get())+"\n"+str(scale4.get())
    label_mesg.config(text=mesg)

scale1 = tk.Scale(window, label="scale1", orient=tk.HORIZONTAL, from_=0, to=100, length=150, command=scale_event)
scale1.pack()
scale1.set(60)  # 預設值

scale2 = tk.Scale(window, label="scale2", orient=tk.HORIZONTAL, from_=0, to=100, length=150, resolution=0.1, command=scale_event)
scale2.pack()

print("------------------------------------------------------------")  # 60個

scale3 = tk.Scale(
    window,
    label="scale3",
    from_=0,
    to=100,
    troughcolor="yellow",  # 槽的顏色
    width="20",  # 槽的高度
    tickinterval=20,  # 刻度
    length=150,
    orient=tk.HORIZONTAL,
    command=scale_event,
)
scale3.pack()

print("------------------------------------------------------------")  # 60個

scale4 = tk.Scale(
    window,
    label="scale4",
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=150,
    showvalue=1,    #scale旁是否顯示數值
    tickinterval=10, #scale刻度間距
    resolution=20,
    command=scale_event,
)
scale4.pack()  # 顯示名字,條方向;長度（像素），是否直接顯示值，標簽的單位長度，保留精度，定義功能

print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, text="取值", width=8, height=2, command=get_slider_data)
button1.pack(pady=20)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

scale6_value_double = tk.DoubleVar(value=15)
scale6 = ttk.Scale(
    window,
    from_=0,
    to=100,
    length=150,
    orient=tk.HORIZONTAL,
    variable=scale6_value_double,
    command=lambda value: progressbar6.stop(),
)
scale6.pack()

progressbar6 = ttk.Progressbar(
    window,
    variable=scale6_value_double,
    maximum=100,
    orient=tk.HORIZONTAL,
    mode="indeterminate",
    length=150,
)
progressbar6.pack()

# progressbar6.start(1000)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar

scale7_value_int = tk.IntVar()
progressbar7 = ttk.Progressbar(window, orient=tk.HORIZONTAL, variable=scale7_value_int, length=150)
progressbar7.pack()
progressbar7.start()

label7 = ttk.Label(window, textvariable=scale7_value_int)
label7.pack()

scale7 = ttk.Scale(window, from_=0, to=100, variable=scale7_value_int)
scale7.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

def setup_bg_color2(e):
    red = r.get()  # 用get()方法讀取刻度值
    green = g.get()
    blue = b.get()
    color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    frame3.config(bg=color)


window = tk.Tk()
window.geometry("600x800")
window.title("調色盤")
window.title("Scale 測試 更改視窗控件背景顏色")

# LabelFrame 之 大小, 若小於內附控件大小, 則會撐大
w = 10
h = 10
labelframe1 = tk.LabelFrame(window, text="LabelFrame", padx=w, pady=h)
# LabelFrame 之 位置, 相較於目前表單位置
x_st = 0
y_st = 0
labelframe1.pack(padx=x_st, pady=y_st)

frame3 = tk.Frame(labelframe1, width=100, height=180, relief="raised", borderwidth=3, bg="white")
frame3.pack(side="left", padx=10)

frame2 = tk.Frame(labelframe1, width=200, height=200, bg="pink")
frame2.pack(side="left")

r = tk.IntVar()
scale_r = tk.Scale(frame2, label="紅：", orient=tk.HORIZONTAL, variable=r, from_=0, to=255, command=setup_bg_color2)
scale_r.pack()

g = tk.IntVar()
scale_g = tk.Scale(frame2, label="綠：", orient=tk.HORIZONTAL, variable=g, from_=0, to=255, command=setup_bg_color2)
scale_g.pack()

b = tk.IntVar()
scale_b = tk.Scale(frame2, label="藍：", orient=tk.HORIZONTAL, variable=b, from_=0, to=255, command=setup_bg_color2)
scale_b.pack()

r.set(0)  # 預設
g.set(255)  # 預設
b.set(255)  # 預設

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def setup_bg_color1(source):
    # 更改視窗背景顏色
    red = scale_r.get()  # 讀取red值
    green = scale_g.get()  # 讀取green值
    blue = scale_b.get()  # 讀取blue值
    #print("R=%d, G=%d, B=%d" % (red, green, blue))  # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)  # 將顏色轉成16進位字串
    #window.config(bg=myColor)  # 設定視窗背景顏色
    frame1.config(bg=myColor)  # 設定視窗背景顏色
    canvas1.config(bg=myColor)  # 設定畫布背景顏色

frame1 = tk.Frame(window, width=300, height=100)  # 建立框架
frame1.pack()  # 自動安置在上方中央

canvas1 = tk.Canvas(window, width=300, height=100)  # 初始化背景
canvas1.pack()  # 自動安置在上方中央

frame2 = tk.Frame(window, width=300, height=100)  # 建立框架
#frame2 = tk.Frame(window)  # 建立框架
frame2.pack()  # 自動安置在上方中央

scale_r = tk.Scale(frame2, label="紅", orient=tk.HORIZONTAL, from_=0, to=255, length=150, command=setup_bg_color1)
scale_g = tk.Scale(frame2, label="綠", orient=tk.HORIZONTAL, from_=0, to=255, length=150, command=setup_bg_color1)
scale_b = tk.Scale(frame2, label="藍", orient=tk.HORIZONTAL, from_=0, to=255, length=150, command=setup_bg_color1)
scale_r.pack()
scale_g.pack()
scale_b.pack()

scale_r.set(255)  # 預設值
scale_g.set(0)  # 預設值
scale_b.set(0)  # 預設值

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


