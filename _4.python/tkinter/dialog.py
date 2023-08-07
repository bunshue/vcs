import tkinter as tk
#from tkinter import _cnfmerge

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

t = tk.Button(None, {'text': 'Test', 'command': open_dialog, tk.Pack: {}})
q = tk.Button(None, {'text': 'Quit', 'command': t.quit, tk.Pack: {}})
t.mainloop()

