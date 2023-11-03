# -*- coding:utf-8 -*-
# file: wxPythonStandardDialog.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		self.frame = wx.Frame(parent = None,title = 'wxPython',size = (300,150))		# 產生框架視窗
		panel = wx.Panel(self.frame, -1)							# 產生面板
		self.button1 = wx.Button(panel,-1,'Input String',pos = (100,20))			# 產生按鈕
		self.button2 = wx.Button(panel,-1,'Input Password',pos = (100,70))
		self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)					# 綁定按鈕事件
		self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button2)
		self.frame.Show()
		return True
	def OnButton1(self, event):
		r = wx.GetTextFromUser('wxPython','String', 'Default')					# 建立文字輸入框
		wx.MessageBox(r, 'wxPython',wx.OK)							# 建立MessageBox
	def OnButton2(self, event):
		r = wx.GetPasswordFromUser('wxPython','Password')					# 建立密碼輸入框
		wx.MessageBox(r, 'wxPython',wx.OK)							# 建立MessageBox
app = MyApp()
app.MainLoop()
