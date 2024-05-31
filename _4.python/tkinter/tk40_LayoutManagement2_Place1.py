import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Place 測試"
window.title(title)

print("------------------------------------------------------------")  # 60個

x_st, y_st = 20, 20
dx , dy = 40, 40

tk.Label(window, text = "Blue", bg = "blue").place(x = x_st, y = y_st + dx*0)
tk.Label(window, text = "Red", bg = "red").place(x = x_st, y = y_st + dx*1)
tk.Label(window, text = "Green", bg = "green").place(x = x_st, y = y_st + dx*2)

print("------------------------------------------------------------")  # 60個

# widgets 
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'green')

label1.place(x = 100 , y = 100, width = 100, height = 100)
label2.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = 'se')

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個






#place 大全

print("------------------------------------------------------------")  # 60個

print("place版面佈局")

taipei=tk.Button(window, width=30, text="台北景點")
taipei.place(x=10, y=10)
kaohsiung=tk.Button(window, width=30, text="高雄景點")
kaohsiung.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()

print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, text='push1')
button2 = tk.Button(window, text='push2')
button3 = tk.Button(window, text='push3')

button1.place(x=0, y=0)
button2.place(x=50, y=30)
button3.place(x=100, y=60)

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("400x100")
window.title("place版面佈局的示範")

plus=tk.Button(window, width=30, text="加法範例")
plus.place(x=10, y=10)
minus=tk.Button(window, width=30, text="減法範例")
minus.place(relx=0.5, rely=0.5, anchor="center")
multiply=tk.Button(window, width=30, text="乘法範例")
multiply.place(relx=0.5, rely=0)
divide=tk.Button(window, width=30, text="除法範例")
divide.place(relx=0.5, rely=0.7)

window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位

window.mainloop()

"""
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位
"""



