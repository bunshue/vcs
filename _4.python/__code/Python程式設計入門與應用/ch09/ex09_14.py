# Filename: ex09_14.py
import tkinter as tk
import tkinter.messagebox as tkmessagebox
import tkinter.font as tkfont
def Cal():
    tkmessagebox.showinfo(title="計算", message="計算資料中的試題難度")
def View():
    tkmessagebox.showinfo(title="檢視", message="檢視計算的結果")    
def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")
def Exit():
    win.destroy() 
def main():
    global win
    win = tk.Tk()
    win.geometry("800x600")
    win.title("試題與測驗分析程式")
    default_font = tkfont.nametofont('TkDefaultFont')
    default_font.configure(size=15)
    menubar = tk.Menu(win)
    win.config(menu=menubar)
    menu_file = tk.Menu(menubar, tearoff = 0)
    menu_cal  = tk.Menu(menubar, tearoff = 0)
    menu_help = tk.Menu(menubar, tearoff = 0)    
    menubar.add_cascade(label='檔案', menu=menu_file)
    menubar.add_cascade(label='計算', menu=menu_cal)
    menubar.add_cascade(label='Help', menu=menu_help)
    menu_file.add_command(label='結束', command=Exit)
    menu_cal.add_command(label='計算', command=Cal)
    menu_cal.add_command(label='檢視', command=View)
    menu_help.add_command(label='關於', command=About)
    win.mainloop()
main()