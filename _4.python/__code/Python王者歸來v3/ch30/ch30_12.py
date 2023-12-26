# ch30_12.py
import subprocess

calcPro = subprocess.Popen('calc.exe')      # 傳回值是子行程
notePro = subprocess.Popen('notepad.exe')   # 傳回值是子行程
writePro = subprocess.Popen('write.exe')    # 傳回值是子行程
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")
print(f"列印notePro  = {notePro}")
print(f"列印writePro = {writePro}")





