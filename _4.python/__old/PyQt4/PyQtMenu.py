# -*- coding:utf-8 -*-
# file: PyQtMenu.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QMainWindow):						# 透過繼承QtGui.QMainWindow建立類別
	def __init__(self):							# 起始化方法
		QtGui.QMainWindow.__init__(self)				# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		menubar = self.menuBar()					# 獲得視窗的選單條
		file = menubar.addMenu('&File')					# 加入File選單
		file.addAction('Open')						# 加入Open指令
		file.addAction('Save')						# 加入Save指令
		file.addSeparator()						# 加入分隔符
		file.addAction('Close')						# 加入Close指令
		edit = menubar.addMenu('&Edit')					# 加入Edit選單
		edit.addAction('Copy')						# 加入Copy指令
		edit.addAction('Paste')						# 加入Paste指令
		edit.addAction('Cut')						# 加入Cut指令
		edit.addAction('SelectAll')					# 加入SelectAll指令
		help = menubar.addMenu('&Help')					# 加入Help選單
		help.addAction('About')						# 加入About指令
app = QtGui.QApplication(sys.argv)						# 建立QApplication物件
mywindow = MyWindow()								# 建立MyWindow物件
mywindow.show()									# 顯示視窗
app.exec_()									# 進入訊息循環
