# ch28_32.py
import pyautogui
import time

time.sleep(5)

# 選擇所有本字, 例如在一個文字編輯器中
pyautogui.hotkey('ctrl', 'a')   # Ctrl + A

# 複製
pyautogui.hotkey('ctrl', 'c')   # Ctrl + C

# 移動到另一個位置或應用
pyautogui.click(100, 100)       # 移動滑鼠游標並按一下

# 貼上
pyautogui.hotkey('ctrl', 'v')   # Ctrl + V


