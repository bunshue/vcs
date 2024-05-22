# -*- coding:utf-8 -*-
# file: TkinterRCButton.py
#
import tkinter							# 匯入Tkinter模組
root = tkinter.Tk()
r = tkinter.StringVar()						# 使用StringVar產生字串變數用於單選框元件
r.set('1')							# 起始化變數值
radio = tkinter.Radiobutton(root,				# 產生單選框元件
			variable = r, 				# 設定單選框關聯的變數
			value = '1',				# 設定勾選單選框時其所關聯的變數的值，即r的值
			indicatoron = 0,			# 將單選框繪製成按鈕型態
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()
radio = tkinter.Radiobutton(root,
			variable = r,
			value = '2',				# 當勾選該單選框時r的值為2
			indicatoron = 0,
			text = 'Radio2' )
radio.pack()
radio = tkinter.Radiobutton(root,
			variable = r,
			value = '3',				# 當勾選該單選框時r的值為3
			indicatoron = 0,
			text = 'Radio3' )
radio.pack()
radio = tkinter.Radiobutton(root,
			variable = r,
			value = '4',				# 當勾選該單選框時r的值為4
			indicatoron = 0,
			text = 'Radio4' )
radio.pack()
c = tkinter.IntVar()						# 使用IntVar產生整數變數用於復選框
c.set(1)
check = tkinter.Checkbutton(root,
			text = 'Checkbutton',			# 設定復選框的文字
			variable = c,				# 設定復選框關聯的變數
			indicatoron = 0,			# 將復選框繪製成按鈕型態
			onvalue = 1,				# 當勾選復選框時，c的值為1
			offvalue = 2)				# 當未勾選復選框時，c的值為2
check.pack()
root.mainloop()
