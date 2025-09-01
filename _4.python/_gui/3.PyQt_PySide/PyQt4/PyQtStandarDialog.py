# -*- coding:utf-8 -*-
# file: PyQtStandarDialog.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		self.label = QtGui.QLabel('StandarDialog example')
		gridlayout.addWidget(self.label, 1, 2)
		self.button1 = QtGui.QPushButton('File')			# 產生Button1
		gridlayout.addWidget(self.button1, 2, 1)
		self.button2 = QtGui.QPushButton('Font')			# 產生Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.button3 = QtGui.QPushButton('Color')			# 產生Button2
		gridlayout.addWidget(self.button3, 2, 3)
		spacer = QtGui.QSpacerItem(200, 80)
		gridlayout.addItem(spacer, 3, 1, 1, 3)
		self.setLayout(gridlayout)					# 向視窗中加入佈局元件
		self.connect(self.button1, 					# Button1事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton1)
		self.connect(self.button2, 					# Button2事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton2)
		self.connect(self.button3, 					# Button3事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton3)
	def OnButton1(self):			
		self.button1.setText('clicked')
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open')	# 建立檔案開啟交談視窗
		if not filename.isEmpty():
			self.label.setText(filename)
	def OnButton2(self):							# Button2插槽函數
		self.button2.setText('clicked')
		font, ok = QtGui.QFontDialog.getFont()				# 建立字型勾選交談視窗
		if ok:
			self.label.setText(font.key())
	def OnButton3(self):							# Button3插槽函數
		self.button3.setText('clicked')
		color = QtGui.QColorDialog.getColor()				# 建立彩色選取交談視窗
		if color.isValid(): 
			self.label.setText(color.name())
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
