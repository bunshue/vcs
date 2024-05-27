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