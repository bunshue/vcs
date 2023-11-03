# -*- coding:utf-8 -*-
# file: MFCGUI.py
#
import win32ui
import win32api
from win32con import *
from pywin.mfc import window
# 定義視窗類別
class MyWnd(window.Wnd):
	def __init__ (self):
		window.Wnd.__init__(self, win32ui.CreateWnd ())
		self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE, \
			win32ui.RegisterWndClass(0, 0, COLOR_WINDOW + 1), \
				'MFC GUI', WS_OVERLAPPEDWINDOW, \
				(100, 100, 400, 300), None, 0, None)
	# 多載OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
	# 多載OnPaint方法，在視窗中輸出“MFC GUI”
	def OnPaint(self):
		dc,ps = self.BeginPaint()
		dc.DrawText('MFC GUI',
			self.GetClientRect(),
			DT_SINGLELINE | DT_CENTER | DT_VCENTER)
		self.EndPaint(ps)

w = MyWnd()				# 產生視窗物件			
w.ShowWindow()				# 顯示視窗
w.UpdateWindow()			# 更新視窗
w.RunModalLoop(1)			# 進入訊息循環
