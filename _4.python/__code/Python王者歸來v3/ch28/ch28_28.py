# ch28_28.py
import pyautogui
import time

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)

pyautogui.write('Taiwan\t',0.3)                     # Taiwan
pyautogui.write('Hung\t',0.3)                       # 姓
pyautogui.write('Jiin-Kwei\t',0.3)                  # 名
pyautogui.write('Jiin-Kwei\t',0.3)                  # 名
pyautogui.write('Hung\t',0.3)                       # 姓
pyautogui.write('1975\t',0.3)                       # 出生年        
pyautogui.write('01\t',0.3)                         # 月
pyautogui.write('01\t',0.3)                         # 日
pyautogui.write('\t',0.3)                           # 選男生
pyautogui.write('Ming-Chi Inst. of Tech\t',0.3)     # 學校
pyautogui.write('Department of ME',0.3)              # 科系





