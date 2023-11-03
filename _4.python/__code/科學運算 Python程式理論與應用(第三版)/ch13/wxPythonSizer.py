# -*- coding:utf-8 -*-
# file: wxPythonSizer.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 產生框架視窗
		panel = wx.Panel(frame, -1)									# 產生面板
		sizer = wx.GridSizer(rows=3,cols=3,vgap=0,hgap=0)			# 建立一個三行三列的sizer
		sizer.AddSpacer(0)											# 向sizer中加入一個空項
		label = wx.StaticText(panel, -1, 'label')					# 產生標簽
		sizer.Add(label,flag = wx.ALIGN_CENTER)						# 向sizer加入標簽置中對齊
		sizer.AddSpacer(0)	
		button1 = wx.Button(panel, -1, 'Button1')					# 產生按鈕
		sizer.Add(button1,flag = wx.ALIGN_CENTER)					# 向sizer中加入按鈕
		sizer.AddSpacer(0)
		button2 = wx.Button(panel, -1, 'Button2')					# 產生按鈕
		sizer.Add(button2,flag = wx.ALIGN_CENTER)					# 向sizer中加入按鈕
		sizer.AddSpacer(0)
		text = wx.TextCtrl(panel, -1, size = (100,20))				# 產生文字框
		sizer.Add(text)												# 向sizer中加入文字框
		sizer.AddSpacer(0)
		panel.SetSizer(sizer)										# 向面板中加入sizer
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
