# Filename: ex06_082.py
# 模組與套件 clock() python3.8後改為perf_counter()
import time as t
#print("開始執行到目前的時間:"+str(t.clock()))
print("開始執行到目前的時間:"+str(t.perf_counter()))
t.sleep(2)
print("程式執行時間經過:"+str(t.perf_counter())+"秒")
t.sleep(3)
print("程式執行時間經過:"+str(t.perf_counter())+"秒")