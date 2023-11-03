# -*- coding:utf-8 -*-
# file: PyQtRCButton.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		self.label1 = QtGui.QLabel('Label1')				# 建立標簽
		self.label2 = QtGui.QLabel('Label2')
		gridlayout.addWidget(self.label1, 1, 2)
		gridlayout.addWidget(self.label2, 2, 2)
		self.radio1 = QtGui.QRadioButton('Radio1')			# 建立單選框
		self.radio2 = QtGui.QRadioButton('Radio2')
		self.radio3 = QtGui.QRadioButton('Radio3')
		self.radio1.setChecked(True)					# 將Radio1勾選
		gridlayout.addWidget(self.radio1, 1, 1 )			# 加入單選框
		gridlayout.addWidget(self.radio2, 2, 1 )
		gridlayout.addWidget(self.radio3, 3, 1 )
		self.check = QtGui.QCheckBox('check')				# 建立復選框
		self.check.setChecked(True)					# 將復選框勾選
		gridlayout.addWidget(self.check, 3, 2)
		self.button = QtGui.QPushButton('Test')				# 建立按鈕
		gridlayout.addWidget(self.button, 4, 1, 1, 2)
		self.setLayout(gridlayout)					# 向視窗中加入佈局元件
		self.connect(self.button, 					# 按鈕事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton)
	def OnButton(self):							# 按鈕插槽函數
		if self.radio1.isChecked():					# 判斷單選框是否勾選
			self.label1.setText('Radio1')
		elif self.radio2.isChecked():
			self.label1.setText('Radio2')
		else :
			self.label1.setText('Radio3')
		if self.check.isChecked():					# 判斷復選框是否勾選
			self.label2.setText('checked')
		else:
			self.label2.setText('uncheck')
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()		
mywindow.show()		
app.exec_()	
