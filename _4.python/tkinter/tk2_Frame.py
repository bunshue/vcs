import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Frame 1")

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


def buttonClick():
    print("click")


print("用Frame做一個toolbar 1")
frame_toolbar1 = tk.Frame(window, relief="raised", borderwidth=1)
frame_toolbar1.pack(side="top", fill="x", padx=2, pady=1)

button1 = tk.Button(frame_toolbar1, text="Function 1", command=buttonClick)
button1.pack(side="left", pady=2)
button2 = tk.Button(frame_toolbar1, text="Function 2", command=buttonClick)
button2.pack(side="left", pady=2)
button3 = tk.Button(frame_toolbar1, text="Function 3", command=buttonClick)
button3.pack(side="left", pady=2)
button4 = tk.Button(frame_toolbar1, text="Function 4", command=buttonClick)
button4.pack(side="left", pady=2)
button5 = tk.Button(frame_toolbar1, text="Function 5", command=buttonClick)
button5.pack(side="left", pady=2)
button6 = tk.Button(frame_toolbar1, text="Function 6", command=buttonClick)
button6.pack(side="left", pady=2)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

print("用Frame做一個toolbar 2")
frame_toolbar2 = tk.Frame(window)
frame_toolbar2.pack(side=tk.TOP, fill=tk.X)

button1 = tk.Button(frame_toolbar2, text="new", width=6, command=buttonClick)
button1.pack(side=tk.LEFT, padx=2, pady=2)
button2 = tk.Button(frame_toolbar2, text="open", width=6, command=buttonClick)
button2.pack(side=tk.LEFT, padx=2, pady=2)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


print("將多個控件做在一個Frame上")

