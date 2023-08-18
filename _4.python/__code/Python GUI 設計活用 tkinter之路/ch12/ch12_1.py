# ch12_1.py
from tkinter import *
    
root = Tk()
root.title("ch12_1")                            # 視窗標題
root.geometry("300x210")                        # 視窗寬300高210

lb1 = Listbox(root)                             # 建立listbox 1
lb1.pack(side=LEFT,padx=5,pady=10)
lb2 = Listbox(root,height=5,relief="raised")    # 建立listbox 2
lb2.pack(anchor=N,side=LEFT,padx=5,pady=10)

root.mainloop()








