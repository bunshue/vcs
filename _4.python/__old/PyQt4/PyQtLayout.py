# -*- coding:utf-8 -*-
# file: PyQtLayout.py
#
import sys							# 匯入sys模組
from PyQt4 import QtCore, QtGui					# 匯入PyQt模組
class MyWindow(QtGui.QWidget):					# 透過繼承QtGui.QWidget建立類別
	def __init__(self):					# 起始化方法
		QtGui.QWidget.__init__(self)			# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')			# 設定視窗標題
		self.resize(300,200)				# 設定視窗大小
		gridlayout = QtGui.QGridLayout()		# 建立佈局元件
		hboxlayout1 = QtGui.QHBoxLayout()
		hboxlayout2 = QtGui.QHBoxLayout()
		vboxlayout1 = QtGui.QVBoxLayout()
		vboxlayout2 = QtGui.QVBoxLayout()
		label1 = QtGui.QLabel('Label1',self)		# 建立標簽
		label1.setAlignment(QtCore.Qt.AlignCenter)
		label2 = QtGui.QLabel('Label2')
		label3 = QtGui.QLabel('Label3')
		label4 = QtGui.QLabel('Label4')
		label5 = QtGui.QLabel('Label5')
		hboxlayout1.addWidget(label1)			# 向佈局元件中加入標簽
		vboxlayout1.addWidget(label2)
		vboxlayout1.addWidget(label3)
		vboxlayout2.addWidget(label4)
		vboxlayout2.addWidget(label5)
		hboxlayout2.addLayout(vboxlayout1)		# 向hboxlayout2加入vboxlayout1
		hboxlayout2.addLayout(vboxlayout2)		# 向hboxlayout2加入vboxlayout2
		gridlayout.addLayout(hboxlayout1, 0 ,0)		# 向第一行第一列加入hboxlayout1
		gridlayout.addLayout(hboxlayout2, 1, 0)		# 向第二行第一列加入hboxlayout2
		gridlayout.setRowMinimumHeight (1, 180)		# 設定第二行的最小高度為108
		self.setLayout(gridlayout)
app = QtGui.QApplication(sys.argv)				# 建立QApplication物件
mywindow = MyWindow()						# 建立MyWindow物件
mywindow.show()							# 顯示視窗
app.exec_()							# 進入訊息循環
