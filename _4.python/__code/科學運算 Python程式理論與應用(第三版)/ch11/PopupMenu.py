# -*- coding:utf-8 -*-
# file: PopupMenu.py
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
		self.HookMessage(self.OnRClick,WM_RBUTTONDOWN)
	# 多載OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
	# 處理點擊滑鼠右鍵訊息
	def OnRClick(self, param):
		submenu = win32ui.CreatePopupMenu()
		submenu.AppendMenu(MF_STRING,1054,'Copy')				# 向選單中加入Copy
		submenu.AppendMenu(MF_STRING,1055,'Paste')				# 向選單中加入Paste
		submenu.AppendMenu(MF_SEPARATOR,1056,None)				# 向選單中加入分隔符
		submenu.AppendMenu(MF_STRING,1057,'Cut')				# 向選單中加入Cut
		flag = TPM_LEFTALIGN|TPM_LEFTBUTTON|TPM_RIGHTBUTTON 			# 出現式選單型態
		submenu.TrackPopupMenu(param[5],flag,self)				# param為系統向OnRClick函數傳遞的參數，其為一個元群組，其第6項為滑鼠x，y座標群組成的元群組
w = MyWnd()				# 產生視窗物件			
w.ShowWindow()				# 顯示視窗
w.UpdateWindow()			# 更新視窗
w.RunModalLoop(1)			# 進入訊息循環
