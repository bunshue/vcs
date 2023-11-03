# -*- coding:utf-8 -*-
# file: PyGTKMenu.py
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
		menu_items = (								# 選單
       			     ( '/_File',      None,         None, 0, '<Branch>' ),
       			     ( '/File/Open',  '<control>O', None, 0, None ),
       			     ( '/File/Save',  '<control>S', None, 0, None ),
       			     ( '/File/s',  None,         None, 0, '<Separator>' ),
       			     ( '/File/Close', '<control>Q', None, 0, None ),
       			     ( '/_Edit',      None,         None, 0, '<Branch>' ),
       			     ( '/Edit/Copy',  None,         None, 0, None ),
			     ( '/Edit/Paste',  None,         None, 0, None ),
			     ( '/Edit/s',  None,         None, 0, '<Separator>' ),
			     ( '/Edit/Cut',  None,         None, 0, None ),
       			     ( '/_Help',      None,         None, 0, '<Branch>' ),
       			     ( '/Help/About', None,         None, 0, None ),
       			     )
		accel_group = gtk.AccelGroup()						# 建立快速鍵物件
		itemfactory = gtk.ItemFactory(gtk.MenuBar, '<main>', accel_group)	# 建立ItemFactory物件
        	itemfactory.create_items(menu_items)					# 從選單元群組建立選單
        	window.add_accel_group(accel_group)					# 向視窗中加入快速鍵
        	menubar = gtk.MenuBar()							# 產生選單條
		menubar = itemfactory.get_widget('<main>')				# 獲得選單選單
		fixed.put(menubar, 0, 0)						# 向Fixed元件中加入選單條
        	menubar.show()								# 顯示個元件
		fixed.show()
		window.show()
	def main(self):									# 定義main方法
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# 建立視窗物件
window.main()
