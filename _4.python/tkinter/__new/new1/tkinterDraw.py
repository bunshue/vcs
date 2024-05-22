# -*- coding:utf-8 -*-
# file: TkinterDraw.py
#
import tkinter											# 匯入Tkinter模組
class MyButton:											# 定義按鈕類別
	def __init__(self,root,canvas,label,type):						# 類別起始化
		self.root = root								# 儲存參考值
		self.canvas = canvas
		self.label = label
		if type == 0:									# 根據型態建立按鈕
			button = tkinter.Button(root,text = 'DrawLine',
					command = self.DrawLine)
		elif type == 1:
			button = tkinter.Button(root,text = 'DrawArc',
					command = self.DrawArc)
		elif type == 2:
			button = tkinter.Button(root,text = 'DrawRec',
					command = self.DrawRec)
		else :
			button = tkinter.Button(root,text = 'DrawOval',
					command = self.DrawOval)
		button.pack(side = 'left')

	def DrawLine(self):									# DrawLine按鈕事件處理函數
		self.label.text.set('Draw Line')
		self.canvas.SetStatus(0)
	def DrawArc(self):									# DrawArc按鈕事件處理函數
		self.label.text.set('Draw Arc')
		self.canvas.SetStatus(1)
	def DrawRec(self):									# DrawRec按鈕事件處理函數
		self.label.text.set('Draw Rectangle')
		self.canvas.SetStatus(2)
	def DrawOval(self):									# DrawOval按鈕事件處理函數
		self.label.text.set('Draw Oval')
		self.canvas.SetStatus(3)
class MyCanvas:											# 定義Canvas類別
	def __init__(self,root):
		self.status = 0									# 儲存參考值
		self.draw = 0
		self.root = root
		self.canvas = tkinter.Canvas(root,bg = 'white',					# 產生Canvas元件
				width = 600,
				height = 480)
		self.canvas.pack()
		self.canvas.bind('<ButtonRelease-1>',self.Draw)					# 綁定事件到左鍵
		self.canvas.bind('<Button-2>',self.Exit)					# 綁定事件到中鍵
		self.canvas.bind('<Button-3>',self.Del)						# 綁定事件到右鍵
		self.canvas.bind_all('<Delete>',self.Del)					# 綁定事件到Delete鍵
		self.canvas.bind_all('<KeyPress-d>',self.Del)					# 綁定事件到d鍵
		self.canvas.bind_all('<KeyPress-e>',self.Exit)					# 綁定事件到e鍵
	def Draw(self,event):									# 繪圖事件處理函數
		if self.draw == 0: 								# 判斷是否繪圖
			self.x = event.x
			self.y = event.y
			self.draw = 1
		else:										# 根據self.status繪制不同圖形
			if self.status == 0:
				self.canvas.create_line(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			elif self.status == 1:
				self.canvas.create_arc(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			elif self.status == 2:
				self.canvas.create_rectangle(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			else:
				self.canvas.create_oval(self.x,self.y,
						event.x,event.y)
				self.draw = 0
	def Del(self,event):									# 當按下右鍵或d鍵則移除圖形
		items = self.canvas.find_all()
		for item in items:
			self.canvas.delete(item)
	def Exit(self,event):									# 當按下中鍵或e鍵則離開
		self.root.quit()
	def SetStatus(self,status):								# 設定繪制的圖形
		self.status = status
class MyLabel:											# 定義標簽類別
	def __init__(self,root):								# 類別起始化
		self.root = root								# 儲存參考
		self.canvas = canvas
		self.text = tkinter.StringVar()							# 產生標簽參考變數
		self.text.set('Draw Line')
		self.label = tkinter.Label(root,textvariable = self.text,			# 產生標簽
				fg = 'red',width = 50)
		self.label.pack(side = 'left')
root = tkinter.Tk()										# 產生主視窗
canvas = MyCanvas(root)										# 產生繪圖元件
label = MyLabel(root)										# 產生標簽
MyButton(root,canvas,label,0)									# 產生按鈕
MyButton(root,canvas,label,1)
MyButton(root,canvas,label,2)
MyButton(root,canvas,label,3)
root.mainloop()											# 進入訊息循環
