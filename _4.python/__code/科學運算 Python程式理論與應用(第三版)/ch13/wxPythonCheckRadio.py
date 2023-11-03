# -*- coding:utf-8 -*-
# file: wxPythonCheckRadio.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 產生框架視窗
		panel = wx.Panel(frame, -1)							# 產生面板
		self.radio1 = wx.RadioButton(panel, 						# 產生單選框
				-1, 								# 指定單選框ID
				'Radio1',							# 指定單選框文字
				pos=(10, 40),							# 指定單選框位置
				style=wx.RB_GROUP)						# 指定單選框型態
		self.radio2 = wx.RadioButton(panel,						# 產生框架視窗
				-1, 								# 指定單選框ID
				'Radio2',							# 指定單選框文字
				pos=(10, 80))							# 指定單選框位置
		self.radio3 = wx.RadioButton(panel, 						# 產生單選框
				-1, 								# 指定單選框ID
				'Radio3', 							# 指定單選框文字
				pos=(10, 120))							# 指定單選框位置
		self.check = wx.CheckBox(panel, 						# 產生復單選框
				-1, 								# 指定復單選框ID
				'CheckBox',							# 指定復單選框文字
				pos = (120, 40),						# 指定復選框位置
				size = (150, 20))						# 指定復選框大小
		self.button1 = wx.Button(panel,-1,'Radio',pos = (120,80))			# 產生按鈕
		self.button2 = wx.Button(panel,-1,'Check',pos = (120,120))
		self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)				# 綁定按鈕事件
		self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button2)
		frame.Show()
		return True
	def OnButton1(self, event):								# 按鈕事件處理方法
		if self.radio1.GetValue():							# 判斷Radio1是否勾選
			self.button1.SetLabel('Radio1')
		elif self.radio2.GetValue():							# 判斷Radio2是否勾選
			self.button1.SetLabel('Radio2')
		else:
			self.button1.SetLabel('Radio3')
	def OnButton2(self, event):								# 按鈕事件處理方法
		if self.check.IsChecked():							# 判斷CheckBox是否勾選
			self.button2.SetLabel('Checked')
		else:
			self.button2.SetLabel('UnChecke')
app = MyApp()
app.MainLoop()
