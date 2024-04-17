# Filename: pex05_02.py
ps = input("請輸入一串列的整數，數目之間利用空白分隔：") 
pitems = ps.split() 
pnumbers = [ eval(x) for x in pitems ] 
pnumbers.reverse()
print(pnumbers)    