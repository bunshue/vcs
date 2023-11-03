# -*- coding:utf-8 -*-
# file: PyQtButton.py
#
import sys									# 匯入sys模組
from PyQt4 import QtCore, QtGui							# 匯入PyQt模組
class MyWindow(QtGui.QWidget):							# 透過繼承QtGui.QWidget建立類別
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		button1 = QtGui.QPushButton('Button1')				# 產生Button1
		gridlayout.addWidget(button1, 1, 1, 1 ,3)			# 加入Button1
		button2 = QtGui.QPushButton('Button2')				# 產生Button2
		button2.setFlat(True)
		gridlayout.addWidget(button2, 2, 2)				# 加入Button2
		self.setLayout(gridlayout)					# 向視窗中加入佈局元件
app = QtGui.QApplication(sys.argv)						# 建立QApplication物件
mywindow = MyWindow()								# 建立MyWindow物件
mywindow.show()									# 顯示視窗
app.exec_()									# 進入訊息循環
