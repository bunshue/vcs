# -*- coding:utf-8 -*-
# file: wxPythonPopupMenu.py
#
import wx											# 匯入wxPython
class MyApp(wx.App):										# 透過繼承建立類別
	def OnInit(self):									# 多載OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 產生框架視窗
		self.panel = wx.Panel(frame, -1)						# 產生面板
		menuBar = wx.MenuBar()								# 建立選單條
		self.menu = wx.Menu()								# 建立選單
		open = self.menu.Append(-1, 'Open')
		save = self.menu.Append(-1, 'Save')
		self.menu.AppendSeparator()	
		close = self.menu.Append(-1, 'Close')
		menuBar.Append(self.menu, '&File')
		frame.SetMenuBar(menuBar)							# 向框架視窗中加入選單
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)					# 綁定右鍵事件
		frame.Show()
		return True
	def OnRClick(self, event):
		pos = (event.GetX(),event.GetY())						# 獲得滑鼠點擊座標
		self.panel.PopupMenu(self.menu, pos)						# 顯示選單
app = MyApp()
app.MainLoop()
