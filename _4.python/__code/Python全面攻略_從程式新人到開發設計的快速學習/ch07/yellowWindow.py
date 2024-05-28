
#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\grid.py

import tkinter as tk
win=tk.Tk()
win.geometry('200x200')
win.title('grid配置')
win.rowconfigure(0,weight=1)
win.rowconfigure(1,weight=1)
win.rowconfigure(2,weight=1)
win.columnconfigure(0,weight=1)
win.columnconfigure(1,weight=1)
win.columnconfigure(2,weight=1)
lbl1=tk.Label(win, text = '北',font=('標楷體', 40))
lbl2=tk.Label(win, text = '東',font=('標楷體', 40),bg='yellow')
lbl3=tk.Label(win, text = '西',font=('標楷體', 40),bg='lightgreen')
lbl4=tk.Label(win, text = '中',font=('標楷體', 40),bg='pink')
lbl5=tk.Label(win, text = '南',font=('標楷體', 40),bg='lightblue')
lbl1.grid(row=0,column=0,columnspan=2,sticky='nswe')
lbl2.grid(row=0,column=2,rowspan=2,sticky='nswe')
lbl3.grid(row=1,column=0,rowspan=2,sticky='nswe')
lbl4.grid(row=1,column=1,sticky='nswe')
lbl5.grid(row=2,column=1,columnspan=2,sticky='nswe')
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\label.py

import tkinter as tk
win=tk.Tk()
win.geometry('300x200')
win.title('Label標籤')
win.configure(bg='white') 
tk.Label(win, text = 'Label標籤', fg='blue',bg='lightblue',bitmap='gray25',\
         compound='left',font=('標楷體', 24, 'bold')).pack()
msg=('使用Label標籤元件可在視窗上提供各種文字訊息，例如顯示程式執行'
     '過程的提示訊息，或是程式的執行結果。Label元件只能顯示文字資料，'
     '無法接受使用者輸入資料。')
tk.Label(win, text = msg, width=28,wraplength=240,justify='left',\
         pady=10,font=('細明體', 14)).pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\pack.py

import tkinter as tk
win=tk.Tk()
win.geometry('300x200')
win.title('pack配置')
win.configure(bg='white')
lbl1=tk.Label(win, text = '元件版面配置',font=('微軟正黑體', 16),fg='white',bg='blue')
lbl2=tk.Label(win, text = '方法',font=('標楷體', 12))
lbl3=tk.Label(win, text = 'pack()方法',font=('標楷體', 12),bg='lightgreen')
lbl4=tk.Label(win, text = 'grid()方法',font=('標楷體', 12),bg='pink')
lbl5=tk.Label(win, text = 'place()方法',font=('標楷體', 12),bg='lightblue')
lbl1.pack(fill='x')
lbl2.pack(side='left', fill='y')
lbl3.pack(pady=5, fill='both', expand=True)
lbl4.pack(pady=5, fill='both', expand=True)
lbl5.pack(pady=5, fill='both', expand=True)
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\place.py

import tkinter as tk
win=tk.Tk()
win.geometry('300x200')
win.configure(bg='white') 
win.title('place配置')
lbl1=tk.Label(win, text = "五色鳥 Muller's Barbet", font=('微軟正黑體', 18),\
              fg='white',bg='black')
lbl2=tk.Label(win, text = '啄木鳥目', font=('標楷體', 16),fg='blue',bg='lightblue')
lbl3=tk.Label(win, text = '五色鳥科', font=('標楷體', 14),fg='green',bg='lightgreen')
msg='分布海平面到2800公尺，全身為鮮艷的翠綠色，在闊葉林中有良好的保護色。'
lbl4=tk.Label(win, text = msg,font=('細明體', 12),wraplength=170)
lbl1.place(x=10,y=5,width=280,height=40)
lbl2.place(x=10,y=50,width=90,height=50)
lbl3.place(x=10,y=105,width=90,height=50)
lbl4.place(x=110,y=50,width=180,height=105)
win.mainloop()


print("------------------------------------------------------------")  # 60個



import tkinter as tk
win=tk.Tk()
win.geometry('300x200+80+50')
win.title('我的第一個視窗應用程式')
win.resizable(True, False)
win.iconbitmap('first.ico')
win.maxsize(500,200)
win.minsize(100,200)
win.configure(bg='yellow')
win.mainloop()
