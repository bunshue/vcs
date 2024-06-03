'''
取得Clipboard內的資料

'''

import tkinter as tk


print('取得Clipboard內的資料')

clipboard_data = tk.Tk().clipboard_get()
print(clipboard_data)

