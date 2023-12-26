# ch28_31.py
import pyautogui
import subprocess
import time

# 打開記事本（或其他應用）
subprocess.Popen('notepad.exe')
time.sleep(2)

# 輸入文本
pyautogui.write('AI實作 - 明志科技大學!', interval=0.1)


