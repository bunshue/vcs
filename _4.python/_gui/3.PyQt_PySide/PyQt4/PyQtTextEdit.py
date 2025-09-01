# -*- coding:utf-8 -*-
# file: PyQtTextEdit.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):							# 透過繼承QtGui.QWidget建立類別
	def __init__(self):							# 起始化方法
		QtGui.QWidget.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')					# 設定視窗標題
		self.resize(300,200)						# 設定視窗大小
		gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		label = QtGui.QLabel('TextEdit')				# 建立標簽
		label.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label, 0, 0 )
		edit = QtGui.QTextEdit()					# 建立多行文字框
		edit.setText('Python\nPyQt')					# 設定文字框中的文字
		gridlayout.addWidget(edit, 1, 0)
		self.setLayout(gridlayout)	
app = QtGui.QApplication(sys.argv)						# 建立QApplication物件
mywindow = MyWindow()								# 建立MyWindow物件
mywindow.show()									# 顯示視窗
app.exec_()									# 進入訊息循環

