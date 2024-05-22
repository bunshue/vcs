# -*- coding:utf-8 -*-
# file: TkinterSimpleDialog.py
#
import tkinter										# 匯入Tkinter模組
import tkinter.simpledialog									# 匯入tkSimpleDialog模組
def InStr():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askstring('Python Tkinter',					# 建立字串輸入交談視窗
			'Input String',							# 指定提示字元
			initialvalue='Tkinter')						# 指定起始化文字
	print(r)									# 輸出傳回值
def InInt():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askinteger('Python Tkinter','Input Integer')			# 建立整數輸入交談視窗
	print(r)
def InFlo():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askfloat('Python Tkinter','Input Float')			# 建立浮點數輸入交談視窗
	print(r)
root = tkinter.Tk()
button1 = tkinter.Button(root,text = 'Input String',					# 建立按鈕
		command = InStr)							# 指定按鈕事件處理函數
button1.pack(side='left')
button2 = tkinter.Button(root,text = 'Input Integer',
		command = InInt)							# 指定按鈕事件處理函數
button2.pack(side='left')
button2 = tkinter.Button(root,text = 'Input Float',
		command = InFlo)							# 指定按鈕事件處理函數
button2.pack(side='left')
root.mainloop()										# 進入訊息循環
