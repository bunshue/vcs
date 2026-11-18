print("------------------------------------------------------------")  # 60個
print("PyAutoGUI，自動控制滑鼠與鍵盤 ST")
print("------------------------------------------------------------")  # 60個


import tkinter as tk
import ctypes

WM_COPYDATA = 0x004A


class COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_void_p),
        ("cbData", ctypes.c_int),
        ("lpData", ctypes.c_void_p)
    ]


def send_message():

    hwnd = ctypes.windll.user32.FindWindowW(
        None,
        "CSharpReceiver"
    )

    if hwnd == 0:
        print("找不到 C# 視窗")
        return

    text = "hello, I am python"

    buf = ctypes.create_unicode_buffer(text)

    cds = COPYDATASTRUCT()
    cds.dwData = None
    cds.cbData = ctypes.sizeof(buf)
    cds.lpData = ctypes.cast(
        buf,
        ctypes.c_void_p
    )

    ctypes.windll.user32.SendMessageW(
        hwnd,
        WM_COPYDATA,
        0,
        ctypes.byref(cds)
    )


root = tk.Tk()

btn = tk.Button(
    root,
    text="Send",
    command=send_message
)

btn.pack(padx=20, pady=20)

root.mainloop()


