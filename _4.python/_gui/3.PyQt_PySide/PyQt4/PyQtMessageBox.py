# -*- coding:utf-8 -*-
# file: PyQtMessageBox.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		self.label = QtGui.QLabel('MessBox example')
		gridlayout.addWidget(self.label, 1, 3, 1, 3)
		self.button1 = QtGui.QPushButton('About')			# 產生Button1
		gridlayout.addWidget(self.button1, 2, 1)
		self.button2 = QtGui.QPushButton('AboutQt')			# 產生Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.button3 = QtGui.QPushButton('Critical')			# 產生Button2
		gridlayout.addWidget(self.button3, 2, 3)
		self.button4 = QtGui.QPushButton('Info')			# 產生Button2
		gridlayout.addWidget(self.button4, 2, 4)
		self.button5 = QtGui.QPushButton('Qusetion')			# 產生Button2
		gridlayout.addWidget(self.button5, 2, 5)
		self.button6 = QtGui.QPushButton('Warning')			# 產生Button2
		gridlayout.addWidget(self.button6, 2, 6)
		spacer = QtGui.QSpacerItem(200, 80)
		gridlayout.addItem(spacer, 3, 1, 1, 5)
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
		self.connect(self.button4, 					# Button4事件
				QtCore.SIGNAL('clicked()'), 
				self.OnButton4)
		self.connect(self.button5, 					# Button5事件
				QtCore.SIGNAL('clicked()'), 
				self.OnButton5)
		self.connect(self.button6, 					# Button6事件
				QtCore.SIGNAL('clicked()'),
				self.OnButton6)	
	def OnButton1(self):							# Button1插槽函數
		self.button1.setText('clicked')
		QtGui.QMessageBox.about(self, 'PyQt', 'About')			# 建立About訊息框
	def OnButton2(self):							# Button2插槽函數
		self.button2.setText('clicked')
		QtGui.QMessageBox.aboutQt(self, 'PyQt')				# 建立AboutQt訊息框
	def OnButton3(self):							# Button3插槽函數
		self.button3.setText('clicked')
		r = QtGui.QMessageBox.critical(self, 'PyQt',			# 建立Ctitical訊息框
				'Critical', 
				QtGui.QMessageBox.Abort,
				QtGui.QMessageBox.Retry,
				QtGui.QMessageBox.Ignore)
		if r == QtGui.QMessageBox.Abort:
			self.label.setText('Abort')
		elif r == QtGui.QMessageBox.Retry:
			self.label.setText('Retry')
		else:
			self.label.setText('Ignore')
	def OnButton4(self):							# Button4插槽函數
		self.button4.setText('clicked')
		QtGui.QMessageBox.information(self, 'PyQt', 'Information')	# 建立Information訊息框
	def OnButton5(self):							# Button5插槽函數
		self.button5.setText('clicked')
		r = QtGui.QMessageBox.question(self, 'PyQt',			# 建立Question訊息框
				'Question', 
				QtGui.QMessageBox.Yes,
				QtGui.QMessageBox.No,
				QtGui.QMessageBox.Cancel)
	def OnButton6(self):							# Button6插槽函數
		self.button6.setText('clicked')
		r = QtGui.QMessageBox.warning(self, 'PyQt',			# 建立Warning訊息框
				'Warning', 
				QtGui.QMessageBox.Yes,
				QtGui.QMessageBox.No)
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()

