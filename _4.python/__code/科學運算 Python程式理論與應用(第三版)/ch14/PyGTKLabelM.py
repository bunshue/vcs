# -*- coding:utf-8 -*-
# file: PyGTKLabelM.py
#
import pygtk											# 匯入pygtk模組
pygtk.require('2.0')										# 設定pygtk所需的gtk版本
import gtk											# 匯入gtk模組
class MyWindow():										# 定義視窗類別
	def __init__(self, title, width, height):						# 定義起始化方法
		self.window = gtk.Window()							# 產生視窗物件
		self.window.set_title(title)							# 設定視窗標題
		self.window.set_default_size(width, height)					# 設定視窗大小
		vbox = gtk.VBox(False, 5)							# 產生豎向Box物件
       		hbox1 = gtk.HBox(False, 5)							# 產生水平Box物件
		hbox2 = gtk.HBox(False, 5)
		label1 = gtk.Label('Label1')							# 建立標簽
		label1.set_angle(90)								# 設定標簽角度
		label2 = gtk.Label('Label2')
		label2.set_angle(270)
		label3 = gtk.Label('Label3')
		label4 = gtk.Label('Label4')
		label5 = gtk.Label('Label5')
		hbox1.pack_start(label1)							# 向Box物件中加入標簽
		hbox1.pack_start(label2)
		hbox2.pack_start(label3)
		hbox2.pack_end(label4)
		hbox2.pack_end(label5)
		vbox.pack_start(hbox1)								# 向Box物件中加入其他Box物件
		vbox.pack_start(hbox2)
		self.window.add(vbox)								# 向視窗加入Box物件
		label1.show()									# 顯示標簽
		label2.show()
		label3.show()
		label4.show()
		label5.show()
		hbox1.show()									# 顯示Box物件
		hbox2.show()
		vbox.show()
		self.window.show()								# 顯示視窗
	def main(self):										# 定義main方法
		gtk.main()									# 呼叫gtk.main方法
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()

