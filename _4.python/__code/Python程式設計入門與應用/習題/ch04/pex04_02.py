# Filename: pex04_02.py
pnumbers = []
for i in range(1,4):
    pitems=int(input("請輸入第%d個整數："%i))
    pnumbers.append(pitems)
pnumbers.reverse()
print(pnumbers)    