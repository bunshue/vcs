print("------------------------------------------------------------")  # 60個
print("Python 發送資料、vcs接收資料")
print("------------------------------------------------------------")  # 60個

import sys
import ctypes
import tkinter as tk

WM_COPYDATA = 0x004A


class COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_void_p),
        ("cbData", ctypes.c_int),
        ("lpData", ctypes.c_void_p),
    ]


def send_message():
    hwnd = ctypes.windll.user32.FindWindowW(None, "CSharpReceiver")
    if hwnd == 0:
        print("找不到 C# 視窗")
        return
    else:
        print("有找到 C# 視窗, 並發送訊息")

    text = "Python 發送資料、vcs接收資料"

    buf = ctypes.create_unicode_buffer(text)

    cds = COPYDATASTRUCT()
    cds.dwData = None
    cds.cbData = ctypes.sizeof(buf)
    cds.lpData = ctypes.cast(buf, ctypes.c_void_p)

    ctypes.windll.user32.SendMessageW(hwnd, WM_COPYDATA, 0, ctypes.byref(cds))


window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
# size = str(W)+'x'+str(H)
# size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
title = "Python 發送資料、vcs接收資料"
window.title(title)

btn = tk.Button(window, width=20, height=4, command=send_message, text="發送訊息")
btn.pack(padx=20, pady=20)

window.mainloop()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
