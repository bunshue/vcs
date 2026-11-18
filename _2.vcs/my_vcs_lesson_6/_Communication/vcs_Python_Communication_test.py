print("------------------------------------------------------------")  # 60個
print("Python 發送資料、vcs接收資料")
print("------------------------------------------------------------")  # 60個


import sys

import platform
print(platform.architecture())


import ctypes
hwnd = ctypes.windll.user32.FindWindowW(None,"CSharpReceiver")
print("FindWindowW =", hwnd)

hwnd = ctypes.windll.user32.FindWindowW(None,"PythonReceiver")
print("FindWindowW =", hwnd)

if hwnd == 0:
    print("找不到 C# 視窗")



