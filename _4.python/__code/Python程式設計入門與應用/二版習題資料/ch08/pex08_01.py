# Filename: pex08_01.py
pfile = input("請輸入讀取檔案名稱：").strip()
pinfile = open(pfile, "r")
ps = pinfile.read()  
print(str(len(ps)) + " 字元數") 
print(str(len(ps.split())) + " 單字數") 
print(str(len(ps.split('\n'))) + " 行數") 
pinfile.close()