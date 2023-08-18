# ch12_2.py
from tkinter import *
    
root = Tk()
root.title("ch12_2")            # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              # 建立listbox 
lb.insert(END,"Banana")
lb.insert(END,"Watermelon")
lb.insert(END,"Pineapple")
lb.pack(pady=10)

root.mainloop()








