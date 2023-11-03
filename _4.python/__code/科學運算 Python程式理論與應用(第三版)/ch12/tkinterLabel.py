# -*- coding:utf-8 -*-
# file: TkinterLabel.py
#
import tkinter								# 匯入Tkinter模組
root = tkinter.Tk()
label1 = tkinter.Label(root,
			anchor = tkinter.E,				# 設定文字的位置
			bg = 'blue',					# 設定標簽背景色
			fg = 'red',					# 設定標簽前景色
			text = 'Python',				# 設定標簽中的文字
			width = 30,					# 設定標簽的寬度為30
			height = 5)					# 設定標簽的的高度為5
label1.pack()
label2 = tkinter.Label(root,
			text = 'Python GUI\nTkinter',			# 設定標簽中的文字，在字串中使用換行符
			justify = tkinter.LEFT,				# 設定多行文字為齊左
			width = 30,
			height = 5)
label2.pack()
label3 = tkinter.Label(root,
			text = 'Python GUI\nTkinter',
			justify = tkinter.RIGHT,			# 設定多行文字為齊右
			width = 30,
			height = 5)
label3.pack()
label4 = tkinter.Label(root,
			text = 'Python GUI\nTkinter',
			justify = tkinter.CENTER,			# 設定多行文字為劇中對齊
			width = 30,
			height = 5)
label4.pack()
root.mainloop()
