# -*- coding:utf-8 -*-
# file: PyGTKMenuItem.py
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
		close = gtk.MenuItem('Close')						# 建立Close選單指令
		close.show()								# 顯示Close
		filemenu.append(open)							# 向選單中加入Open
		filemenu.append(close)							# 向選單中加入Close
        	file = gtk.MenuItem('_File')						# 產生File選單，下劃線表示快速鍵
		file.set_submenu(filemenu)						# 向File選單加入項
        	file.show()								# 顯示File選單
		editmenu = gtk.Menu()							# 建立選單
		copy = gtk.MenuItem('Copy')						# 建立Copy選單指令
		copy.show()								# 顯示Copy
		paste = gtk.MenuItem('Paste')						# 建立Paste選單指令
		paste.show()								# 顯示Paste
		editmenu.append(copy)							# 向選單中加入Copy
		editmenu.append(paste)							# 向選單中加入Paste
		edit = gtk.MenuItem('_Edit')						# 產生Edit選單
		edit.set_submenu(editmenu)						# 向Edit選單中加入項
		edit.show()								# 顯示Edit選單
        	menubar = gtk.MenuBar()							# 產生選單條
		menubar.append(file)							# 向選單條中加入File選單
        	menubar.append(edit)							# 向選單條中加入Edit選單
		fixed.put(menubar, 0, 0)						# 向Fixed元件中加入選單條
        	menubar.show()								# 顯示個元件
		fixed.show()
		window.show()
	def main(self):									# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# 建立視窗物件
window.main()
