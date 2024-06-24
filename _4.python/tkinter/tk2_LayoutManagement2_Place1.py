import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Place 測試 絕對位置")

print("------------------------------------------------------------")  # 60個

x_st, y_st = 20, 20
dx, dy = 40, 40

tk.Label(window, text="Blue", bg="blue").place(x=x_st, y=y_st + dx * 0)
tk.Label(window, text="Red", bg="red").place(x=x_st, y=y_st + dx * 1)
tk.Label(window, text="Green", bg="green").place(x=x_st, y=y_st + dx * 2)

print("------------------------------------------------------------")  # 60個

# widgets
label1 = ttk.Label(window, text="方塊 Label", background="red")
label1.place(x=100, y=20, width=100, height=100)

print("------------------------------------------------------------")  # 60個

taipei = tk.Button(window, width=30, text="台北景點")
taipei.place(x=300, y=200)

print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, text="push1")
button2 = tk.Button(window, text="push2")
button3 = tk.Button(window, text="push3")

x_st, y_st = 10, 150
dy = 40
button1.place(x=x_st, y=y_st + dy * 0)
button2.place(x=x_st, y=y_st + dy * 1)
button3.place(x=x_st, y=y_st + dy * 2)

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(
    window, text="歡迎來到美國", bg="lightyellow", width=15  # 標籤背景是淺黃色
)  # 標籤寬度是15
lab2 = tk.Label(window, text="歡迎來到日本", bg="lightgreen", width=15)  # 標籤背景是淺綠色  # 標籤寬度是15
lab3 = tk.Label(window, text="歡迎來到加拿大", bg="lightblue", width=15)  # 標籤背景是淺藍色  # 標籤寬度是15

x_st, y_st = 100, 150
dy = 40
lab1.place(x=x_st, y=y_st + dy * 0)  # 直接定位
lab2.place(x=x_st, y=y_st + dy * 1)  # 直接定位
lab3.place(x=x_st, y=y_st + dy * 2)  # 直接定位

print("------------------------------------------------------------")  # 60個


label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow", width=15)
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen", width=15)
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue", width=15)
label1.place(x=300, y=0)  # 直接定位
label2.place(x=300, y=50)  # 直接定位
label3.place(x=300, y=100)  # 直接定位

print("------------------------------------------------------------")  # 60個

label1 = tk.Label(
    window, text="五色鳥 Muller's Barbet", font=("微軟正黑體", 18), fg="white", bg="black"
)
label2 = tk.Label(window, text="啄木鳥目", font=("標楷體", 16), fg="blue", bg="lightblue")
label3 = tk.Label(window, text="五色鳥科", font=("標楷體", 14), fg="green", bg="lightgreen")
msg = "分布海平面到2800公尺，全身為鮮艷的翠綠色，在闊葉林中有良好的保護色。"
label4 = tk.Label(window, text=msg, font=("細明體", 12), wraplength=170)

x_st, y_st = 10, 300
label1.place(x=x_st + 10, y=y_st + 5, width=280, height=40)
label2.place(x=x_st + 10, y=y_st + 50, width=90, height=50)
label3.place(x=x_st + 10, y=y_st + 105, width=90, height=50)
label4.place(x=x_st + 110, y=y_st + 50, width=180, height=105)

print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Place 測試 比例")

label2 = ttk.Label(window, text="Label 2", background="green")
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor="se")

kaohsiung = tk.Button(window, width=30, text="高雄景點")
kaohsiung.place(relx=0.6, rely=0.6, anchor="center")

x_st, y_st = 300, 10
dy = 40
plus = tk.Button(window, width=30, text="加法範例")
plus.place(x=x_st, y=y_st + dy * 0)
minus = tk.Button(window, width=30, text="減法範例")
minus.place(relx=0.5, rely=0.1, anchor="center")
multiply = tk.Button(window, width=30, text="乘法範例")
multiply.place(relx=0.5, rely=0.2)
divide = tk.Button(window, width=30, text="除法範例")
divide.place(relx=0.5, rely=0.3)

print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
