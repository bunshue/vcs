# -*- coding:utf-8 -*-
# file: wxPythonDialog.py
#
import wx											# 匯入wxPython
class MyApp(wx.App):										# 透過繼承建立類別
	def OnInit(self):									# 多載OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 產生框架視窗
		panel = wx.Panel(frame, -1)							# 產生面板
		self.button = wx.Button(panel, -1, 'Show Dialog', pos=(100, 50))		# 加入Button
		self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)
		frame.Show()									# 顯示視窗
		return True
	def OnButton(self, event):								# 按鈕事件響應函數
		dialog = MyDialog()
		r = dialog.ShowModal()								# 取得傳回值
		if r == wx.ID_OK:								# 判斷是否點選交談視窗的Ok按鈕
			wx.MessageBox('You input:' + dialog.text.GetValue(),			# 出現訊息框
					'wxPython', wx.OK)
		dialog.Destroy()								# 銷毀交談視窗
class MyDialog(wx.Dialog):									# 定義交談視窗類別
	def __init__(self):									# 起始化
		wx.Dialog.__init__(self, None, -1, 'wxDilog',size=(300, 170))			# 呼叫父類別的起始化方法
		label = wx.StaticText(self, -1, 'Simple Dialog',pos = (120,20))			# 產生標簽
		self.text = wx.TextCtrl(self, -1, pos = (100,50), size = (160, -1))		# 產生文字框
		self.ok = wx.Button(self, wx.ID_OK, "OK", pos=(50, 80))				# 產生OK按鈕	
		self.cancel = wx.Button(self, wx.ID_CANCEL, "Cancel",pos=(200, 80))		# 產生Cancel按鈕
app = MyApp()
app.MainLoop()
