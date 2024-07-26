# -*- coding:utf-8 -*-
# file: PyQtLineEdit.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):							# 透過繼承QtGui.QWidget建立類別
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		label1 = QtGui.QLabel('Normal Lineedit')			# 建立標簽
		label1.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label1, 0, 0 )
		edit1 = QtGui.QLineEdit()					# 建立單行文字框
		gridlayout.addWidget(edit1, 1, 0)
		label2 = QtGui.QLabel('Password')				# 建立標簽
		label2.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label2, 2, 0)
		edit2 = QtGui.QLineEdit()					# 建立單行文字框
		edit2.setEchoMode(QtGui.QLineEdit.Password)			# 將其設定為密碼框
		gridlayout.addWidget(edit2, 3, 0)
		self.setLayout(gridlayout)	
app = QtGui.QApplication(sys.argv)						# 建立QApplication物件
mywindow = MyWindow()								# 建立MyWindow物件
mywindow.show()									# 顯示視窗
app.exec_()									# 進入訊息循環
