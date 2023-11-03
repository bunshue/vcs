# -*- coding:utf-8 -*-
# file: WinGUI.py
#
import win32gui
from win32con import *
# 視窗訊息處理函數
def WndProc(hwnd, msg, wParam, lParam):
	if msg == WM_PAINT:
		hdc,ps = win32gui.BeginPaint(hwnd)
		rect = win32gui.GetClientRect(hwnd)
		win32gui.DrawText(hdc,
				'GUI Python',
				len('GUI Python'),
				rect,
				DT_SINGLELINE|DT_CENTER|DT_VCENTER)
		win32gui.EndPaint(hwnd,ps)
	if msg == WM_DESTROY:
		win32gui.PostQuitMessage(0)
	return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)
# 產生視窗類別，並對關聯項給予值       
wc = win32gui.WNDCLASS()
wc.hbrBackground = COLOR_BTNFACE + 1
wc.hCursor = win32gui.LoadCursor(0, IDC_ARROW)
wc.hIcon = win32gui.LoadIcon(0, IDI_APPLICATION)
wc.lpszClassName = "Python on Windows"
wc.lpfnWndProc = WndProc
# 登錄視窗類別
reg = win32gui.RegisterClass(wc)
# 建立視窗
hwnd = win32gui.CreateWindow(
            reg, 'Python', WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT, CW_USEDEFAULT,
            CW_USEDEFAULT, CW_USEDEFAULT,
            0,0, 0, None)
# 顯示視窗
win32gui.ShowWindow(hwnd, SW_SHOWNORMAL)
win32gui.UpdateWindow(hwnd)
# 進入訊息循環，直到視窗結束
win32gui.PumpMessages()