frame2 = tk.Frame(window, bg="yellow")  # 按鈕容器
frame2.pack()
button1 = tk.Button(frame2, text="播放", width=8, command="")
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(frame2, text="暫停", width=8, command="")
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(frame2, text="音量調大", width=8, command="")
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(frame2, text="音量調小", width=8, command="")
button4.grid(row=0, column=3, padx=5, pady=5)
button5 = tk.Button(frame2, text="停止", width=8, command="")
button5.grid(row=0, column=4, padx=5, pady=5)
button6 = tk.Button(frame2, text="結束", width=8, command="")
button6.grid(row=0, column=5, padx=5, pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

"""
width:設置框架寬度，默認值是 0。
height:框架的高度，默認值是 0。
bg:框架背景顏色
bd:框架的大小，默認為 2 個像素
relief:邊框樣式，可選的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默認為 FLAT。
cursor:鼠標移動到框架時，光標的形狀，可以設置為 arrow, circle, cross, plus 等。
highlightbackground:框架沒有獲得焦點時，高亮邊框的顏色，默認由系統指定。
highlightcolor:框架獲得焦點時，高亮邊框的顏色
highlightthickness:指定高亮邊框的寬度，默認值為 0不帶高亮邊框）
takefocus:指定該組件是否接受輸入焦點（用戶可以通過 tab 鍵將焦點轉移上來），默認為 false。
"""

separator = tk.Frame(width=30, height=80, bg="pink", bd=5, relief=tk.GROOVE).pack(
    fill=tk.X, padx=5, pady=5
)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

width = 100
height = 100
frame = tk.Frame(window, bg="pink", width=width, height=height)
frame.pack()
frame = tk.Frame(window, bg="yellow", width=width, height=height)
frame.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("Toolbox 測試")
tk.Button(window, text="OK").pack(side=tk.LEFT)
tk.Button(window, text="Cancel").pack(side=tk.LEFT)
tk.Label(window, text="Enter your name:").pack(side=tk.LEFT)
tk.Entry(window, text="Type Name").pack(side=tk.LEFT)
tk.Checkbutton(window, text="Bold").pack(side=tk.LEFT)
tk.Checkbutton(window, text="Italic").pack(side=tk.LEFT)
tk.Radiobutton(window, text="Red").pack(side=tk.LEFT)
tk.Radiobutton(window, text="Yellow").pack(side=tk.LEFT)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Frame 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

from tkinter.ttk import Frame, Style

for fm in ["red", "green", "blue"]:  # 建立3個不同底色的框架
    tk.Frame(window, bg=fm, height=30, width=250).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

for fm in ["red", "green", "blue"]:  # 建立3個不同底色的框架
    tk.Frame(bg=fm, height=30, width=250).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 用字典儲存框架顏色與游標外形
fms = {"red": "cross", "green": "boat", "blue": "clock"}
for fmColor in fms:  # 建立3個不同底色的框架與游標外形
    tk.Frame(window, bg=fmColor, cursor=fms[fmColor], height=30, width=200).pack(
        side=tk.LEFT
    )


window.mainloop()


print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("600x800")
window.title("Frame 3")


# Add labels and entries to frame1
frame1 = tk.Frame(window, bg="pink")
frame1.pack()

tk.Label(frame1, text="Number 1:").pack(side=tk.LEFT)
string1 = tk.StringVar()
tk.Entry(frame1, width=5, textvariable=string1, justify=tk.RIGHT).pack(side=tk.LEFT)
tk.Label(frame1, text="Number 2:").pack(side=tk.LEFT)
string2 = tk.StringVar()
tk.Entry(frame1, width=5, textvariable=string2, justify=tk.RIGHT).pack(side=tk.LEFT)
tk.Label(frame1, text="Result:").pack(side=tk.LEFT)
string3 = tk.StringVar()
tk.Entry(frame1, width=5, textvariable=string3, justify=tk.RIGHT).pack(side=tk.LEFT)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


# 第一個frame
frame1 = tk.Frame(window, bg="lightyellow")
frame1.pack()

button1 = tk.Button(frame1, text="紅", fg="red")
button1.pack(side=tk.LEFT, padx=5, pady=5)

button2 = tk.Button(frame1, text="綠", fg="green")
button2.pack(side=tk.LEFT, padx=5, pady=5)

button3 = tk.Button(frame1, text="藍", fg="blue")
button3.pack(side=tk.LEFT, padx=5, pady=5)

# 第二個frame
frame2 = tk.Frame(window, bg="lightblue")
frame2.pack()

button4 = tk.Button(frame2, text="紫", fg="purple")
button4.pack(side=tk.LEFT, padx=5, pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(width=300, height=30, relief=tk.GROOVE, borderwidth=5).pack()
frame2 = tk.Frame(width=300, height=30, relief=tk.RAISED, borderwidth=5).pack()
frame3 = tk.Frame(width=300, height=30, relief=tk.RIDGE, borderwidth=5).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 47")
window.title("AddressBook, Grid範例")

frame1 = tk.Frame(window, bg="pink")
frame1.pack()
tk.Label(frame1, text="Name").grid(row=1, column=1, sticky=tk.W)
tk.Entry(frame1, width=40).grid(row=1, column=2)

frame2 = tk.Frame(window)
frame2.pack()
tk.Label(frame2, text="Street").grid(row=1, column=1, sticky=tk.W)
tk.Entry(frame2, width=40).grid(row=1, column=2)

frame3 = tk.Frame(window)
frame3.pack()
tk.Label(frame3, text="City", width=5).grid(row=1, column=1, sticky=tk.W)
tk.Entry(frame3).grid(row=1, column=2)
tk.Label(frame3, text="State").grid(row=1, column=3, sticky=tk.W)
tk.Entry(frame3, width=5).grid(row=1, column=4)
tk.Label(frame3, text="ZIP").grid(row=1, column=5, sticky=tk.W)
tk.Entry(frame3, width=5).grid(row=1, column=6)

frame4 = tk.Frame(window)
frame4.pack()
tk.Button(frame4, text="Add").grid(row=1, column=1)
btFirst = tk.Button(frame4, text="First").grid(row=1, column=2)
btNext = tk.Button(frame4, text="Next").grid(row=1, column=3)
btPrevious = tk.Button(frame4, text="Previous").grid(row=1, column=4)
btLast = tk.Button(frame4, text="Last").grid(row=1, column=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
