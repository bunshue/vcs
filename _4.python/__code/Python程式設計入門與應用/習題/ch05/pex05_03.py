# Filename: pex05_03.py
ps = input("請輸入一串列的整數，數目之間利用空白分隔：") 
pitems = ps.split()
pscores = [ eval(x) for x in pitems ]
pabove = 0
paverage = sum(pscores)/len(pscores)
for score in pscores:
    if score >= paverage:
        pabove += 1
print("平均數："+str(paverage))
print("大於或等於平均數的數目："+str(pabove))
print("小於平均數的數目："+str(len(pscores)-pabove))