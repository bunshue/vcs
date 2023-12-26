# ch30_35.py
import subprocess

ret = subprocess.run('echo %time%', shell=True, stdout=subprocess.PIPE)
print("資料型態           = ", type(ret))
print("列印ret  = ", ret)
print("列印ret.stdout", ret.stdout)






