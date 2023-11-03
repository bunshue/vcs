# -*- coding:utf-8 -*-
# file: wxEditor.py
#
import wx											# 匯入wxPython
class CreateMenu():										# 建立選單類別
	def __init__(self, parent):
		self.menuBar = wx.MenuBar()							# 建立選單條
		self.file = wx.Menu()								# 建立選單
		self.open = self.file.Append(-1, '開啟')
		self.save = self.file.Append(-1, '儲存')
		self.saveas = self.file.Append(-1, '另存為')
		self.file.AppendSeparator()	
		self.close = self.file.Append(-1, '離開')
		self.menuBar.Append(self.file, '檔案(&F)')
		self.edit = wx.Menu()
		self.undo = self.edit.Append(-1, '撤消')
		self.redo = self.edit.Append(-1, '重做')
		self.edit.AppendSeparator()
		self.cut = self.edit.Append(-1, '剪下')
		self.copy = self.edit.Append(-1, '複製')
		self.paste = self.edit.Append(-1, '貼上')
		self.edit.AppendSeparator()
		self.selectall = self.edit.Append(-1, '全選')
		self.menuBar.Append(self.edit,'編輯(&E)')
		self.view = wx.Menu()
		self.color = self.view.AppendCheckItem(1051, '設為黑色')
		self.trans = self.view.Append(-1, '設定透明度')
		self.menuBar.Append(self.view, '檢視(&V)')
		self.help = wx.Menu()
		self.about = self.help.Append(-1, '關於')
		self.menuBar.Append(self.help, '幫助(&H)')
		parent.SetMenuBar(self.menuBar)							# 向框架視窗中加入選單

class MyApp(wx.App):										# 透過繼承建立類別
	def OnInit(self):									# 多載OnInit方法
		self.file = ''
		self.width = 600
		self.height = 480
		self.frame = wx.Frame(parent = None,title = 'wxPython Notebook',
				size = (self.width,self.height))				# 產生框架視窗
		self.panel = wx.Panel(self.frame, -1)						# 產生面板
		self.menu = CreateMenu(self.frame)						# 產生選單
		self.text = wx.TextCtrl(self.panel,						# 產生文字框
				-1, 
				pos = (2,2),
				size = (self.width-10, self.height-50),
				style = wx.HSCROLL | wx.TE_MULTILINE)
		self.Bind(wx.EVT_MENU, self.OnOpen, self.menu.open)				# 綁定事件
		self.Bind(wx.EVT_MENU, self.OnSave, self.menu.save)
		self.Bind(wx.EVT_MENU, self.OnSaveAs, self.menu.saveas)
		self.Bind(wx.EVT_MENU, self.OnClose, self.menu.close)
		self.Bind(wx.EVT_MENU, self.OnUndo, self.menu.undo)
		self.Bind(wx.EVT_MENU, self.OnRedo, self.menu.redo)
		self.Bind(wx.EVT_MENU, self.OnCut, self.menu.cut)
		self.Bind(wx.EVT_MENU, self.OnCopy, self.menu.copy)
		self.Bind(wx.EVT_MENU, self.OnPaste, self.menu.paste)
		self.Bind(wx.EVT_MENU, self.OnSelectAll, self.menu.selectall)
		self.Bind(wx.EVT_MENU, self.OnColor, self.menu.color)
		self.Bind(wx.EVT_MENU, self.OnTrans, self.menu.trans)
		self.Bind(wx.EVT_MENU, self.OnAbout, self.menu.about)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)
		self.Bind(wx.EVT_SIZE, self.Resize)
		self.frame.Show()
		return True
	def OnOpen(self, event):								# 處理開啟指令
		dialog = wx.FileDialog(None, 'wxPython Notebook', style = wx.FD_OPEN) 
		if dialog.ShowModal() == wx.ID_OK:
			self.file = dialog.GetPath()
			file = open(self.file)
			self.text.Clear()
			self.text.WriteText(file.read())
			file.close()
		dialog.Destroy()
	def OnSave(self, event):								# 處理儲存指令
		if self.file == '':
			dialog = wx.FileDialog(None, 'wxPython Notebook', style =  wx.FD_SAVE)
			if dialog.ShowModal() == wx.ID_OK:
				self.file = dialog.GetPath()
				self.text.SaveFile(self.file)
			dialog.Destroy()
		else:
			self.text.SaveFile(self.file)
	def OnSaveAs(self, event):								# 處理另存為指令
		dialog = wx.FileDialog(None, 'wxPython Notebook', style =  wx.FD_SAVE)
		if dialog.ShowModal() == wx.ID_OK:
			self.file = dialog.GetPath()
			self.text.SaveFile(self.file)
		dialog.Destroy()
	def OnClose(self, event):								# 處理離開指令
		self.frame.Destroy()
	def OnAbout(self, event):								# 處理關於指令
		wx.MessageBox('A simple editor!', 'wxPython Notebook', wx.OK)
	def OnRClick(self, event):								# 處理右鍵事件
		pos = (event.GetX(),event.GetY())
		self.panel.PopupMenu(self.menu.edit, pos)
	def OnUndo(self, event):								# 處理撤消指令
		self.text.Undo()
	def OnRedo(self, event):								# 處理重做指令
		self.text.Redo()
	def OnCut(self, event):									# 處理剪下指令
		self.text.Cut()
	def OnCopy(self, event):								# 處理複製指令
		self.text.Copy()
	def OnPaste(self, event):								# 處理貼上指令
		self.text.Paste()
	def OnSelectAll(self, event):								# 處理全選指令
		self.text.SelectAll()
	def OnColor(self, event):								# 處理設為黑色指令
		if self.menu.view.IsChecked(1051):
			self.text.SetBackgroundColour('black')
			self.text.SetForegroundColour('green')
			self.text.Refresh()
		else:
			self.text.SetBackgroundColour('white')
			self.text.SetForegroundColour('black')
			self.text.Refresh()
	def OnTrans(self, event):								# 處理設定透明度指令
		r = wx.GetNumberFromUser('請選取透明度','',
				'wxPython Notebook',80, min = 30)
		if r != -1:
			self.frame.SetTransparent((r* 255/100))
			self.frame.Refresh()
	def Resize(self, event):								# 處理視窗改變大小指令
		newsize = self.frame.GetSize()
		width = newsize.GetWidth() - 10
		height = newsize.GetHeight() - 50
		self.text.SetSize((width,height))
		self.text.Refresh()
app = MyApp()
app.MainLoop()
