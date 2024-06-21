"""
# 以Menu元件建置功能表

"""

import sys
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個
'''
window = tk.Tk()
window.geometry("400x300")

#建立功能選單
menu = tk.Menu(window)
window.config(menu = menu)   #顯示功能表單

#第1排功能選單
menu1 = tk.Menu(menu, tearoff = False)
menu1.add_command(label = 'New', command = lambda: print('你按了 New'))
menu1.add_command(label = 'Open', command = lambda: print('你按了 Open'))
menu1.add_separator()
menu.add_cascade(label = 'File', menu = menu1)

#第2排功能選單
menu2 = tk.Menu(menu, tearoff = False)
menu2.add_command(label = 'Help entry', command = lambda: print("你按了", help_check_string.get()))

help_check_string = tk.StringVar()
menu2.add_checkbutton(label = 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label = 'Help', menu = menu2)

#第3排功能選單
# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm
menu3 = tk.Menu(menu, tearoff = False)
menu3.add_command(label = 'exercise test 1')
menu.add_cascade(label = 'Exercise', menu = menu3)

menu3b = tk.Menu(menu, tearoff = False)
menu3b.add_command(label = 'some more stuff')
menu3.add_cascade(label = 'more stuff', menu = menu3b)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

#建立功能選單
menu = tk.Menu(window)
window.config(menu = menu)   #顯示功能表單

#第1排功能選單
menu1 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Operation", menu = menu1)
menu1.add_command(label = "Add", command = lambda: print('你按了 Add'))
menu1.add_command(label = "Substract", command = lambda: print('你按了 Substract'))
menu1.add_separator()
menu1.add_command(label = "Multiply", command = lambda: print('你按了 Multiply'))
menu1.add_command(label = "Divide", command = lambda: print('你按了 Divide'))

#第2排功能選單
menu2 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Exit", menu = menu2)
menu2.add_command(label = "Quit", command = window.destroy)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

#建立功能選單
menu = tk.Menu(window)
window.config(menu = menu)   #顯示功能表單

#第1排功能選單
#menu1 = tk.Menu(menu)
menu1 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "File", menu = menu1)
menu1.add_command(label = "Open", command = lambda: print('你按了 Open'))
menu1.add_command(label = "Save", command = lambda: print('你按了 Save'))
menu1.add_separator()
menu1.add_command(label = "Exit", command = window.destroy)

#第2排功能選單
menu2 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Edit", menu = menu2)
menu2.add_command(label = "Cut", command = lambda: print('你按了 Cut'))
menu2.add_command(label = "Copy", command = lambda: print('你按了 Copy'))
menu2.add_command(label = "Paste", command = lambda: print('你按了 Paste'))

#第3排功能選單
#menu3 = tk.Menu(menu)
menu3 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Help", menu = menu3)
menu3.add_command(label = "About...", command = lambda: print('你按了 About...'))

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

def supermode():
    print('super mode!')

menu = tk.Menu(window)

menu1 = tk.Menu(menu)

menu1.add_command(label = 'supermode', command = supermode)

menu.add_cascade(label = 'Operation', menu = menu1)

window.config(menu = menu)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menu = tk.Menu(window)

menu1 = tk.Menu(menu)

menu.add_cascade(label = 'File', menu = menu1)

menu1.add_command(label = 'open', command = lambda: print('你按了 open'))

menu1.add_separator()

menu1.add_command(label = 'exit', command = window.destroy)

menu2 = tk.Menu(menu)

menu.add_cascade(label = 'Edit', menu = menu2)

menu2.add_command(label = 'find', command = lambda: print('你按了 find'))

window.config(menu = menu)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

print('GUI介面-Menu')

# 1.產生功能表物件menuBar
menuBar = tk.Menu(window)

# 2.將功能表物件menuBar佈置到主視窗的頂部
window.config(menu = menuBar)

# 3.加入主功能表項目
menu_file = tk.Menu(menuBar, tearoff = 0)
menu_font = tk.Menu(menuBar, tearoff = 0)
menu_help = tk.Menu(menuBar, tearoff = 0)

# 4. 產生主功能項目實體
menuBar.add_cascade(label = '檔案', menu = menu_file)
menuBar.add_cascade(label = '字體大小', menu = menu_font)
menuBar.add_cascade(label = '版權宣告', menu = menu_help)

# 5-1. 加入'檔案'功能表下拉選單
menu_file.add_command(label = '開啟新檔',
        underline = 1, accelerator = 'Ctrl+N',
        command = lambda: print('你按了 開啟新檔'))
menu_file.add_command(label = '開啟',
        underline = 1, accelerator = 'Ctrl+O',
        command = lambda: print('你按了 開啟舊檔'))
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '儲存',
        underline = 1, accelerator = 'Ctrl+S',
        command = lambda: print('你按了 另存新檔'))
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '離開',
        underline = 1, accelerator = 'Ctrl+Q',
        command = lambda : window.destroy())

# 5-2. 加入'字體大小'功能表下拉選單
labels = ('大', '中', '小')
for item in labels:
    menu_font.add_radiobutton(label = item)

# 5-3. 加入'版權宣告'功能表下拉選單
menu_help.add_command(label = '關於', command = lambda: print('你按了 關於'))

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)

# File menu
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='檔案', menu=filemenu)
filemenu.add_command(label='開啟新檔', command= lambda: print('你按了 開啟新檔'))
filemenu.add_command(label='開啟舊檔', command= lambda: print('你按了 開啟舊檔'))
filemenu.add_command(label='另存為', command= lambda: print('你按了 另存為'))
filemenu.add_separator()
filemenu.add_command(label='結束', command = window.destroy)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='編輯', menu=editmenu)
editmenu.add_command(label='剪下', command= lambda: print('你按了 剪下'))
editmenu.add_command(label='複製', command= lambda: print('你按了 複製'))
editmenu.add_command(label='貼上', command= lambda: print('你按了 貼上'))

# About menu
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='說明', menu=helpmenu)
helpmenu.add_command(label='關於', command= lambda: print('你按了 關於'))

window.config(menu=menubar)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window,tearoff=0)
window.config(menu = menubar)
file_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "檔案", menu = file_menu)
file_menu.add_command(label = "開啟舊檔")  
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
edit_menu.add_command(label = "復原") 
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
run_menu.add_command(label = "編譯及執行本程式")
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label=' 檔案', menu=filemenu)

filemenu.add_command(label='開啟檔案', command= lambda: print('你按了 開啟檔案'))

window.config(menu=menubar)

window.mainloop()

print('------------------------------------------------------------')	#60個

"""
生成選單視窗，需要的檔案結構如下：

檔案：
	開啟新檔
	開啟舊檔
	另存為
	結束
編輯：
	剪下
	複製
	貼上
說明：
	關於

"""

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command= lambda: print('你按了 Open'))
filemenu.add_separator()
filemenu.add_command(label='Exit', command= window.destroy)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Find', command= lambda: print('你按了 Find'))
window.config(menu=menubar)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)
window.config(menu=menubar)
menu_file = tk.Menu(menubar, tearoff = 0)
menu_cal  = tk.Menu(menubar, tearoff = 0)
menu_help = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='檔案', menu=menu_file)
menubar.add_cascade(label='計算', menu=menu_cal)
menubar.add_cascade(label='Help', menu=menu_help)
menu_file.add_command(label='離開', command = window.destroy)
menu_cal.add_command(label='計算', command = lambda: print('你按了 計算'))
menu_cal.add_command(label='檢視', command = lambda: print('你按了 檢視'))
menu_help.add_command(label='關於', command = lambda: print('你按了 關於'))

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter.messagebox as tkmessagebox
import tkinter.filedialog as tkfiledialog

def Cal():
    options = {}
    options['filetypes'] = [("allfiles","*"),("text","*.txt")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:
        f = open(fs.name,'r')
        fc = f.readlines()
        f.close()
        fo = open('output.txt','w')
        fo.write("試題分析結果\n")
        pitem = int(fc[0][0:3])
        fo.write('題數:'+str(pitem)+'\n')
        pmiss = fc[0][4:5]
        fo.write('缺失:'+pmiss+'\n')
        pomit = fc[0][6:7]
        fo.write('遺漏:'+pomit+'\n')
        pid   = int(fc[0][8:10])
        fo.write('ID長度:'+str(pid)+'\n')
        pans  = fc[1]
        fo.write('答案:'+pans)
        pnum  = len(fc)-2
        fo.write('人數:'+str(pnum)+'\n')        
        psitem = []
        for j in range(0, pitem, 1):
            psitem.append(0)
        for i in range(0,pnum, 1):            
            for j in range(0,pitem, 1):                
                if (fc[2+i][pid+j]==pans[j]):                    
                    psitem[j] = psitem[j]+1                
        for j in range(0, pitem):
            fo.write('第'+str(j+1).rjust(2,'0')+'題，難度值p='+str(round(psitem[j]/pnum,2)).ljust(4,'0')+'\n')
        fo.close()
        tkmessagebox.showinfo(title="試題分析", message="分析完成")
    else:
        print ("沒有選擇檔案")

def View():
    options = {}
    options['filetypes'] = [("allfiles","*")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:        
        f = open(fs.name,'r')
        fc= f.readlines()
        f.close()
        ptext = tk.Text(window, width=800, height=600)        
        for i in range(0, len(fc), 1):
            ptext.insert(tk.INSERT, fc[i])        
        ptext.pack()
        ptext.config(state=tk.DISABLED)       
    else:
        print ("沒有選擇檔案")

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)
window.config(menu=menubar)
menu_file = tk.Menu(menubar, tearoff = 0)
menu_cal  = tk.Menu(menubar, tearoff = 0)
menu_help = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='檔案', menu=menu_file)
menubar.add_cascade(label='計算', menu=menu_cal)
menubar.add_cascade(label='Help', menu=menu_help)
menu_file.add_command(label='結束', command = window.destroy)
menu_cal.add_command(label='計算', command=Cal)
menu_cal.add_command(label='檢視', command=View)
menu_help.add_command(label='關於', command = lambda: print('你按了 關於'))

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def openFile(): 
    filenameforReading = askopenfilename()
    infile = open(filenameforReading, "r")
    text.insert("end", infile.read()) # Read all from the file
    infile.close()  # Close the input file
    
def saveFile():
    filenameforWriting = asksaveasfilename()
    outfile = open(filenameforWriting, "w")
    # Write to the file
    outfile.write(text.get(1.0, "end")) 
    outfile.close() # Close the output file

window = tk.Tk()
window.geometry("400x300")
window.title("簡易文字編輯器")
        
menubar = tk.Menu(window)
window.config(menu = menubar) # Display the menu bar
        
# create a pulldown menu, and add it to the menu bar
operationMenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = operationMenu)
operationMenu.add_command(label = "Open", command = openFile)
operationMenu.add_command(label = "Save", command = saveFile)
        
# Add a tool bar frame 
frame0 = tk.Frame(window) # Create and add a frame to window
frame0.grid(row = 1, column = 1, sticky = "W")

# Create images
opneImage = tk.PhotoImage(file = "__new/open.gif")
saveImage = tk.PhotoImage(file = "__new/save.gif")
        
tk.Button(frame0, image = opneImage, command = openFile).grid(row = 1, column = 1, sticky = "W")
tk.Button(frame0, image = saveImage, command = saveFile).grid(row = 1, column = 2)

frame1 = tk.Frame(window) # Hold editor pane
frame1.grid(row = 2, column = 1)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = "right", fill = "y")
text = tk.Text(frame1, width = 40, height = 20, wrap = "word", yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")
window.title("簡易文字編輯器")

def supermode():
    print('super mode!')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)
filemenu.add_command(label='supermode', command=supermode)
menubar.add_cascade(label='Operation', menu=filemenu)
window.config(menu=menubar)

window.mainloop()

print('------------------------------------------------------------')	#60個

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Application")
        self.create_menu()
        self.pack()

    def create_menu(self):
        # 建立主功能表
        menubar = tk.Menu(self.master)

        # 建立檔案主功能
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="開啟檔案", command=self.open_file)
        file_menu.add_command(label="儲存檔案", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="結束", command=self.master.quit)
        menubar.add_cascade(label="檔案", menu=file_menu)

        # 建立編輯主功能
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="複製", command=self.copy)
        edit_menu.add_command(label="剪下", command=self.cut)
        edit_menu.add_command(label="貼上", command=self.paste)
        menubar.add_cascade(label="編輯", menu=edit_menu)

        # 建立執行主功能
        run_menu = tk.Menu(menubar, tearoff=0)
        run_menu.add_command(label="執行程式", command=self.run)
        menubar.add_cascade(label="執行", menu=run_menu)

        # 建立線上說明主功能
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="使用說明", command=self.show_help)
        menubar.add_cascade(label="線上說明", menu=help_menu)

        # 設定主功能表
        self.master.config(menu=menubar)

    def open_file(self):
        print("你按了 開啟檔案")

    def save_file(self):
        print("你按了 儲存檔案")

    def copy(self):
        print("你按了 複製")

    def cut(self):
        print("你按了 剪下")

    def paste(self):
        print("你按了 貼上")

    def run(self):
        print("你按了 執行程式")

    def show_help(self):
        print("你按了 使用說明")

window = tk.Tk()
window.geometry("400x300")
window.title("簡易文字編輯器")

# 建立應用程式
app = Application(master=window)

# 執行主迴圈
app.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menu = tk.Menu(window)						# 產生選單
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Open")					# 向下拉選單中加入Open指令
submenu.add_command(label="Save")					# 向下拉選單中加入Save指令
submenu.add_command(label="Close")					# 向下拉選單中加入Close指令
menu.add_cascade(label="File", menu=submenu)				# 將下拉選單新增到選單中
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Copy")					# 向下拉選單中加入Copy指令
submenu.add_command(label="Paste")					# 向下拉選單中加入Paste指令
submenu.add_separator()							# 向下拉選單中加入分隔符
submenu.add_command(label="Cut")					# 向下拉選單中加入Cut指令
menu.add_cascade(label="Edit", menu=submenu)				# 將下拉選單新增到選單中
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="About")					# 向下拉選單中加入About指令
menu.add_cascade(label="Help", menu=submenu)				# 將下拉選單新增到選單中
window.config(menu=menu)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立最上層功能表
menubar = tk.Menu(window)
menubar.add_command(label="Hello!",command= lambda: print('你按了 Hello'))
menubar.add_command(label="Exit!",command=window.destroy)
window.config(menu=menubar)           # 顯示功能表物件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command= lambda: print('你按了 開新檔案'))
filemenu.add_command(label="Exit!",command=window.destroy)
window.config(menu=menubar)           # 顯示功能表物件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command= lambda: print('你按了 開新檔案'))
filemenu.add_command(label="Exit!",command=window.destroy)
window.config(menu=menubar)           # 顯示功能表物件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="開新檔案",command= lambda: print('你按了 開新檔案'))
filemenu.add_command(label="開啟舊檔",command= lambda: print('你按了 開啟舊檔'))
filemenu.add_separator()
filemenu.add_command(label="儲存檔案",command= lambda: print('你按了 儲存檔案'))
filemenu.add_command(label="另存新檔",command= lambda: print('你按了 另存新檔'))
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=window.destroy)
window.config(menu=menubar)           # 顯示功能表物件

window.mainloop()

print("------------------------------------------------------------")  # 60個
    
window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="開新檔案",command = lambda: print('你按了 開新檔案'))
filemenu.add_command(label="開啟舊檔",command = lambda: print('你按了 開啟舊檔'))
filemenu.add_separator()
filemenu.add_command(label="儲存檔案",command = lambda: print('你按了 儲存檔案'))
filemenu.add_command(label="另存新檔",command = lambda: print('你按了 另存新檔'))
filemenu.add_separator()
filemenu.add_command(label="離開",command = window.destroy)
# 建立功能表類別物件,和將此功能表類別命名Help 
helpmenu = tk.Menu(menubar)               
menubar.add_cascade(label="Help",menu=helpmenu)
# 在Help功能表內建立功能表清單
helpmenu.add_command(label="關於",command = lambda: print('你按了 關於'))
window.config(menu=menubar)           # 顯示功能表物件

window.mainloop()

print("------------------------------------------------------------")  # 60個
    
window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
filemenu.add_command(label="開新檔案",command = lambda: print('你按了 開新檔案'),underline=0)
filemenu.add_command(label="開啟舊檔",command = lambda: print('你按了 開啟舊檔'),underline=0)
filemenu.add_separator()
filemenu.add_command(label="儲存檔案",command = lambda: print('你按了 儲存檔案'),underline=0)
filemenu.add_command(label="另存新檔",command = lambda: print('你按了 另存新檔'),underline=5)
filemenu.add_separator()
filemenu.add_command(label="離開",command=window.destroy,underline=0)
# 建立功能表類別物件,和將此功能表類別命名Help 
helpmenu = tk.Menu(menubar)               
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
# 在Help功能表內建立功能表清單
helpmenu.add_command(label="About",command = lambda: print('你按了 開新檔案'),underline=1)
window.config(menu=menubar)           # 顯示功能表物件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
filemenu.add_command(label="開新檔案",command= lambda: print('你按了 開新檔案'), accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="離開",command=window.destroy,underline=0)
window.config(menu=menubar)           # 顯示功能表物件

window.bind("<Control-N>",            # 快捷鍵綁定
          lambda event:messagebox.showinfo("New File","開新檔案"))

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                        # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
# 首先在File功能表內建立find子功能表物件
findmenu = tk.Menu(filemenu,tearoff=False)     # 取消分隔線
findmenu.add_command(label="尋找下一筆",command= lambda: print('你按了 尋找下一筆'))
findmenu.add_command(label="尋找上一筆",command= lambda: print('你按了 尋找上一筆'))
filemenu.add_cascade(label="Find",menu=findmenu)
# 下列是增加分隔線和建立Exit!指令
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=window.destroy,underline=0)

window.config(menu=menubar)                   # 顯示功能表物件

window.mainloop()

'''

