# -*- coding:utf-8 -*-
# file: DllRes.py
#
import win32ui							# 匯入Win32ui模組
import win32con							# 匯入win32con模組 
from pywin.mfc import dialog					# 匯入pywin.mfc中的dialog模組
class MyDialog(dialog.Dialog):					# 透過繼承dialog.Dialog產生交談視窗類別
	def OnInitDialog(self):					# 多載起始化函數
		dialog.Dialog.OnInitDialog(self)		# 呼叫父類別的起始化函數
	def OnOK(self):						# 多載OnOK方法
		win32ui.MessageBox('Press Ok',	\
				'Python',	\
				win32con.MB_OK)	
		self.EndDialog(1)
	def OnCancel(self):					# 多載OnCancel方法
		win32ui.MessageBox('Press Cancel',\
				'Python',	  \
				win32con.MB_OK)
		self.EndDialog(1)	
dll = win32ui.LoadLibrary('Res.dll')
l = win32ui.LoadDialogResource(7000,dll)
mydialog = MyDialog(l)						# 產生交談視窗案例物件
mydialog.DoModal()						# 顯示交談視窗	
