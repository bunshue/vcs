# -*- coding:utf-8 -*-
# file: TkinterColorChooser.py
#
import tkinter										# 匯入Tkinter模組
import tkinter.colorchooser									# 匯入tkColorChooser模組
def ChooseColor():									# 按鈕事件處理函數
	r = tkinter.colorchooser.askcolor(title = 'Python Tkinter')				# 建立彩色選取交談視窗
	print(r)										# 輸出傳回值
root = tkinter.Tk()
button = tkinter.Button(root,text = 'Choose Color',					# 建立按鈕
		command = ChooseColor)							# 指定按鈕事件處理函數
button.pack()
root.mainloop()										# 進入訊息循環
