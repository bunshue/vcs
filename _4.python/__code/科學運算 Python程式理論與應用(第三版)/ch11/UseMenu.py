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
		submenu = win32ui.CreateMenu()
		# 向選單中加入Copy
		submenu.AppendMenu(MF_STRING,1054,'&Copy')
		# 向選單中加入Paste
		submenu.AppendMenu(MF_STRING,1055,'&Paste')	
		# 向選單中加入分隔符
		submenu.AppendMenu(MF_SEPARATOR,1056,None)
		# 向選單中加入Cut
		submenu.AppendMenu(MF_STRING,1057,'C&ut')
		# 將上面的選單新增到Edit選單中
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&Edit')
		submenu = win32ui.CreateMenu()
		# 向選單中加入Tools
		submenu.AppendMenu(MF_STRING,1058,'Tools')
		# 向選單中加入Settings
		submenu.AppendMenu(MF_STRING|MF_GRAYED,1059,'Setting')
		m = win32ui.CreateMenu()
		# 將上面的選單新增到Option選單中
		m.AppendMenu(MF_STRING|MF_POPUP|MF_CHECKED,submenu.GetHandle(),'Option')
		# 將Option選單新增到Other選單中
		menu.AppendMenu(MF_STRING|MF_POPUP,m.GetHandle(),'&Other')
		# 將選單新增到視窗中
		self._obj_.SetMenu(menu)
	# 多載OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
w = MyWnd()											# 產生視窗物件
w.ShowWindow()											# 顯示視窗
w.UpdateWindow()										# 更新視窗
w.RunModalLoop(1)										# 進入訊息循環

