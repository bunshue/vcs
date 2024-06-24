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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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




"""
