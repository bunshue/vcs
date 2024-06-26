import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

print("------------------------------------------------------------")  # 60個


def openFile(): 
    filenameforReading = askopenfilename()
    infile = open(filenameforReading, "r")
    text.insert(tk.END, infile.read()) # Read all from the file
    infile.close()  # Close the input file

    
def saveFile():
    filenameforWriting = asksaveasfilename()
    outfile = open(filenameforWriting, "w")
    # Write to the file
    outfile.write(text.get(1.0, tk.END)) 
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
frame0.grid(row = 1, column = 1, sticky = tk.W)
        
# Create images
opneImage = tk.PhotoImage(file = "../image/open.gif")
saveImage = tk.PhotoImage(file = "../image/save.gif")

tk.Button(frame0, image = opneImage, command = openFile).grid(row = 1, column = 1, sticky = tk.W)
tk.Button(frame0, image = saveImage, command = saveFile).grid(row = 1, column = 2)

frame1 = tk.Frame(window) # Hold editor pane
frame1.grid(row = 2, column = 1)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
text = tk.Text(frame1, width = 40, height = 20, wrap = tk.WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

window.mainloop()

print("------------------------------------------------------------")  # 60個


import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("簡易文字編輯器")

# 設定主視窗之背景色
window.configure(bg = "#7AFEC6")

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def showPopupMenu(event):
    popupmenu.post(event.x_root,event.y_root)

def undo():
    try:
        text.edit_undo()
    except:
        print("No action")

def redo():
    try:
        text.edit_redo()
    except:
        print("No action")

popupmenu = tk.Menu(window,tearoff = False)
popupmenu.add_command(label = "cut",command = cut)
popupmenu.add_command(label = "copy",command = copy)
popupmenu.add_command(label = "paste",command = paste)

window.bind("<Button-3>",showPopupMenu)

toolbar = tk.Frame(window, relief = "raised", borderwidth = 1)
toolbar.pack(side = "top",fill = "x", padx = 2, pady = 1)

undoBtn = tk.Button(toolbar, text = "Undo", command = undo)
undoBtn.pack(side = "left", pady = 2)
redoBtn = tk.Button (toolbar, text = "Redo", command = redo)
redoBtn.pack(side = "left", pady = 2)

text = tk.Text (window, undo = True)
text.pack(fill = "both", expand = True, padx = 3, pady = 2)
text.insert ('end', "我沒有說謊 我何必說謊\n")
text.insert ('end', "妳懂我的 我對妳從來就不會假裝 \n")
text.insert ('end', "我哪有說謊\n")
text.insert ('end', "請別以為妳有多難忘 笑是真的不是我逞強\n")

window.mainloop()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
