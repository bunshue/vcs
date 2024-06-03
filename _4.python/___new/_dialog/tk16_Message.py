import sys

import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog

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

# MessageBox測試

my_mesg = "大雄：1964年8月7日\n哆啦A夢：2112年9月3日\n靜香：1964年12月2日\n小夫：1964年2月29日\n胖虎：1964年6月15日\n哆啦美：2114年12月2日"
msg = tk.Message(window, text = my_mesg)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

print("------------------------------------------------------------")  # 60個
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

message = tk.Message(window, text = "It is a widgets demo")
message.pack()

print("------------------------------------------------------------")  # 60個
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Message測試
tk.Label(text = 'Message測試').pack()

#w = tk.Message(window, text = "this is a relatively long message")    #自動換行
w = tk.Message(window, text = "this is a relatively long message", width = 50)  #限定寬度
w.pack()


print("------------------------------------------------------------")  # 60個
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


