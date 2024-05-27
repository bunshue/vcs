import tkinter as tk

def fnEnd():
    res = tk.messagebox.askokcancel('注意','確定要結束程式嗎？')
    if(res == True):	#若傳回值為 True
        win.destroy()   #結束程式執行
        
win=tk.Tk()
win.geometry('300x150')
win.title('對話方塊')
lblTitle=tk.Label(win, text = '按鈕結束程式',font=('標楷體', 16))
btnEnd=tk.Button(win, text = '結束',pady=5,padx=10,command=fnEnd)
lblTitle.pack(pady=20)
btnEnd.pack(pady=5)
win.mainloop()

