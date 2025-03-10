# -*- coding:utf-8 -*-
# file: HelloPyQt.py
#
import sys							# 匯入sys模組
from PyQt4 import QtCore, QtGui					# 匯入PyQt模組
class MyWindow(QtGui.QMainWindow):				# 透過繼承QtGui.QMainWindow建立類別
	def __init__(self):					# 起始化方法
		QtGui.QMainWindow.__init__(self)		# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')			# 設定視窗標題
		self.resize(300,200)				# 設定視窗大小
app = QtGui.QApplication(sys.argv)				# 建立QApplication物件
mywindow = MyWindow()						# 建立MyWindow物件
mywindow.show()							# 顯示視窗
app.exec_()							# 進入訊息循環
