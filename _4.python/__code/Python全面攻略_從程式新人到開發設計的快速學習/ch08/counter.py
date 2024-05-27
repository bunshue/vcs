import tkinter as tk
num = 0
def fnAdd():
    global num		#宣告為全域變數
    num += 1		#num加1
    lblNum['text']=str(num)	#重設標籤文字
    if (num>0):		#若num大於0，就設歸零鈕可以使用
        btnClear['state']='normal'
    
def fnClear():
    global num
    num = 0
    lblNum['text']=str(num)
    btnClear['state']='disabled'  #設歸零鈕不能使用
 
win=tk.Tk()
win.geometry('300x200')
win.title('計數器')
win.configure(bg='white')
lblTitle=tk.Label(win, text = '計數器',font=('標楷體', 16),fg='white',bg='blue')
lblNum=tk.Label(win, text = '0',font=('微軟正黑體', 36))
btnAdd=tk.Button(win, text = '加 1',pady=5,padx=10,command=fnAdd)
btnClear=tk.Button(win, text = '歸零',pady=5,padx=10,command=fnClear,state='disabled')
lblTitle.pack(pady=10,fill='x')
lblNum.pack(pady=20,fill='x')
btnAdd.pack(pady=5, side='left',fill='x', expand=True)
btnClear.pack(pady=5, side='left',fill='x', expand=True)
win.mainloop()

