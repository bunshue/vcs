# ch17_25.py
from tkinter import *
from tkinter.filedialog import asksaveasfilename
    
def saveAsFile():
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
filemenu.add_command(label="Save As",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")
    
root.mainloop()












