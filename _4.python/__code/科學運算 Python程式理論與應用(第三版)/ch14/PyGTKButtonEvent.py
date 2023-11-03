# -*- coding:utf-8 -*-
# file: PyGTKButtonEvent.py
#
import pygtk											# 匯入pygtk模組
pygtk.require('2.0')										# 設定pygtk所需的gtk版本
import gtk											# 匯入gtk模組
class MyWindow():										# 定義視窗類別
	def __init__(self, title, width, height):						# 定義起始化方法
		self.window = gtk.Window()							# 產生視窗物件
		self.window.set_title(title)							# 設定視窗標題
		self.window.set_default_size(width, height)					# 設定視窗大小
		self.window.connect('destroy', lambda w: gtk.main_quit())			# 關閉視窗時離開程式
       		hbox = gtk.HBox(False, 20)							# 產生水平Box物件
		self.button1 = gtk.Button('Button1')						# 建立按鈕
		self.button2 = gtk.Button('Button2')
		self.button1.connect('clicked', self.OnButton1, 'Button1')			# 綁定按鈕事件
		self.button2.connect('clicked', self.OnButton2, 'Button2')
		hbox.pack_start(self.button1)							# 向Box物件中加入按鈕
		hbox.pack_start(self.button2)
		self.window.add(hbox)								# 向視窗加入Box物件
		hbox.show()									# 顯示Box物件
		self.button1.show()								# 顯示按鈕
		self.button2.show()
		self.window.show()								# 顯示視窗
	def main(self):										# 定義main方法
		gtk.main()									# 呼叫gtk.main方法
	def OnButton1(self,widget, data):							# 處理按鈕事件
		self.button2.set_label('Quit')							# 重新設定Button2文字
	def OnButton2(self, widgte, data):							# 處理按鈕事件
		gtk.main_quit()									# 離開程式
window = MyWindow('PyGTK', 150, 30)								# 建立視窗物件
window.main()
