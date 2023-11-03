# -*- coding:utf-8 -*-
# file: wxPythonButtonEvent.py
#
import wx											# 匯入wxPython
class MyApp(wx.App):										# 透過繼承建立類別
	def OnInit(self):									# 多載OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 產生框架視窗
		panel = wx.Panel(frame, -1)							# 產生面板
		self.button1 = wx.Button(panel, -1, 'Button1', pos=(50, 50))			# 加入Button1
		self.Bind(wx.EVT_BUTTON, 							# 綁定按鈕事件
			self.OnButton1, 							# 指定事件響應函數
			self.button1)								# 指定按鈕
		self.button2 = wx.Button(panel, -1, 'Button2',pos = (150,50))
		self.Bind(wx.EVT_BUTTON,							# 綁定按鈕事件 
			self.OnButton2,                                                         # 指定事件響應函數
			self.button2)								# 指定按鈕
		self.button1.SetDefault()							# 將Button1設定為預設按鈕
		frame.Show()									# 顯示視窗
		return True
	def OnButton1(self, event):								# 按鈕事件響應函數
		self.button2.SetLabel('Button1')						# 變更Button2的文字
		self.button2.SetDefault()							# 將Button2設定為預設按鈕
		self.button1.SetLabel('Button2')						# 變更Button1的文字
	def OnButton2(self, event):								# 按鈕事件響應函數
		self.button1.SetLabel('Button1')						# 變更Button1的文字
		self.button1.SetDefault()							# 將Button1設定為預設按鈕
		self.button2.SetLabel('Button2')						# 變更Button2的文字
app = MyApp()
app.MainLoop()
