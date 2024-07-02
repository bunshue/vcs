"""

1. pack無參數
2. pack(side)
3. pack(fill)
4. pack


"""

import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Pack 測試")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame()
frame1.pack()

tk.Label(frame1, text="tk.LEFT:").pack(side=tk.LEFT)
tk.Entry(frame1, text="Type Name").pack(side=tk.LEFT)
tk.Checkbutton(frame1, text="Bold").pack(side=tk.LEFT)
tk.Checkbutton(frame1, text="Italic").pack(side=tk.LEFT)
tk.Radiobutton(frame1, text="Red").pack(side=tk.LEFT)
tk.Radiobutton(frame1, text="Yellow").pack(side=tk.LEFT)

button1 = tk.Button(frame1, text="LEFT", fg="red")
button1.pack(side=tk.LEFT)  # 靠左, 這樣下一個會連上來

button3 = tk.Button(frame1, text="LEFT")
button3.pack(side=tk.LEFT)  # 靠左, 這樣下一個會連上來
# button3.pack() #這一行結束

button4 = tk.Button(frame1, text="PACK()")
button4.pack()

button5 = tk.Button(frame1, text="PACK()")
button5.pack()

button6 = tk.Button(frame1, text="PACK()")
button6.pack()

button7 = tk.Button(frame1, text="PACK()")
button7.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

"""
lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM)
lab3.pack(side=tk.BOTTOM)
"""
lab1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM, pady=5)  # 包裝與定位元件,增加y軸間距
lab3.pack(side=tk.BOTTOM)

"""
lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT)
lab3.pack(side=tk.LEFT)
"""
"""
lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT,padx=5)         # 增加x軸間距
lab3.pack(side=tk.LEFT)
"""

lab1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)
lab1.pack()
lab2.pack(side=tk.RIGHT)
lab3.pack(side=tk.LEFT)


lab1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM)
lab3.pack(side=tk.BOTTOM)


lab1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)

lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM, pady=5)  # 增加y軸間距
lab3.pack(side=tk.BOTTOM)


lab1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)

lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT)
lab3.pack(side=tk.LEFT)


lab1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)
lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT, padx=5)  # 增加x軸間距
lab3.pack(side=tk.LEFT)


lab1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)
lab1.pack()
lab2.pack(side=tk.RIGHT)
lab3.pack(side=tk.LEFT)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


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
window.geometry("600x400")
window.title("Pack 測試")
window.configure(bg="white")

label1 = tk.Label(
    window, text="元件版面配置 fill x", font=("微軟正黑體", 16), fg="white", bg="blue"
)
label1.pack(fill="x")

label2 = tk.Label(window, text="方法 left, y", font=("標楷體", 12))
label2.pack(side="left", fill="y")

label3 = tk.Label(
    window, text="pack()方法, both, True", font=("標楷體", 12), bg="lightgreen"
)
label3.pack(pady=5, fill="both", expand=True)

label4 = tk.Label(window, text="place()方法, both, True", font=("標楷體", 12), bg="pink")
label4.pack(pady=5, fill="both", expand=True)

label5 = tk.Label(window, text="grid()方法, both, True", font=("標楷體", 12), bg="lightblue")
label5.pack(pady=5, fill="both", expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x300")
window.title("Pack 測試")

tk.Label(window, text="紅色 pack()", bg="red").pack()
tk.Label(window, text="綠色, BOTH expand", bg="green").pack(fill=tk.BOTH, expand=1)
tk.Label(window, text="藍色, BOTH", bg="blue").pack(fill=tk.BOTH)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def drawABar(x, percent, color, title):
    canvas.create_line(0, height - 10, width, height - 10)
    canvas.create_rectangle(
        x, (1 - percent) * (height - 30), x + width / 4.3 - 5, height - 10, fill=color
    )
    canvas.create_text(
        (x + x + width / 4.3 - 5) / 2, (1 - percent) * (height - 30) - 10, text=title
    )


window = tk.Tk()
window.geometry("600x800")
window.title("Pack 測試")
window.title("Pyramid")  # Set a title

width = 400
height = 150
canvas = tk.Canvas(window, bg="white", width=width, height=height)
canvas.pack()

x = 10
drawABar(x, 0.4, "red", "Project -- 20%")

x += width / 4.3 - 5 + 10
drawABar(x, 0.1, "blue", "Quizzes -- 10%")

x += width / 4.3 - 5 + 10
drawABar(x, 0.3, "green", "Midterm -- 30%")

x += width / 4.3 - 5 + 10
drawABar(x, 0.4, "orange", "Final -- 40%")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("Pack布局")

# 創建第一個容器
fm1 = tk.Frame(window)
# 該容器放在左邊排列
fm1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
# 向fm1中添加3個按鈕
# 設置按鈕從頂部開始排列，且按鈕只能在垂直（X）方向填充
tk.Button(fm1, text="第一個").pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
tk.Button(fm1, text="第二個").pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
tk.Button(fm1, text="第三個").pack(side=tk.TOP, fill=tk.X, expand=tk.YES)

# 創建第二個容器
fm2 = tk.Frame(window)
# 該容器放在左邊排列，就會挨著fm1
#fm2.pack(side=tk.LEFT, padx=10, expand=tk.YES)
fm2.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=tk.YES)
# 向fm2中添加3個按鈕
# 設置按鈕從右邊開始排列
tk.Button(fm2, text="第一個").pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
tk.Button(fm2, text="第二個").pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
tk.Button(fm2, text="第三個").pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)

