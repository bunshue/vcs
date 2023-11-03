# -*- coding:utf-8 -*-
# file: PyGTKLayout.py
#
import pygtk											# 匯入pygtk模組
pygtk.require('2.0')										# 設定pygtk所需的gtk版本
import gtk											# 匯入gtk模組
class MyWindow():										# 定義視窗類別
	def __init__(self, title, width, height):						# 定義起始化方法
		self.x = 10									# 定義座標訊息
		self.y = 5
		self.window = gtk.Window()							# 產生視窗物件
		self.window.set_title(title)							# 設定視窗標題
		self.window.set_default_size(width, height)					# 設定視窗大小
		self.window.connect('destroy', lambda q: gtk.main_quit())
		self.layout = gtk.Layout()
		self.label = gtk.Label('PyGTK')							# 建立標簽
		self.layout.put(self.label,self.x,self.y)					# 加入標簽
		self.button = gtk.Button('Move')						# 建立按鈕
		self.button.connect('clicked',self.OnButton, 'Move')				# 綁定按鈕事件
		self.layout.put(self.button, 120, 150)						# 加入按鈕
		self.window.add(self.layout)							# 向視窗中加入Layout
		self.label.show()								# 顯示標簽
		self.button.show()								# 顯示按鈕
		self.layout.show()								# 顯示Layout元件
		self.window.show()								# 顯示視窗
	def OnButton(self, widget, data):							# 按鈕事件響應函數
		self.x = self.x + 5
		self.y = self.y + 5
		if self.x >= 300:
			self.x = 10
		if self.y >= 200:
			self.y = 5
		self.layout.move(self.label, self.x, self.y)					# 搬移標簽
	def main(self):										# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()