print("------------------------------------------------------------")  # 60個


def status():                       # 設定是否顯示狀態列
    if demoStatus.get():
        statusLabel.pack(side=tk.BOTTOM,fill=tk.X)
    else:
        statusLabel.pack_forget()
       
window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單Exit
filemenu.add_command(label="Exit",command=window.destroy)
# 建立功能表類別物件,和將此功能表類別命名View 
viewmenu = tk.Menu(menubar,tearoff=False)               
menubar.add_cascade(label="View",menu=viewmenu)
# 在View功能表內建立Check menu button
demoStatus = tk.BooleanVar()
demoStatus.set(True)
viewmenu.add_checkbutton(label="Status",command=status, variable=demoStatus)
window.config(menu=menubar)           # 顯示功能表物件

statusVar = tk.StringVar()
statusVar.set("顯示")
statusLabel = tk.Label(window,textvariable=statusVar,relief="raised")
statusLabel.pack(side=tk.BOTTOM,fill=tk.X)

window.mainloop()

print("------------------------------------------------------------")  # 60個
       
window = tk.Tk()
window.geometry("400x300")

menubar = tk.Menu(window)                    # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = tk.Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單Exit
filemenu.add_command(label="Exit",command=window.destroy)

# 建立工具列
toolbar = tk.Frame(window,relief=tk.RAISED,borderwidth=3)
# 在工具列內建立按紐
sunGif = tk.PhotoImage(file="__new/sun.gif")
exitBtn = tk.Button(toolbar,image=sunGif,command=window.destroy)
exitBtn.pack(side=tk.LEFT,padx=3,pady=3)   # 包裝按鈕

toolbar.pack(side=tk.TOP,fill=tk.X)           # 包裝工具列
window.config(menu=menubar)               # 顯示功能表物件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立選單畫面
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="save", command= lambda: print('你按了 save'))
filemenu.add_separator()
filemenu.add_command(label="exit", command= window.destroy)
window.config(menu=menubar)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

def newfile():
    print('你按了 newfile');
    
def savefile():
    print('你按了 savefile');
   
def about():
    print('你按了 about');

window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 7')

menu = tk.Menu(window)                 # 建立功能表物件
window.config(menu=menu)

filemenu = tk.Menu(menu)               # 建立檔案功能表
menu.add_cascade(label="檔案",menu=filemenu)
filemenu.add_command(label="開新檔案",command=newfile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="儲存檔案",command=savefile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="結束",command=window.destroy)

helpmenu = tk.Menu(menu)               # 建立說明功能表
menu.add_cascade(label="說明",menu=helpmenu)
helpmenu.add_command(label="程式說明",command=about)

window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




