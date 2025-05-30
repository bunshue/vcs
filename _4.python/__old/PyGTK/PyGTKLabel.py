# -*- coding:utf-8 -*-
# file: PyGTKLabel.py
#
import pygtk											# 匯入pygtk模組
pygtk.require('2.0')										# 設定pygtk所需的gtk版本
import gtk											# 匯入gtk模組
class MyWindow():										# 定義視窗類別
	def __init__(self, title, width, height):						# 定義起始化方法
		self.window = gtk.Window()							# 產生視窗物件
		self.window.set_title(title)							# 設定視窗標題
		self.window.set_default_size(width, height)					# 設定視窗大小
		label = gtk.Label('PyGTK')							# 建立標簽
		label.set_angle(90)								# 設定標簽角度
		self.window.add(label)								# 向視窗中加入標簽
		label.show()									# 顯示標簽
		self.window.show()								# 顯示視窗
	def main(self):										# 定義main方法
		gtk.main()									# 呼叫gtk.main方法
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()
