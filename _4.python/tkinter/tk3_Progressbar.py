"""
Progressbar

"""

import sys
import time

import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

# 使用預設建立進度條
pb1 = ttk.Progressbar(window)
pb1.pack(pady=20)
pb1["maximum"] = 100
pb1["value"] = 50

# 使用各參數設定方式建立進度條
pb2 = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=200, mode="determinate")
pb2.pack(pady=20)
pb2["maximum"] = 100
pb2["value"] = 50

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def running1():  # 開始Progressbar動畫
    for i in range(100):
        pb["value"] = i + 1  # 每次更新1
        window.update()  # 更新畫面
        time.sleep(0.05)


pb = ttk.Progressbar(window, length=200, mode="determinate", orient=tk.HORIZONTAL)
pb.pack(padx=10, pady=10)
pb["maximum"] = 100
pb["value"] = 0

button1 = tk.Button(window, text="Running", command=running1)
button1.pack(pady=10)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def running2():  # 開始Progressbar動畫
    while pb.cget("value") <= pb["maximum"]:
        pb.step(2)
        window.update()  # 更新畫面
        print(pb.cget("value"))  # 列印指針值
        time.sleep(0.05)


pb = ttk.Progressbar(window, length=200, mode="determinate", orient=tk.HORIZONTAL)
pb.pack(padx=10, pady=10)
pb["maximum"] = 100
pb["value"] = 0

button1 = tk.Button(window, text="Running", command=running2)
button1.pack(pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def run1():  # 開始Progressbar動畫
    pb.start()  # 指針每次移動1


def stop1():  # 中止Progressbar動畫
    pb.stop()  # 中止pb物件動畫


window = tk.Tk()
window.geometry("600x400")

pb = ttk.Progressbar(window, length=200, mode="determinate", orient=tk.HORIZONTAL)
pb.pack(padx=5, pady=10)
pb["maximum"] = 100
pb["value"] = 0

button1 = tk.Button(window, text="Run", command=run1)  # 建立Run按鈕
button1.pack(side=tk.LEFT, padx=5, pady=10)

button2 = tk.Button(window, text="Stop", command=stop1)  # 建立Stop按鈕
button2.pack(side=tk.LEFT, padx=5, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def run2():  # 開始Progressbar動畫
    pb.start()  # 指針每次移動1


def stop2():  # 中止Progressbar動畫
    pb.stop()  # 中止pb物件動畫


window = tk.Tk()
window.geometry("600x400")

pb = ttk.Progressbar(window, length=200, mode="indeterminate", orient=tk.HORIZONTAL)
pb.pack(padx=5, pady=10)
pb["maximum"] = 100
pb["value"] = 0

button3 = tk.Button(window, text="Run", command=run2)  # 建立Run按鈕
button3.pack(side=tk.LEFT, padx=5, pady=10)

button4 = tk.Button(window, text="Stop", command=stop2)  # 建立Stop按鈕
button4.pack(side=tk.LEFT, padx=5, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
