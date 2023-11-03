# -*- coding:utf-8 -*-
# file: PyGTKFixed.py
#
import pygtk											# 匯入pygtk模組
pygtk.require('2.0')										# 設定pygtk所需的gtk版本
import gtk											# 匯入gtk模組
class MyWindow():										# 定義視窗類別
	def __init__(self, title, width, height):						# 定義起始化方法
		self.window = gtk.Window()							# 產生視窗物件
		self.window.set_title(title)							# 設定視窗標題
		self.window.set_default_size(width, height)					# 設定視窗大小
		self.window.connect('destroy', lambda q: gtk.main_quit())
		self.fixed = gtk.Fixed()
		self.label = gtk.Label('PyGTK')							# 建立標簽
		self.fixed.put(self.label,10,5)							# 加入標簽
		self.button = gtk.Button('Move')						# 建立按鈕
		self.button.connect('clicked',self.OnButton, 'Move')				# 綁定按鈕事件
		self.fixed.put(self.button, 120, 150)						# 加入按鈕
		self.window.add(self.fixed)							# 向視窗中加入Fixed
		self.label.show()								# 顯示標簽
		self.button.show()								# 顯示按鈕
		self.fixed.show()								# 顯示Fixed元件
		self.window.show()								# 顯示視窗
	def OnButton(self, widget, data):
		self.fixed.move(self.label, 100,50)
	def main(self):										# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()

