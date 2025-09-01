# -*- coding:utf-8 -*-
# file: PyQtRes.py
#
import sys
from PyQt4 import QtCore, QtGui, uic	
class MyDialog(QtGui.QDialog):							# 繼承QtGui.QDialog
	def __init__(self):
		QtGui.QWidget.__init__(self)
		uic.loadUi("res.ui", self)	

class MyWindow(QtGui.QWidget):
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		self.button = QtGui.QPushButton('CreateDialog')			# 產生Button1
		gridlayout.addWidget(self.button, 1, 1)
		self.setLayout(gridlayout)					# 向視窗中加入佈局元件
		self.connect(self.button, 					# Button事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton)
	def OnButton(self):							# 處理按鈕事件		
		dialog = MyDialog()						# 建立交談視窗物件
		r = dialog.exec_()						# 執行交談視窗
		if r:
			self.button.setText(dialog.lineEdit.text())
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
