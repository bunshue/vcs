# -*- coding:utf-8 -*-
# file: TkinterEntry.py
#
import tkinter								# 匯入Tkinter模組
root = tkinter.Tk()
entry1 = tkinter.Entry(root,						# 產生單行文字框元件
			show = '*',)					# 輸入文字框中的字元被顯示為“*”
entry1.pack()								# 將文字框新增到視窗中
entry2 = tkinter.Entry(root,
			show = '#',					# 輸入文字框中的字元被顯示為“#”
			width = 50)					# 將文字框的寬度設定為50
entry2.pack()
entry3 = tkinter.Entry(root,
			bg = 'red',					# 將文字框的背景色設定為紅色
			fg = 'blue')					# 將文字框的前景色設定為藍色
entry3.pack()
entry4 = tkinter.Entry(root,
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
entry4.pack()
entry5 = tkinter.Entry(root,
			state = tkinter.DISABLED)			# 將文字框設定為禁用
entry5.pack()
edit1 = tkinter.Text(root,						# 產生多行文字框元件
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
edit1.pack()
root.mainloop()								# 進入訊息循環
