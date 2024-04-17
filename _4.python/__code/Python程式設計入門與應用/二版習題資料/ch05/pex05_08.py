# Filename: pex05_08.py
def ctof(pc):
    presult = pc*9/5+32
    return presult

ptemp = float(input("請輸入攝氏溫度:"))
print("攝氏溫度%6.2f轉換為華氏溫度為%6.2f"%(ptemp,ctof(ptemp)))