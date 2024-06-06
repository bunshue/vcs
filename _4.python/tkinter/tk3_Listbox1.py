import tkinter as tk

print('------------------------------------------------------------')	#60個

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = 'Listbox 測試'
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

tk.Label(text = 'Listbox 測試').pack()
tk.Label(text = 'Scrollbar 測試').pack()

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

listbox = tk.Listbox(window, yscrollcommand = scrollbar.set)
#Listbox內加入項目
for i in range(100):
    listbox.insert(tk.END, str(i))
    
listbox.pack(side = tk.LEFT, fill = tk.BOTH)

scrollbar.config(command = listbox.yview)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

tk.Label(text = 'Listbox 測試').pack()

listbox = tk.Listbox(window)
#Listbox內加入項目
listbox.insert(tk.END, "a list entry")
for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)

listbox.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

print('------------------------------------------------------------')	#60個


print('Listbox + Scrollbar')

window = tk.Tk()
window.geometry("400x200")

scrollbar = tk.Scrollbar(window)
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

wordlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = tk.Listbox(window, yscrollcommand = scrollbar.set )

for line in range(26):
   list1.insert(tk.END, "字母: " + wordlist[line])

list1.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = list1.yview )

window.mainloop()

print('------------------------------------------------------------')	#60個


