# ch30_30.py
import subprocess

calcPro = subprocess.Popen('calc.exe')      # 傳回值是子行程
notePro = subprocess.Popen('notepad.exe')   # 傳回值是子行程
writePro = subprocess.Popen('write.exe')    # 傳回值是子行程
print("資料型態           = ", type(calcPro))
print("列印calcPro  = ", calcPro)
print("列印notePro  = ", notePro)
print("列印writePro = ", writePro)





