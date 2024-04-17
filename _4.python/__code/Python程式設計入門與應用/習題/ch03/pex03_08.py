# Filename: pex03_08.py
pm = float(input("請輸入水的公升數:"))
pinitaltemp = float(input("請輸入水的起始溫度(攝氏):"))
pfinaltemp = float(input("請輸入水的最後溫度(攝氏):"))
pq = pm*(pfinaltemp-pinitaltemp)*4184
print("水的公升數%6.2f起始溫度%6.2f最後溫度%6.2f所需能量(焦耳)%6.2f"%(pm,pinitaltemp,pfinaltemp,pq))