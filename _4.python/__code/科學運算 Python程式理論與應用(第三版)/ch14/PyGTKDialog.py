# -*- coding:utf-8 -*-
# file: PyGTKDialog.py
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
		self.label = gtk.Label('Dialog Example')					# 建立標簽
		self.fixed.put(self.label, 80, 40)						# 加入標簽
		self.button = gtk.Button('CreateDialog')					# 建立按鈕
		self.button.connect('clicked',self.OnButton, 'CreateDialog')			# 綁定按鈕事件
		self.fixed.put(self.button, 80, 130)						# 加入按鈕
		self.window.add(self.fixed)							# 向視窗中加入Fixed
		self.label.show()								# 顯示元件
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):							# 按鈕事件處理函數
		dialog = gtk.Dialog('PyGTK', 							# 建立交談視窗
				None,								# 交談視窗父視窗
				gtk.DIALOG_MODAL,						# 交談視窗標志
                     		(gtk.STOCK_CANCEL, 						# 向交談視窗中加入Cancel按鈕
				gtk.RESPONSE_CANCEL,						# Cancel按鈕的傳回值
                      		gtk.STOCK_OK, 							# 向交談視窗中加入Ok按鈕
				gtk.RESPONSE_OK))						# Ok按鈕的傳回值
		fixed = gtk.Fixed()								# 建立Fixed元件
		dialog.vbox.pack_start(fixed)							# 向交談視窗中的vbox加入Fixed元件
		label = gtk.Label('Input')							# 建立標簽
		fixed.put(label,10,5)								# 向Fixed元件中加入標簽
		entry = gtk.Entry()								# 建立文字框
		fixed.put(entry,50,5)								# 向Fixed元件中加入文字框
		fixed.show()									# 顯示個元件
		label.show()
		entry.show()
		r = dialog.run()								# 顯示交談視窗並取得其傳回值
		if r == gtk.RESPONSE_OK:							# 若果點擊Ok按鈕則輸出文字框中的內容
			print entry.get_text()
		dialog.destroy()
	def main(self):										# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()
