import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

#DIALOG_ICON = 'warning'
DIALOG_ICON = 'questhead'

class Dialog(tk.Widget):
    def __init__(self, master = None, cnf = {}, **kw):
        cnf = tk._cnfmerge((cnf, kw))
        self.widgetName = '__dialog__'
        tk.Widget._setup(self, master, cnf)
        self.num = self.tk.getint(
                self.tk.call(
                      'tk_dialog', self._w,
                      cnf['title'], cnf['text'],
                      cnf['bitmap'], cnf['default'],
                      *cnf['strings']))
        try: tk.Widget.destroy(self)
        except TclError: pass
    def destroy(self): pass

def open_dialog():
    d = Dialog(None, {'title': 'File Modified',
                      'text':
                      'File "Python.h" has been modified'
                      ' since the last time it was saved.'
                      ' Do you want to save it before'
                      ' exiting the application.',
                      'bitmap': DIALOG_ICON,
                      'default': 0,
                      'strings': ('Save File',
                                  'Discard Changes',
                                  'Return to Editor')})
    print('你選擇了', d.num)


print(tk.TkVersion)

button1 = tk.Button(window, {'text': 'Test', 'command': open_dialog, tk.Pack: {}})
button2 = tk.Button(window, {'text': 'Quit', 'command': window.destroy, tk.Pack: {}})

window.mainloop()

