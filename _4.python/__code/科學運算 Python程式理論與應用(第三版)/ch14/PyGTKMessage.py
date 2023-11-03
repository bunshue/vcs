# -*- coding:utf-8 -*-
# file: PyGTKMessage.py
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
		self.label = gtk.Label('MessageDialog Example')					# 建立標簽
		self.fixed.put(self.label, 80, 20)						# 加入標簽
		self.button = gtk.Button('Create')						# 建立按鈕
		self.button.connect('clicked',self.OnButton, 'Create')				# 綁定按鈕事件
		self.fixed.put(self.button, 120, 150)						# 加入按鈕
		self.window.add(self.fixed)							# 向視窗中加入Fixed
		self.label.show()								# 顯示元件
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):
		msg = gtk.MessageDialog(self.window, 						# 建立訊息框
				gtk.DIALOG_MODAL, 						# 訊息框標志
				gtk.MESSAGE_INFO, 						# 訊息框型態
				gtk.BUTTONS_OK, 						# 訊息框按鈕
				'An example')							# 訊息框中的內容
        	msg.run()									# 顯示訊息框
       		msg.destroy()									# 銷毀訊息框
	def main(self):										# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()