# 創建第三個容器
fm3 = tk.Frame(window)
# 該容器放在右邊排列，就會挨著fm1
fm3.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=tk.YES)
# 向fm3中添加3個按鈕
# 設置按鈕從底部開始排列，且按鈕只能在垂直（Y）方向填充
tk.Button(fm3, text="第一個").pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)
tk.Button(fm3, text="第二個").pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)
tk.Button(fm3, text="第三個").pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""

各種 pack 之 side


label1.pack(side=tk.BOTTOM)
label2.pack(side=tk.BOTTOM)
label3.pack(side=tk.BOTTOM)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label1.pack()
label2.pack(side=RIGHT)               # 靠右包裝與定位元件
label3.pack(side=LEFT)                # 靠左包裝與定位元件

button1.pack(side = tk.LEFT)    #靠左對齊
button2.pack(side = tk.RIGHT)   #靠右對齊


#三個button並排靠左排列
button1 = tk.Button(window,text = 'Input String')
button1.pack(side='left')
button2 = tk.Button(window,text = 'Input Integer')
button2.pack(side='left')
button2 = tk.Button(window,text = 'Input Float')
button2.pack(side='left')


print("pack版面佈局")

taipei=tk.Button(window, width=20, text="台北景點")
taipei.pack(side="top")
kaohsiung=tk.Button(window, width=20, text="高雄景點")
kaohsiung.pack(side="top")



button1 = tk.Button(window, text="pack置中", width=20).pack()
button2 = tk.Button(window, text="pack左", width=20).pack(side=tk.LEFT)
button3 = tk.Button(window, text="pack右", width=20).pack(side=tk.RIGHT)

# 將4個鈕包裝定位在右下方
button4.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button3.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button2.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button1.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)

print("pack版面佈局的示範")

plus = tk.Button(window, width=20, text="加法範例")
plus.pack(side="left")
minus = tk.Button(window, width=20, text="減法範例")
minus.pack(side="left")
multiply = tk.Button(window, width=20, text="乘法範例")
multiply.pack(side="left")
divide = tk.Button(window, width=20, text="除法範例")
divide.pack(side="left")

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(fill=tk.X)  # 填滿X軸包裝與定位元件
label2.pack(pady=10)  # y軸增加10像素
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")  # 標籤背景是淺藍色
label1.pack(fill=tk.X, pady=10)  # 填滿X軸,Y軸增加10像素
label2.pack(pady=10)  # Y軸增加10像素
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(
    window, text="歡迎來到美國", bg="lightyellow", width=15  # 標籤背景是淺黃色
)  # 標籤寬度是15
label2 = tk.Label(
    window, text="歡迎來到美國", bg="lightgreen", width=15  # 標籤背景是淺綠色
)  # 標籤寬度是15
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue", width=15)  # 標籤寬度是15
label1.pack(padx=50)  # 左右邊界間距是50像素
label2.pack(padx=50)  # 左右邊界間距是50像素
label3.pack(padx=50)  # 左右邊界間距是50像素

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(
    window, text="歡迎來到美國", bg="lightyellow", width=15  # 標籤背景是淺黃色
)  # 標籤寬度是15
label2 = tk.Label(
    window, text="歡迎來到美國", bg="lightgreen", width=15  # 標籤背景是淺綠色
)  # 標籤寬度是15
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue", width=15)  # 標籤寬度是15
label1.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT, padx=10)  # 左右間距padx=10
label3.pack(side=tk.LEFT)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack()
label2.pack(ipadx=10)  # ipadx=10包裝與定位元件
label3.pack()




label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")  # 標籤背景是淺黃色
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack()
label2.pack(ipadx=10)  # ipadx=10包裝與定位元件
label3.pack(ipady=10)  # ipady=10包裝與定位元件

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(fill=tk.X)  # 填滿X軸包裝與定位元件
label2.pack()
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件


label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(fill=tk.X)  # 填滿X軸包裝與定位元件
label2.pack(fill=tk.Y)  # 填滿Y軸包裝與定位元件
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件


label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT)  # 從左配置控件
label2.pack()  # 預設從上開始配置控件
label3.pack()  # 預設從上開始配置控件

print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack()  # 預設從上開始配置控件

print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH)  # 預設從上開始配置控件fill=tk.BOTH




"""




window = tk.Tk()
window.geometry("600x800")
window.title("new all 4")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH, expand=True)  # fill=tk.BOTH,expand=True

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text="Mississippi", bg="red", fg="white", font="Times 24 bold").pack(
    fill=tk.X
)
tk.Label(
    window, text="Kentucky", bg="green", fg="white", font="Arial 24 bold italic"
).pack(fill=tk.BOTH, expand=True)
tk.Label(window, text="Purdue", bg="blue", fg="white", font="Times 24 bold").pack(
    fill=tk.X
)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text="Mississippi", bg="red", fg="white", font="Times 20 bold").pack(
    side=tk.LEFT, fill=tk.Y
)
tk.Label(
    window, text="Kentucky", bg="green", fg="white", font="Arial 20 bold italic"
).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
tk.Label(window, text="Purdue", bg="blue", fg="white", font="Times 20 bold").pack(
    side=tk.LEFT, fill=tk.Y
)

window.mainloop()
