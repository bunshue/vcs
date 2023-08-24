# ch14_1.py
from tkinter import *
    
pw = PanedWindow(orient=VERTICAL)       # 建立PanedWindow物件
pw.pack(fill=BOTH,expand=True)

top = Label(pw,text="Top Pane")         # 建立標籤Top Pane
pw.add(top)                             # top標籤插入PanedWindow

bottom = Label(pw,text="Bottom Pane")   # 建立標籤Bottom Pane
pw.add(bottom)                          # bottom標籤插入PanedWindow

pw.mainloop()










#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch14\ch14_2.py

# ch14_2.py
from tkinter import *

root = Tk()
root.title("ch14_2")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe)                       # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe)                     # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe)                      # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch14\ch14_3.py

# ch14_3.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch14_3")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe,weight=1)              # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe,weight=1)            # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe,weight=1)             # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch14\ch14_4.py

# ch14_4.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch14_4")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe,weight=2)              # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe,weight=2)            # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe,weight=1)             # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch14\ch14_5.py

# ch14_5.py
from tkinter import *

pw = PanedWindow(orient=HORIZONTAL)     # 建立外層PanedWindow
pw.pack(fill = BOTH,expand=True)

entry = Entry(pw,bd=3)                  # 建立entry            
pw.add(entry)                           # 這是外層PanedWindow的子物件

# 建立PanedWindow物件pwin,這是外層PanedWindow的子物件
pwin = PanedWindow(pw,orient=VERTICAL)  
pw.add(pwin)                            
# 建立Scale,這是pwin物件的子物件
scale = Scale(pwin,orient=HORIZONTAL)   
pwin.add(scale)                         

pw.mainloop()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch14\ch14_6.py

# ch14_6.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch14_6")
root.geometry("300x160")

notebook = Notebook(root)           # 建立Notebook

frame1 = Frame()                    # 建立Frame1
frame2 = Frame()                    # 建立Frame2

notebook.add(frame1,text="頁次1")   # 建立頁次1同時插入Frame1
notebook.add(frame2,text="頁次2")   # 建立頁次2同時插入Frame2
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch14\ch14_7.py

# ch14_7.py
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def msg():
    messagebox.showinfo("Notebook","歡迎使用Notebook")

root = Tk()
root.title("ch14_7")
root.geometry("300x160")

notebook = Notebook(root)           # 建立Notebook

frame1 = Frame()                    # 建立Frame1
frame2 = Frame()                    # 建立Frame2

label = Label(frame1,text="Python") # 在Frame1建立標籤控件
label.pack(padx=10,pady=10)
btn = Button(frame2,text="Help",command=msg) # 在Frame2建立按鈕控件
btn.pack(padx=10,pady=10)

notebook.add(frame1,text="頁次1")   # 建立頁次1同時插入Frame1
notebook.add(frame2,text="頁次2")   # 建立頁次2同時插入Frame2
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()












print('------------------------------------------------------------')	#60個


