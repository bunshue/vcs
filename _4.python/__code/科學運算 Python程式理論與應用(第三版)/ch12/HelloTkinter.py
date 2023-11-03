# -*- coding:utf-8 -*-
# file: HelloTkinter.py
#
import tkinter							# 匯入Tkinter模組
root = tkinter.Tk()						# 產生root主視窗
label= tkinter.Label(root, text="Hello, Tkinter!")		# 產生標簽
label.pack()							# 將標簽新增到root主視窗
button1 = tkinter.Button(root, text="Button1")			# 產生button1
button1.pack(side=tkinter.LEFT)					# 將button1新增到root主視窗
button2 = tkinter.Button(root, text="Button2")			# 產生button2
button2.pack(side=tkinter.RIGHT)				# 將button2新增到root主視窗
root.mainloop()							# 進入訊息循環
