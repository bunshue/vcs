# ch30_16.py
import subprocess

calcPro = subprocess.run('calc.exe')      
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")






