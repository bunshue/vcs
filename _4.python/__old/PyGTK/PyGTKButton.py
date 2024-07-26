# -*- coding:utf-8 -*-
# file: PyGTKButton.py
#
import pygtk											# 匯入pygtk模組
pygtk.require('2.0')										# 設定pygtk所需的gtk版本
import gtk											# 匯入gtk模組
class MyWindow():										# 定義視窗類別
	def __init__(self, title, width, height):						# 定義起始化方法
		self.window = gtk.Window()							# 產生視窗物件
		self.window.set_title(title)							# 設定視窗標題
		self.window.set_default_size(width, height)				# 設定視窗大小
		hbox = gtk.HBox(False, 20)							# 產生水平Box物件
		button1 = gtk.Button('Button1')							# 建立按鈕
		button2 = gtk.Button('Button2')
		hbox.pack_start(button1)							# 向Box物件中加入按鈕
		hbox.pack_start(button2)
		self.window.add(hbox)								# 向視窗加入Box物件
		hbox.show()									# 顯示Box物件
		button1.show()									# 顯示按鈕
		button2.show()
		self.window.show()								# 顯示視窗
	def main(self):										# 定義main方法
		gtk.main()									# 呼叫gtk.main方法
window = MyWindow('PyGTK', 150, 30)								# 建立視窗物件
window.main()
