# Filename: pex04_02.py
#ps = input("請輸入一串列的整數，數目之間利用空白分隔：") 
#pitems = ps.split() 
#pnumbers = [ eval(x) for x in pitems ] 
pnumbers = []
for i in range(1,4):
    pitems=int(input("請輸入第%d個整數："%i))
    pnumbers.append(pitems)
pnumbers.reverse()
print(pnumbers)    