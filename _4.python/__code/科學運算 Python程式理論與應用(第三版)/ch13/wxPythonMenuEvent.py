# -*- coding:utf-8 -*-
# file: wxPythonMenuEvent.py
#
import wx											# 匯入wxPython
class MyApp(wx.App):										# 透過繼承建立類別
	def OnInit(self):									# 多載OnInit方法
		self.frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))	# 產生框架視窗
		self.panel = wx.Panel(self.frame, -1)						# 產生面板
		menuBar = wx.MenuBar()								# 建立選單條
		self.menu = wx.Menu()								# 建立選單
		open = self.menu.Append(-1, 'Open')
		save = self.menu.Append(-1, 'Save')
		self.menu.AppendSeparator()	
		close = self.menu.Append(-1, 'Close')
		menuBar.Append(self.menu, '&File')
		self.menu = wx.Menu()								# 重新建立選單
		about = self.menu.Append(-1, 'About')
		menuBar.Append(self.menu, '&Help')
		self.frame.SetMenuBar(menuBar)							# 向框架視窗中加入選單
		self.Bind(wx.EVT_MENU, self.OnOpen, open)					# 綁定選單事件
		self.Bind(wx.EVT_MENU, self.OnSave, save)
		self.Bind(wx.EVT_MENU, self.OnClose, close)
		self.Bind(wx.EVT_MENU, self.OnAbout, about)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)
		self.frame.Show()
		return True
	def OnOpen(self, event):								# 處理Open指令
		dialog = wx.FileDialog(None, 'wxPython', style = wx.FD_OPEN) 			# 建立開啟檔案交談視窗
		dialog.ShowModal()
		dialog.Destroy()
	def OnSave(self, event):								# 處理Save指令
		dialog = wx.FileDialog(None, 'wxPython', style =  wx.FD_SAVE)			# 建立儲存檔案交談視窗
		dialog.ShowModal()
		dialog.Destroy()
	def OnClose(self, event):								# 處理Close指令
		self.frame.Destroy()								# 離開程式
	def OnAbout(self, event):								# 處理About指令
		wx.MessageBox('wxPython Menu Event', 'wxPython', wx.OK)				# 建立訊息框
	def OnRClick(self, event):								# 處理右鍵事件
		pos = (event.GetX(),event.GetY())
		self.panel.PopupMenu(self.menu, pos)						# 建立出現式選單
app = MyApp()
app.MainLoop()
