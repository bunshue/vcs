# -*- coding:utf-8 -*-
# file: TkinterMessageBox.py
#
import tkinter										# 匯入Tkinter模組
import tkinter.messagebox									# 匯入tkMessageBox模組
def cmd():										# 按鈕訊息處理函數
	global n									# 使用全局變數n
	global buttontext								# 使用全局變數buttontext
	n = n + 1
	if n == 1:									# 判斷n的值，顯示不同的訊息框
		tkinter.messagebox.askokcancel('Python Tkinter','askokcancel')		# 使用askokcancel函數
		buttontext.set('skquestion')						# 變更按鈕上的文字
	elif n == 2:
		tkinter.messagebox.askquestion('Python Tkinter','skquestion')			# 使用askquestion函數
		buttontext.set('askyesno')
	elif n == 3:
		tkinter.messagebox.askyesno('Python Tkinter','askyesno')			# 使用askyesno函數
		buttontext.set('showerror')
	elif n == 4:
		tkinter.messagebox.showerror('Python Tkinter','showerror')			# 使用showerror函數
		buttontext.set('showinfo')
	elif n == 5:
		tkinter.messagebox.showinfo('Python Tkinter','showinfo')			# 使用showinfo函數
		buttontext.set('showwarning')
	else :
		n = 0									# 將n給予值為0重新開始循環
		tkinter.messagebox.showwarning('Python Tkinter','showwarning')		# 使用showwarning函數
		buttontext.set('askokcancel')
n = 0											# 為n賦初值
root = tkinter.Tk()
buttontext = tkinter.StringVar()							# 產生關聯按鈕文字的變數
buttontext.set('askokcancel')								# 設定buttontext值
button = tkinter.Button(root,								# 產生按鈕
		textvariable = buttontext,						# 設定關聯變數
		command = cmd)								# 設定事件處理函數
button.pack()
root.mainloop()										# 進入訊息循環
