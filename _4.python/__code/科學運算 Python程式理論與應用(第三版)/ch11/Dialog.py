# -*- coding:utf-8 -*-
# file: Dialog.py
#
import win32ui								# 匯入win32ui模組
import win32con 							# 匯入win32con模組
from pywin.mfc import dialog						# 從pywin.mfc匯入dialog
class MyDialog(dialog.Dialog):						# 多載交談視窗起始化方法
	def OnInitDialog(self):						# 呼叫父類別的交談視窗起始化方法
		dialog.Dialog.OnInitDialog(self)			# 多載OnOK方法
	def OnOK(self):							#
		win32ui.MessageBox('Press Ok',	\
				'Python',	\
				win32con.MB_OK)
		self.EndDialog(1)
	def OnCancel(self):						# 多載OnCancel方法
		win32ui.MessageBox('Press Cancel',\
				'Python',	  \
				win32con.MB_OK)
		self.EndDialog(1)
style = (win32con.DS_MODALFRAME  |					# 定義交談視窗型態
	     win32con.WS_POPUP 	 |
	     win32con.WS_VISIBLE |
	     win32con.WS_CAPTION |
	     win32con.WS_SYSMENU |
	     win32con.DS_SETFONT)
childstyle = (win32con.WS_CHILD |					# 定義控制項型態
	  win32con.WS_VISIBLE)
buttonstyle = win32con.WS_TABSTOP | childstyle				# 定義按鈕型態
di = ['Python',								# 設定交談視窗屬性 
	(0,0,300,180),
	style,
	None,
	(8, "MS Sans Serif")]
ButOK = (['Button',							# 設定OK按鈕屬性
	"OK",
	win32con.IDOK,
	(80,150, 50, 14), 
	buttonstyle | win32con.BS_PUSHBUTTON])
ButCancel = (['Button',							# 設定Cancel按鈕屬性
		"Cancel",
		win32con.IDCANCEL,
		(160, 150, 50, 14),
		buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static',							# 設定標簽屬性
		'Python Dialog',
		12,
		(130,50,60,14),
		childstyle])
Edit = (['Edit',							# 設定文字框屬性
		'',
		13,
		(130,80,60,14),
		childstyle|win32con.ES_LEFT|
		win32con.WS_BORDER|win32con.WS_TABSTOP])
init = []								# 起始化訊息清單
init.append(di)
init.append(ButOK)
init.append(ButCancel)
init.append(Stadic)
init.append(Edit)
mydialog = MyDialog(init)						# 產生交談視窗案例物件
mydialog.DoModal()							# 建立交談視窗

