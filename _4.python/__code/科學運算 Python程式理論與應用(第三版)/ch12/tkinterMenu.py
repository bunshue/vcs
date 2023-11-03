# -*- coding:utf-8 -*-
# file: TkinterMenu.py
#
import tkinter 								# 匯入Tkinter模組
root = tkinter.Tk()
menu = tkinter.Menu(root)						# 產生選單
submenu = tkinter.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Open")					# 向下拉選單中加入Open指令
submenu.add_command(label="Save")					# 向下拉選單中加入Save指令
submenu.add_command(label="Close")					# 向下拉選單中加入Close指令
menu.add_cascade(label="File", menu=submenu)				# 將下拉選單新增到選單中
submenu = tkinter.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Copy")					# 向下拉選單中加入Copy指令
submenu.add_command(label="Paste")					# 向下拉選單中加入Paste指令
submenu.add_separator()							# 向下拉選單中加入分隔符
submenu.add_command(label="Cut")					# 向下拉選單中加入Cut指令
menu.add_cascade(label="Edit", menu=submenu)				# 將下拉選單新增到選單中
submenu = tkinter.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="About")					# 向下拉選單中加入About指令
menu.add_cascade(label="Help", menu=submenu)				# 將下拉選單新增到選單中
root.config(menu=menu)
root.mainloop()
