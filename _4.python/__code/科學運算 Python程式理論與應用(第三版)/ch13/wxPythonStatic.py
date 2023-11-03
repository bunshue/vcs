# -*- coding:utf-8 -*-
# file: wxPythonStatic.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 產生框架視窗
		panel = wx.Panel(frame, -1)							# 產生面板
		label1 = wx.StaticText(panel,							# 產生標簽
				-1, 								# 指定標簽ID
				'Python', 							# 指定標簽中文字
				size = (160,20),						# 指定標簽大小
				pos = (60,10),							# 指定標簽位置
				style = wx.ALIGN_RIGHT)						# 指定標簽型態，齊右
		label2 = wx.StaticText(panel,							# 產生標簽
				-1, 								# 指定標簽ID
				'Python',							# 指定標簽中文字
				size = (160,20),						# 指定標簽大小
				pos = (60,50),							# 指定標簽位置
				style = wx.ALIGN_CENTER)					# 指定標簽型態，劇中對齊
		label2.SetForegroundColour('red')						# 指定標簽前景色
		label2.SetBackgroundColour('black')						# 指定標簽背景色
		label3 = wx.StaticText(panel,							# 產生標簽
				-1, 								# 指定標簽ID
				'Python\nwxPython',						# 在文字中使用換行符
				size = (160,40),						# 指定標簽大小
				pos = (60,90))							# 指定標簽位置
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
