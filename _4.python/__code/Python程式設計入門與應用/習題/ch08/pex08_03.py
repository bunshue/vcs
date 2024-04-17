# Filename: pex08_03.py
try:
    pnumber = int(input("請輸入一個整數："))
    print("所輸入的整數%d"%pnumber)
except Exception as ex:
    print("異常例外：", ex) 