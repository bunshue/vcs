# -*- coding:utf-8 -*-
# file: TkinterPopupmenu.py
#
import tkinter 
root = tkinter.Tk()
menu = tkinter.Menu(root, tearoff=0)				# 建立選單
menu.add_command(label="Copy")					# 向出現式選單中加入Copy指令
menu.add_command(label="Paste")					# 向出現式選單中加入Paste指令
menu.add_separator()						# 向出現式選單中加入分隔符
menu.add_command(label="Cut")					# 向出現式選單中加入Cut指令
def popupmenu(event):						# 定義右鍵事件處理函數
    menu.post(event.x_root, event.y_root)			# 顯示選單
root.bind("<Button-3>", popupmenu)				# 在主視窗中綁定右鍵事件
root.mainloop()
