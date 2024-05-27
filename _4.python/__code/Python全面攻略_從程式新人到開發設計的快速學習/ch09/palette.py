import tkinter as tk

def fnBg(e):
    red=r.get()	#用get()方法讀取刻度值
    green=g.get()
    blue=b.get()
    color='#{:02x}{:02x}{:02x}'.format(red,green,blue)
    frmColor.config(bg=color)
    
win = tk.Tk()
win.title('調色盤')
win.geometry('250x200')
frmColor=tk.Frame(win,width=100,height=180,relief='raised',borderwidth=3,bg='white')
frmColor.pack(side='left',padx=10)
frmRGB=tk.Frame(win,width=200,height=200)
frmRGB.pack(side='left')
r=tk.IntVar()
sclR=tk.Scale(frmRGB,label='紅：',orient='horizontal',variable=r,from_=0,to=255,command=fnBg)
r.set(255)	#用set()方法設定刻度值
sclR.pack()
g=tk.IntVar()
sclG=tk.Scale(frmRGB,label='綠：',orient='horizontal',variable=g,from_=0,to=255,command=fnBg)
sclG.pack()
g.set(255)
b=tk.IntVar()
sclB=tk.Scale(frmRGB,label='藍：',orient='horizontal',variable=b,from_=0,to=255,command=fnBg)
sclB.pack()
b.set(255)
win.mainloop()
