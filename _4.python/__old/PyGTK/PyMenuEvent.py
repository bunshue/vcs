# -*- coding:utf-8 -*-
# file: PyMenuEvent.py
#
import pygtk										# 匯入pygtk模組
pygtk.require('2.0')									# 設定pygtk所需的gtk版本
import gtk										# 匯入gtk模組
class MyWindow():									# 定義視窗類別
	def __init__(self, title, width, height):					# 定義起始化方法
		window = gtk.Window()							# 產生視窗物件
		window.set_title(title)							# 設定視窗標題
		window.set_default_size(width, height)					# 設定視窗大小
		window.connect('destroy', lambda q: gtk.main_quit())			# 關閉視窗離開程式
		fixed = gtk.Fixed()							# 建立Fixed元件
		window.add(fixed)
		filemenu = gtk.Menu()							# 建立選單
		open = gtk.MenuItem('Open')						# 建立Open選單指令
		open.show()								# 顯示Open
		open.connect('activate', self.OnOpen, 'Open')				# 綁定選單事件
		close = gtk.MenuItem('Close')						# 建立Close選單指令
		close.connect('activate', self.OnClose, 'Close')			# 綁定選單事件
		close.show()								# 顯示Close
		filemenu.append(open)							# 向選單中加入Open
		filemenu.append(close)							# 向選單中加入Close
        	file = gtk.MenuItem('_File')						# 產生File選單，下劃線表示快速鍵
		file.set_submenu(filemenu)						# 向File選單加入項
        	file.show()								# 顯示File選單
        	menubar = gtk.MenuBar()							# 產生選單條
		menubar.append(file)							# 向選單條中加入File選單
		fixed.put(menubar, 0, 0)						# 向Fixed元件中加入選單條
        	menubar.show()								# 顯示個元件
		fixed.show()
		window.show()
	def OnOpen(self, widget, data):							# 處理選單事件
		dialog = gtk.FileChooserDialog('Open',					# 建立開啟檔案交談視窗
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		response = dialog.run()
		dialog.destroy()
	def OnClose(self, widget, data):						# 處理選單事件
		gtk.main_quit()								# 離開程式
	def main(self):									# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# 建立視窗物件
window.main()
