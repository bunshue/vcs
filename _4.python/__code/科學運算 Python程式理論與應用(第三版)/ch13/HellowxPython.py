# -*- coding:utf-8 -*-
# file: HellowxPython.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'Hello,wxPython!')
		frame.Show()
		return True
app = MyApp()
app.MainLoop()