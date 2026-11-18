print("------------------------------------------------------------")  # 60個
print("PyAutoGUI，自動控制滑鼠與鍵盤 ST")
print("------------------------------------------------------------")  # 60個


import tkinter as tk
import ctypes

WM_COPYDATA = 0x004A
GWL_WNDPROC = -4


class COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_void_p),
        ("cbData", ctypes.c_int),
        ("lpData", ctypes.c_void_p)
    ]


root = tk.Tk()
root.title("PythonReceiver")

text = tk.Text(root)
text.pack(fill="both", expand=True)


WNDPROC = ctypes.WINFUNCTYPE(
    ctypes.c_long,
    ctypes.c_int,
    ctypes.c_uint,
    ctypes.c_int,
    ctypes.c_int
)


def new_wndproc(hwnd, msg, wparam, lparam):

    if msg == WM_COPYDATA:

        cds = ctypes.cast(
            lparam,
            ctypes.POINTER(COPYDATASTRUCT)
        ).contents

        message = ctypes.wstring_at(cds.lpData)

        text.insert("end", message + "\n")
        text.see("end")

        return 1

    return ctypes.windll.user32.CallWindowProcW(
        old_wndproc,
        hwnd,
        msg,
        wparam,
        lparam
    )


new_proc = WNDPROC(new_wndproc)

hwnd = root.winfo_id()

old_wndproc = ctypes.windll.user32.SetWindowLongPtrW(
    hwnd,
    GWL_WNDPROC,
    new_proc
)

root.mainloop() 

