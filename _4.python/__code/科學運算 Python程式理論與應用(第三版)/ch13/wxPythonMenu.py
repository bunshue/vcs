# -*- coding:utf-8 -*-
# file: wxPythonMenu.py
#
import wx											# 匯入wxPython
class MyApp(wx.App):										# 透過繼承建立類別
	def OnInit(self):									# 多載OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 產生框架視窗
		panel = wx.Panel(frame, -1)							# 產生面板
		menuBar = wx.MenuBar()								# 建立選單條
		menu = wx.Menu()								# 建立選單
		open = menu.Append(-1, 'Open')							# 向選單中加入Open
		exit = menu.Append(-1, 'Save')							# 向選單中加入Save
		menu.AppendSeparator()								# 向選單中加入分隔符
		close = menu.Append(-1, 'Close')						# 向選單中加入Close
		menuBar.Append(menu, '&File')							# 向選單條中加入File
		menu = wx.Menu()								# 重新建立選單
		copy = menu.Append(-1, 'Copy')							# 向選單中加入Copy
		paste = menu.Append(-1, 'Paste')						# 向選單中加入Paste
		cut = menu.Append(-1, 'Cut')							# 向選單中加入Cut 
		menu.AppendSeparator()								# 向選單中加入分隔符
		selectall = menu.Append(-1, 'SelectAll')					# 向選單中加入SelectAll
		menuBar.Append(menu, '&Edit')							# 向選單條中加入Edit
		menu = wx.Menu()								# 重新建立選單
		about = menu.Append(-1, 'About')						# 向選單中加入About
		menuBar.Append(menu, '&Help')							# 向選單條中加入Help
		frame.SetMenuBar(menuBar)							# 向框架視窗中加入選單
		frame.Show()									# 顯示視窗
		return True
app = MyApp()
app.MainLoop()
