# -*- coding:utf-8 -*-
# file: PyGTKStandardDialog.py
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
		self.label1 = gtk.Label('StandardDialog Example')				# 建立標簽
		self.fixed.put(self.label1, 80, 40)						# 加入標簽
		self.button1 = gtk.Button('FileChooser')						# 建立按鈕
		self.button1.connect('clicked',self.OnButton1, 'FileChooser')			# 綁定按鈕事件
		self.button2 = gtk.Button('FontChooser')						# 建立按鈕
		self.button2.connect('clicked',self.OnButton2, 'FontChooser')			# 綁定按鈕事件
		self.button3 = gtk.Button('ColorChooser')						# 建立按鈕
		self.button3.connect('clicked',self.OnButton3, 'ColorChooser')			# 綁定按鈕事件
		self.fixed.put(self.button1, 10, 130)						# 加入按鈕
		self.fixed.put(self.button2, 95, 130)						# 加入按鈕
		self.fixed.put(self.button3, 190, 130)						# 加入按鈕
		self.window.add(self.fixed)							# 向視窗中加入Fixed
		self.label1.show()								# 顯示元件
		self.button1.show()
		self.button2.show()
		self.button3.show()
		self.fixed.show()
		self.window.show()
	def OnButton1(self, widget, data):							# 按鈕事件處理函數
		dialog = gtk.FileChooserDialog('Open',						# 建立檔案開啟交談視窗
                               None,								# 設定父視窗
                               gtk.FILE_CHOOSER_ACTION_OPEN,					# 設定交談視窗標志
                               (gtk.STOCK_CANCEL, 						# 加入Cancel按鈕
				gtk.RESPONSE_CANCEL,						# Cancel按鈕的傳回值
                                gtk.STOCK_OPEN, 						# 加入Open按鈕
				gtk.RESPONSE_OK))						# Open按鈕的傳回值
		filter = gtk.FileFilter()							# 產生gtk.FileFilter物件
		filter.set_name('All files')							# 加入檔案型態名
		filter.add_pattern('*')								# 即所有檔案
		dialog.add_filter(filter)							# 向交談視窗中加入gtk.FileFilter物件
		filter = gtk.FileFilter()							# 產生gtk.FileFilter物件
		filter.set_name('Python')							# 加入檔案型態名
		filter.add_pattern('*.py')							# 加入檔案副檔名
		filter.add_pattern('*.pyw')							# 加入檔案副檔名
		dialog.add_filter(filter)							# 向視窗中加入gtk.FileFilter物件
		r = dialog.run()								# 顯示交談視窗
		if r == gtk.RESPONSE_OK:
			print dialog.get_filename()
		dialog.destroy()								# 銷毀交談視窗
	def OnButton2(self, widget, data):							# 按鈕事件處理函數
		fontdlg = gtk.FontSelectionDialog('Choose Font')				# 建立字型勾選交談視窗
		r = fontdlg.run()								# 顯示交談視窗
		if r == gtk.RESPONSE_OK:
			print fontdlg.get_font_name()
		fontdlg.destroy()								# 銷毀交談視窗
	def OnButton3(self, widget, data):							# 按鈕事件處理函數
            	colordlg = gtk.ColorSelectionDialog('Choose Color')				# 建立彩色選取交談視窗
		colordlg.colorsel.set_has_palette(True)						# 顯示調色板
            	response = colordlg.run()							# 顯示交談視窗
            	if response == gtk.RESPONSE_OK:
            	    print colordlg.colorsel.get_current_color()
            	colordlg.destroy()								# 銷毀交談視窗
	def main(self):										# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# 建立視窗物件
window.main()

