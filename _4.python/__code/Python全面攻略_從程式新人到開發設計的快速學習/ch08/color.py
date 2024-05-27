import tkinter as tk

def fnBlue():
    frmColor.config(bg='blue')

def fnRed():
    frmColor.config(bg='red')

def fnGreen():
    frmColor.config(bg='green')  
    
win = tk.Tk()
win.title('顏色切換')
win.geometry('240x200')
frmColor=tk.Frame(win,width=200,height=100,relief='raised',borderwidth=3,bg='white')
frmColor.pack(pady=5)
lfrmBtns=tk.LabelFrame(win,text='顏色')
lfrmBtns.pack(pady=20,fill='x')
btnBlue=tk.Button(lfrmBtns,text='藍色',width=8,command=fnBlue).pack(side='left',padx=5)
btnRed=tk.Button(lfrmBtns,text='紅色',width=8,command=fnRed).pack(side='left',padx=5)
btnGreen=tk.Button(lfrmBtns,text='綠色',width=8,command=fnGreen).pack(side='left',padx=5)
win.mainloop()
