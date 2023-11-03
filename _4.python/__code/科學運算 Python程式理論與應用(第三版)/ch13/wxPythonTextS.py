# -*- coding:utf-8 -*-
# file: wxPythonTextS.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 產生框架視窗
		panel = wx.Panel(frame, -1)							# 產生面板
		label1 = wx.StaticText(panel, -1, 'wxPython', pos = (120,20))			# 產生標簽
		label2 = wx.StaticText(panel, -1, 'User Name:',pos = (10,50)) 			# 產生標簽
		text = wx.TextCtrl(panel,							# 產生文字框
				-1,  								# 指定文字框ID
				pos = (100,50),							# 指定文字框位置
				size = (160, -1))						# 指定文字框大小
		label3 = wx.StaticText(panel, -1, "Password:",pos = (10,100))			# 產生標簽
		password = wx.TextCtrl(panel,							# 產生文字框
				-1,                                                             # 指定文字框ID
				"password",                                                     # 指定起始文字
				pos = (100,100),						# 指定文字框位置
				size = (160, -1),						# 指定文字框大小
				style=wx.TE_PASSWORD)						# 指定文字框為密碼框
		frame.Show()
		return True
app = MyApp()
app.MainLoop()

