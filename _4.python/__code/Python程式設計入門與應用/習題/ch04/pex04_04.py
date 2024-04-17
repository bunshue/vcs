# Filename: pex04_04.py
pscores = []
for i in range(1,6):
    pitems=int(input("請輸入5位中第%d個學生成績："%i))
    pscores.append(pitems)
pabove = 0
paverage = sum(pscores)/len(pscores)
for score in pscores:
    if score >= paverage:
        pabove += 1
print("平均數："+str(paverage))
print("大於或等於平均數的數目："+str(pabove))
print("小於平均數的數目："+str(len(pscores)-pabove))