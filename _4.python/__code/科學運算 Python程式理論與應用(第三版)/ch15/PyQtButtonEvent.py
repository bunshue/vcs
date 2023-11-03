# -*- coding:utf-8 -*-
# file: PyQtButtonEvent.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		self.button1 = QtGui.QPushButton('Button1')			# 產生Button1
		gridlayout.addWidget(self.button1, 1, 1, 1 ,3)
		self.button2 = QtGui.QPushButton('Button2')			# 產生Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.setLayout(gridlayout)					# 向視窗中加入佈局元件
		self.connect(self.button1, 					# Button1事件
				QtCore.SIGNAL('clicked()'), 			# clicked()訊號
				self.OnButton1)					# 插槽函數
		self.connect(self.button2, 					# Button2事件
				QtCore.SIGNAL('clicked()'), 			# clicked()訊號
				self.OnButton2)					# 插槽函數
	def OnButton1(self):							# Button1插槽函數
		self.button1.setText('clicked')
	def OnButton2(self):							# Button2插槽函數
		self.button2.setText('clicked')
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()		
mywindow.show()		
app.exec_()	
