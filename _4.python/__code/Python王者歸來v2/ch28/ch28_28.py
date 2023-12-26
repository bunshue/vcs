# ch28_28.py
import pyautogui
import time

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)

pyautogui.typewrite('Taiwan\t',0.3)                     # Taiwan
pyautogui.typewrite('Hung\t',0.3)                       # 姓
pyautogui.typewrite('Jiin-Kwei\t',0.3)                  # 名
pyautogui.typewrite('Jiin-Kwei\t',0.3)                  # 名
pyautogui.typewrite('Hung\t',0.3)                       # 姓
pyautogui.typewrite('1975\t',0.3)                       # 出生年        
pyautogui.typewrite('01\t',0.3)                         # 月
pyautogui.typewrite('01\t',0.3)                         # 日
pyautogui.typewrite('\t',0.3)                           # 選男生
pyautogui.typewrite('Ming-Chi Inst. of Tech\t',0.3)     # 學校
pyautogui.typewrite('Department of ME',0.3)              # 科系





