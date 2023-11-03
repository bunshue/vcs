# -*- coding:utf-8 -*-
# file: MenuCmd.py
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
			(10, 10, 800, 500), None, 0, None)
		# 建立選單物件
		submenu = win32ui.CreateMenu()
		menu = win32ui.CreateMenu()
		# 向選單中加入Open，其中&表示可以使用Alt+&後的字母存取該選單指令
		submenu.AppendMenu(MF_STRING,1051,'&Open')	
		# 向選單中加入Close
		submenu.AppendMenu(MF_STRING,1052,'&Close')	
		# 向選單中加入Save
		submenu.AppendMenu(MF_STRING,1053,'&Save')
		# 將上面的選單新增到File選單中
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&File')
		# 將選單新增到視窗中
		self._obj_.SetMenu(menu)
		# 設定選單處理訊息
		self.HookCommand(self.MenuClick,1051)
		self.HookCommand(self.MenuClick,1052)
		self.HookCommand(self.MenuClick,1053)
		# 多載OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
	def MenuClick(self,lParam,wParam):
		# 根據lParam參數判斷點擊的選單
		if lParam == 1051:
			self.MessageBox('Open','Python',MB_OK)
		elif lParam == 1053:
			self.MessageBox('Save','Python',MB_OK)
		else:
			self.OnClose()
w = MyWnd()											# 產生視窗物件
w.ShowWindow()											# 顯示視窗
w.UpdateWindow()										# 更新視窗
w.RunModalLoop(1)										# 進入訊息循環


