# -*- coding:utf-8 -*-
# file: TkinterButton.py
#
import tkinter							# 匯入Tkinter模組
root = tkinter.Tk()
button1 = tkinter.Button(root, 			
			anchor = tkinter.E,			# 指定文字對齊模式
			text = 'Button1',			# 指定按鈕上的文字
			width = 40,				# 指定按鈕的寬度，相當於40個字元
			height = 5)				# 指定按鈕的高度，相當於5行字元
button1.pack()							# 將按鈕新增到視窗
button2 = tkinter.Button(root, 			
			text = 'Button2',	
			bg = 'blue')				# 指定按鈕的背景色
button2.pack()
button3 = tkinter.Button(root, 			
			text = 'Button3',	
			width = 14,				# 指定按鈕的寬度
			height = 1)				# 指定按鈕的高度
button3.pack()
button4 = tkinter.Button(root, 			
			text = 'Button4',	
			width = 60,		
			height = 5,		
			state = tkinter.DISABLED)		# 指定按鈕為禁用狀態
button4.pack()
root.mainloop()							# 進入訊息循環
