"""
import tkinter as tk
import tkinter.colorchooser									# 匯入tkColorChooser模組

def ChooseColor():									# 按鈕事件處理函數
	r = tkinter.colorchooser.askcolor(title = 'Python Tkinter')				# 建立彩色選取交談視窗
	print(r)										# 輸出傳回值

window = tk.Tk()
button = tk.Button(window,text = 'Choose Color',					# 建立按鈕
		command = ChooseColor)							# 指定按鈕事件處理函數
button.pack()

window.mainloop()

"""

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.colorchooser import *

def bgUpdate():
    ''' 更改視窗背景顏色 '''
    myColor = askcolor()            # 列出色彩對話方塊
    print(type(myColor),myColor)    # 列印傳回值
    root.config(bg=myColor[1])      # 設定視窗背景顏色
        
root = Tk()
root.title("")
root.geometry("360x240")

btn = Button(text="Select Color",command=bgUpdate)
btn.pack(pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

