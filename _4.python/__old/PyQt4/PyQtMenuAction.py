# -*- coding:utf-8 -*-
# self.file: PyQtMenuAction.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QMainWindow):							# 透過繼承QtGui.QMainWindow建立類別
	def __init__(self):								# 起始化方法
		QtGui.QMainWindow.__init__(self)					# 呼叫父類別起始化方法
		self.setWindowTitle('PyQt')						# 設定視窗標題
		self.resize(300,200)							# 設定視窗大小
		self.label = QtGui.QLabel('Menu Action')				# 建立標簽
		self.label.setAlignment(QtCore.Qt.AlignCenter)				# 設定標籤文字對齊型態
		self.setCentralWidget(self.label)
		menubar = self.menuBar()						# 獲得視窗的選單條
		self.file = menubar.addMenu('&File')					# 加入File選單
		open = self.file.addAction('Open')					# 加入Open指令
		self.connect(open, QtCore.SIGNAL('triggered()'), self.OnOpen)		# 選單訊號
		save = self.file.addAction('Save')					# 加入Save指令
		self.connect(save, QtCore.SIGNAL('triggered()'), self.OnSave)		# 選單訊號
		self.file.addSeparator()						# 加入分隔符
		close = self.file.addAction('Close')					# 加入Close指令
		self.connect(close, QtCore.SIGNAL('triggered()'), self.OnClose)		# 選單訊號
	def OnOpen(self):								# 處理Open指令
		self.label.setText('Menu Action: Open')
	def OnSave(self):								# 處理Save指令
		self.label.setText('Menu Action: Save')
	def OnClose(self):								# 處理Close指令
		self.close()
	def contextMenuEvent(self, event):						# 多載出現式選單事件
        	self.file.exec_(event.globalPos())
app = QtGui.QApplication(sys.argv)							# 建立QApplication物件
mywindow = MyWindow()									# 建立MyWindow物件
mywindow.show()										# 顯示視窗
app.exec_()										# 進入訊息循環
