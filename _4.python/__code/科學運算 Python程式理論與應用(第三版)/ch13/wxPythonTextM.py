# -*- coding:utf-8 -*-
# file: wxPythonTextM.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (600,400))		# 產生框架視窗
		panel = wx.Panel(frame, -1)							# 產生面板
		label1 = wx.StaticText(panel, -1, 'MultiLine', pos = (280,10))			# 產生標簽
		text1 = wx.TextCtrl(panel,							# 產生文字框
				-1,  								# 指定文字框ID
				pos = (10,30),							# 指定文字框位置
				size = (580, 150),style=wx.TE_MULTILINE)			# 指定文字框大小
		label2 = wx.StaticText(panel, -1, 'RichText', pos = (280,190))			# 產生標簽
		text2 = wx.TextCtrl(panel,							# 產生文字框
				-1,                                                             # 指定文字框ID
				'Python wxPython',                                              # 指定起始文字
				pos = (10,210),							# 指定文字框位置
				size = (580, 150),						# 指定文字框大小
				style =wx.TE_MULTILINE|wx.TE_RICH)				# 指定文字框為密碼框
		text2.SetStyle(0, 6, wx.TextAttr('red', 'blue'))
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
