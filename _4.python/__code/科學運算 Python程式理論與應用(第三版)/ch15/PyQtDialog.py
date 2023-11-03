# -*- coding:utf-8 -*-
# file: PyQtDialog.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyDialog(QtGui.QDialog):							# 繼承QtGui.QDialog
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.gridlayout = QtGui.QGridLayout()				# 建立佈局元件
		self.label = QtGui.QLabel('Input:')				# 建立標簽
		self.gridlayout.addWidget(self.label, 0, 0)
		self.edit = QtGui.QLineEdit()					# 建立單行文字框
		self.gridlayout.addWidget(self.edit, 0, 1)
		self.ok = QtGui.QPushButton('Ok')				# 建立Ok按鈕
		self.gridlayout.addWidget(self.ok, 1, 0)
		self.cancel = QtGui.QPushButton('Cancel')			# 建立Cancel按鈕
		self.gridlayout.addWidget(self.cancel, 1, 1)
		self.setLayout(self.gridlayout)
		self.connect(self.ok, 						# Ok按鈕事件
				QtCore.SIGNAL('clicked()'),
				self.OnOk)		
		self.connect(self.cancel, 					# Cancel按鈕事件
				QtCore.SIGNAL('clicked()'),
				self.OnCancel)		
	def OnOk(self):								# 處理Ok按鈕事件
		self.text = self.edit.text()					# 取得文字框中內容
		self.done(1)							# 結束交談視窗傳回1
	def OnCancel(self):							# 處理Cancel按鈕事件
		self.done(0)							# 結束交談視窗傳回0
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
			self.button.setText(dialog.text)
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()

