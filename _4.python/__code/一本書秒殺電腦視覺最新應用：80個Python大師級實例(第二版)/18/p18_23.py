from tkinter import *
abc = Tk()
abc.title('创建文本框右键菜单')
abc.resizable(False, False)
abc.geometry("300x100+200+20")
Label(abc, text='被生成的文本框').pack(side="top")
Label(abc).pack(side="top")
show = StringVar()
Entry = Entry(abc, textvariable=show, width="30")
Entry.pack() 
class section:
    def onPaste(self):
        try:
            self.text = abc.clipboard_get()
        except TclError:
            pass
        show.set(str(self.text))
 
    def onCopy(self):
        self.text = Entry.get()
        abc.clipboard_append(self.text)
 
    def onCut(self):
        self.onCopy()
        try:
            Entry.delete('sel.first', 'sel.last')
        except TclError:
            pass 
section = section()
menu = Menu(abc, tearoff=0)
menu.add_command(label="复制", command=section.onCopy)
menu.add_separator()
menu.add_command(label="粘贴", command=section.onPaste)
menu.add_separator()
menu.add_command(label="剪切", command=section.onCut) 
 
def popupmenu(event):
    menu.post(event.x_root, event.y_root)
Entry.bind("<Button-3>", popupmenu)
abc.mainloop()
