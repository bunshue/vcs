# -*- coding:utf-8 -*-
# file: wxPythonPanel.py
#
import wx								# 匯入wxPython模組
class MyApp(wx.App):							# 透過繼承wx.App類別建立類別
	def OnInit(self):						# 多載OnInit方法
		frame = wx.Frame(parent = None,				# 建立框架視窗
				id=-1, 					# 指定框架ID
				title='Panel', 				# 指定視窗標題
				pos=(100,100),				# 指定視窗位置
				size=(600,480), 			# 指定視窗大小
				style=wx.DEFAULT_FRAME_STYLE,		# 指定視窗型態
				name="frame")				# 指定視窗名
		panel = wx.Panel(frame, -1)				# 向框架視窗加入面板
		frame.Show()						# 顯示框架視窗
		return True						# 傳回True
app = MyApp()								# 類別案例化
app.MainLoop()								# 進入訊息循環
