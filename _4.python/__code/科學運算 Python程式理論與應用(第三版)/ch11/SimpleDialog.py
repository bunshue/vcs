# -*- coding:utf-8 -*-
# file: SimpleDialog.py
#
import win32ui							# 匯入Win32ui模組
import win32con							# 匯入win32con模組 
from pywin.mfc import dialog					# 匯入pywin.mfc中的dialog模組
class MyDialog(dialog.Dialog):					# 透過繼承dialog.Dialog產生交談視窗類別
	def OnInitDialog(self):					# 多載起始化函數
		dialog.Dialog.OnInitDialog(self)		# 呼叫父類別的起始化函數
style = (win32con.DS_MODALFRAME  |
	     win32con.WS_POPUP 	 |
	     win32con.WS_VISIBLE |
	     win32con.WS_CAPTION |
	     win32con.WS_SYSMENU |
	     win32con.DS_SETFONT)
di = ['Python',							# 設定交談視窗屬性，設定標題為“Python”
	(0,0,300,180),						# 設定交談視窗位置及大小
	style,							# 設定交談視窗型態
	None,							# 設定交談視窗延伸型態
	(8, "MS Sans Serif")]					# 設定交談視窗字型及大小
init = []							# 定義交談視窗起始化參數清單
init.append(di) 
mydialog = MyDialog(init)					# 產生交談視窗案例物件
mydialog.DoModal()						# 顯示交談視窗	
