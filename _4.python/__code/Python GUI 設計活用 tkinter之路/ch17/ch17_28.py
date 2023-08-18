# ch17_28.py
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
def newFile():                      # 開新檔案
    text.delete("1.0",END)          # 刪除Text控件內容
    root.title("Untitled")          # 視窗標題改為Untitled

def openFile():                     # 開啟舊檔
    global filename
    filename = askopenfilename()    # 讀取開啟的檔案
    if filename == "":              # 如果沒有選擇檔案
        return                      # 返回
    with open(filename,"r") as fileObj:     # 開啟檔案
        content = fileObj.read()    # 讀取檔案內容
    text.delete("1.0",END)          # 刪除Text控件內容       
    text.insert(END,content)        # 插入所讀取的檔案
    root.title(filename)            # 更改視窗標題
    
def saveAsFile():                   # 另存新檔
    global filename
    textContent = text.get("1.0",END)
# 開啟另存新檔對話方塊, 預設所存的檔案副檔名是txt
    filename = asksaveasfilename(defaultextension=".txt")
    if filename == "":              # 如果沒有輸入檔案名稱
        return                      # 不往下執行
    with open(filename,"w") as output:
        output.write(textContent)
        root.title(filename)        # 更改root視窗標題
    
filename = "Untitled"                            
root = Tk()
root.title(filename)
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open File ...",command=openFile)
filemenu.add_command(label="Save As ...",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

# 建立Text
text = ScrolledText(root,undo=True)
text.pack(fill=BOTH,expand=True)
    
root.mainloop()












