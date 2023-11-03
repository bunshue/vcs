# -*- coding:utf-8 -*-
# file: PyQtSpacer.py
#
import sys							# 匯入sys模組
from PyQt4 import QtCore, QtGui					# 匯入PyQt模組
class MyWindow(QtGui.QWidget):					# 透過繼承QtGui.QWidget建立類別
	def __init__(self):					# 起始化方法
		QtGui.QWidget.__init__(self)			# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')			# 設定視窗標題
		self.resize(300,200)				# 設定視窗大小
		gridlayout = QtGui.QGridLayout()		# 建立佈局元件
		spacer1 = QtGui.QSpacerItem(300,40)		# 建立空白項
		spacer2 = QtGui.QSpacerItem(300,40)
		label = QtGui.QLabel('Label1',self)		# 建立標簽
		label.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addItem(spacer1, 0 ,0)		# 加入空白項
		gridlayout.addWidget(label, 1, 0)		# 加入標簽
		gridlayout.addItem(spacer2, 2, 0)		# 加入空白項
		self.setLayout(gridlayout)
app = QtGui.QApplication(sys.argv)				# 建立QApplication物件
mywindow = MyWindow()						# 建立MyWindow物件
mywindow.show()							# 顯示視窗
app.exec_()							# 進入訊息循環
