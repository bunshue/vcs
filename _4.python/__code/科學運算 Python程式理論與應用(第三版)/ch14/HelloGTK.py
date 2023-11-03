# -*- coding:utf-8 -*-
# file: HelloGTK.py
#
import pygtk					# 匯入pygtk模組
pygtk.require('2.0')				# 設定pygtk所需的gtk版本
import gtk					# 匯入gtk模組
window = gtk.Window()				# 建立視窗物件
window.set_title('PyGTK')			# 設定視窗標題
window.set_default_size(300, 200)		# 設定視窗大小
window.show()					# 顯示視窗
gtk.main()					# 進入訊息循環
