# -*- coding:utf-8 -*-
# file: PyGTKGlade.py
#
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
class MyWindow():							# 定義視窗類別
	def __init__(self):						# 定義起始化方法
	        res = gtk.glade.XML('res.glade') 			# 載入資源檔案，產生gtk.glade.XML案例物件
		window = res.get_widget('window')			# 載入window
		signal = { 'OnQuit' : self.OnQuit }			# 建立訊號字典
		res.signal_autoconnect(signal)				# 綁定訊號事件
		window.connect('destroy', lambda q:gtk.main_quit())	# 視窗關閉則離開程式
		window.show()
	def OnQuit(self, widget):					# Quit選單指令處理事件
		gtk.main_quit()
	def main(self):							# 定義main方法
		gtk.main()						# 呼叫gtk.main方法
window = MyWindow()							# 建立視窗物件
window.main()			
