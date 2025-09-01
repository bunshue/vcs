"""
MessageBox測試

"""

import sys

import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog

# from tkinter import *

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("message 1")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

my_mesg = "大雄：1964年8月7日\n哆啦A夢：2112年9月3日\n靜香：1964年12月2日\n小夫：1964年2月29日\n胖虎：1964年6月15日\n哆啦美：2114年12月2日"
msg = tk.Message(window, text=my_mesg)
msg.config(bg="lightgreen", font=("times", 24, "italic"))
msg.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

message = tk.Message(window, text="It is a widgets demo")
message.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# Message測試
tk.Label(text="Message測試").pack()

# w = tk.Message(window, text = "this is a relatively long message")    #自動換行
w = tk.Message(window, text="this is a relatively long message", width=50)  # 限定寬度
w.pack()


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
window.geometry("600x800")
window.title("message 1")

myText = "2016年12月,我一個人訂了機票和船票,開始我的南極旅行"
msg = tk.Message(window, bg="yellow", text=myText, font="times 12 italic")
msg.pack(padx=10, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()

var = tk.StringVar()
msg = tk.Message(window, textvariable=var, relief=tk.RAISED)
var.set("2016年12月,我一個人訂了機票和船票,開始我的南極旅行")
msg.pack(padx=10, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

var = tk.StringVar()
msg = tk.Message(window, textvariable=var, relief=tk.RAISED)
var.set("2016年12月,我一個人訂了機票和船票,開始我的南極旅行")
msg.config(bg="yellow")
msg.pack(padx=10, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
