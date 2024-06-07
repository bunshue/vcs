import tkinter as tk

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
title = "這是主視窗"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def changeString():
    stringToCopy = entry.get()
    #stringToCopy = stringToCopy[::-1]
    #entry.delete(0, tk.END)
    entry.insert(0, stringToCopy)

entry = tk.Entry(window)
entry.pack()

button0 = tk.Button(window, text = 'Change', command = changeString)
button0.pack()

frame = tk.Frame()
frame.pack()

button1 = tk.Button(frame, text = 'QUIT', fg = 'red', command = frame.quit)
button1.pack(side = tk.LEFT)#靠左, 這樣下一個會連上來

button2 = tk.Button(frame, text = 'Hello')
button2.pack(side = tk.LEFT)#靠左, 這樣下一個會連上來

button3 = tk.Button(frame, text = 'New')
button3.pack(side = tk.LEFT)#靠左, 這樣下一個會連上來
#button3.pack() #這一行結束

button4 = tk.Button(frame, text = 'New')
button4.pack()

button5 = tk.Button(frame, text = 'New')
button5.pack()

button6 = tk.Button(frame, text = 'New')
button6.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def display():
    number = int(order.get())
    print('取得 order = ', number)
                
frame1 = tk.Frame(window, bg = 'pink') # Create and add a frame to window
frame1.pack()

tk.Label(frame1, text = "Enter an order: ").pack(side = tk.LEFT)
order = tk.StringVar()
entry = tk.Entry(frame1, textvariable = order, justify = tk.RIGHT).pack(side = tk.LEFT)
tk.Button(frame1, text = 'Do something', command = display).pack(side = tk.LEFT)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()


import tkinter as tk

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
title = "這是主視窗"
window.title(title)




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線






separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線




window.mainloop()



print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個
print("pack")
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM)
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM,pady=5)       # 包裝與定位元件,增加y軸間距
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT,padx=5)         # 增加x軸間距
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack()
lab2.pack(side=tk.RIGHT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM)
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM,pady=5)       # 增加y軸間距
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT,padx=5)  # 增加x軸間距
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack()
lab2.pack(side=tk.RIGHT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

label=tk.Label(window,text="歡迎來到美國",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="se")
label.pack()  

window.mainloop()

print("------------------------------------------------------------")  # 60個

window=tk.Tk()
window.geometry("600x400")
window.title('pack配置')
window.configure(bg='white')

label1=tk.Label(window, text = '元件版面配置',font=('微軟正黑體', 16),fg='white',bg='blue')
label2=tk.Label(window, text = '方法',font=('標楷體', 12))
label3=tk.Label(window, text = 'pack()方法',font=('標楷體', 12),bg='lightgreen')
label4=tk.Label(window, text = 'grid()方法',font=('標楷體', 12),bg='pink')
label5=tk.Label(window, text = 'place()方法',font=('標楷體', 12),bg='lightblue')
label1.pack(fill='x')
label2.pack(side='left', fill='y')
label3.pack(pady=5, fill='both', expand=True)
label4.pack(pady=5, fill='both', expand=True)
label5.pack(pady=5, fill='both', expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

