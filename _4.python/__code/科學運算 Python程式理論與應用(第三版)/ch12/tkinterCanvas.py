# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
import tkinter								# 匯入Tkinter模組
root = tkinter.Tk()
canvas = tkinter.Canvas(root,
			width = 600,					# 指定Canvas元件的寬度
			height = 480,					# 指定Canvas元件的高度
			bg = 'white')					# 指定Canvas元件的背景色
im = tkinter.PhotoImage(file='python.gif')				# 使用PhotoImage開啟圖片
canvas.create_image(300,50,image = im)					# 使用create_image將圖片新增到Canvas元件中
canvas.create_text(302,77,						# 使用create_text方法在座標（302，77）處繪制文字
		text = 'Use Canvas'					# 所繪制文字的內容
		,fill = 'gray')						# 所繪制文字的彩色為灰色
canvas.create_text(300,75,
		text = 'Use Canvas',
		fill = 'blue')
canvas.create_polygon(290,114,316,114,330,130,				# 使用create_polygon方法繪制六邊形
		      310,146,284,146,270,130)
canvas.create_oval(280,120,320,140,					# 使用create_oval方法繪制橢圓
		fill = 'white')						# 設定橢圓用白色填充
canvas.create_line(250,130,350,130)					# 使用create_line繪制一條從（250,130）到（350,130）的直線
canvas.create_line(300,100,300,160)
canvas.create_rectangle(90,190,510,410,					# 使用create_rectangle繪制一個矩形
		width=5)						# 設定矩形線寬為5個像素
canvas.create_arc(100, 200, 500, 400, 					# 使用create_arc繪制圓弧
		start=0, extent=240, 					# 設定圓弧的起止角度
		fill="pink")						# 設定圓弧填充彩色
canvas.create_arc(103,203,500,400, 
		start=241, extent=118, 
		fill="red")
canvas.pack()								# 將Canvas新增到主視窗
root.mainloop()
