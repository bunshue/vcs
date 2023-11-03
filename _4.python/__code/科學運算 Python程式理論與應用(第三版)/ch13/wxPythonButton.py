# -*- coding:utf-8 -*-
# file: wxPythonButton.py
#
import wx									# 匯入wxPython
class MyApp(wx.App):								# 透過繼承建立類別
	def OnInit(self):							# 多載OnInit方法
		frame = wx.Frame(parent = None,title = 'Button')		# 產生框架視窗
		panel = wx.Panel(frame, -1)					# 產生面板
		button = wx.Button(panel,					# 向面板加入按鈕
				-1,						# 指定按鈕ID
				'Button',					# 指定按鈕上的文字
				pos=(50,50))					# 指定按鈕在面板上的位置
		frame.Show()							# 顯示視窗
		return True
app = MyApp()									# 類別案例化
app.MainLoop()									# 進入訊息循環
