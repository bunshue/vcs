# -*- coding:utf-8 -*-
# file: PyGTKRCbutton.py
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
		self.label1 = gtk.Label('PyGTK')						# 建立標簽
		self.fixed.put(self.label1, 80, 20)						# 加入標簽
		self.label2 = gtk.Label('PyGTK')
		self.fixed.put(self.label2, 160, 20)						# 加入單選框
		self.radio1 = gtk.RadioButton(None, 'Radio1')
		self.fixed.put(self.radio1, 50, 60)
		self.radio2 = gtk.RadioButton(self.radio1, 'Radio2')
		self.fixed.put(self.radio2, 50, 90)
		self.radio3 = gtk.RadioButton(self.radio1, 'Radio3')
		self.fixed.put(self.radio3, 50, 120)
		self.check = gtk.CheckButton('CheckButton')
		self.fixed.put(self.check, 150, 60)
		self.button = gtk.Button('Test')						# 建立按鈕
		self.button.connect('clicked',self.OnButton, 'Test')				# 綁定按鈕事件
		self.fixed.put(self.button, 120, 150)						# 加入按鈕
		self.window.add(self.fixed)							# 向視窗中加入Fixed
		self.label1.show()								# 顯示元件
		self.label2.show()
		self.radio1.show()
		self.radio2.show()
 		self.radio3.show()
		self.check.show()
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):
		if self.check.get_active():							# 判斷復選框是否勾選
			self.label2.set_text('checked')
		else:
			self.label2.set_text('uncheck')
		if self.radio1.get_active():							# 判斷復選框勾選狀態
			self.label1.set_text('Radio1')
		elif self.radio2.get_active():
			self.label1.set_text('Radio2')
		else:
			self.label1.set_text('Radio3')
	def main(self):										# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()


