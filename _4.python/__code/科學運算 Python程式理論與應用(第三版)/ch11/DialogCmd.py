# -*- coding:utf-8 -*-
# file: DialogCmd.py
#
import win32ui								# 匯入win32ui模組
import win32con 							# 匯入win32con模組
from pywin.mfc import dialog						# 從pywin.mfc匯入dialog
class MyDialog(dialog.Dialog):						# 透過繼承dialog.Dialog產生交談視窗類別
	def OnInitDialog(self):						# 多載交談視窗起始化方法
		dialog.Dialog.OnInitDialog(self)			# 呼叫父類別的交談視窗起始化方法
		self.HookCommand(self.OnButton1,1051)			# 設定訊息處理方法 
		self.HookCommand(self.OnButton2,1052) 
	def OnButton1(self,wParam,lParam):				# 處理Button1點擊訊息
		win32ui.MessageBox('Button1',	\
				'Python',	\
				win32con.MB_OK)
		self.EndDialog(1)
	def OnButton2(self,lParam,wParam):				# 處理Button2點擊訊息
		text = self.GetDlgItemText(1054)
		win32ui.MessageBox(text,	\
				'Python',	\
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
Button1 = (['Button',							# 設定OK按鈕屬性
	'Button1',
	1051,
	(80,150, 50, 14), 
	buttonstyle | win32con.BS_PUSHBUTTON])
Button2 = (['Button',							# 設定Cancel按鈕屬性
	'Button2',
	1052,
	(160, 150, 50, 14),
	buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static',							# 設定標簽屬性
	'Python Dialog',
	1053,
	(130,50,60,14),
	childstyle])
Edit = (['Edit',							# 設定文字框屬性
	'',
	1054,
	(130,80,60,14),
	childstyle|win32con.ES_LEFT|
	win32con.WS_BORDER|win32con.WS_TABSTOP])
init = []								# 起始化訊息清單
init.append(di)
init.append(Button1)
init.append(Button2)
init.append(Stadic)
init.append(Edit)
mydialog = MyDialog(init)						# 產生交談視窗案例物件
mydialog.DoModal()							# 建立交談視窗



