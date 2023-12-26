# ch30_17.py
import subprocess

ret = subprocess.run('echo %time%', shell=True, stdout=subprocess.PIPE)
print(f"資料型態       = {type(ret)}")
print(f"列印ret        = {ret}")
print(f"列印ret.stdout = {ret.stdout}")






