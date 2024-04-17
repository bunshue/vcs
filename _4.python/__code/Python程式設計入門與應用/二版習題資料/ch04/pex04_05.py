# Filename: pex04_05.py
ps=input("請輸入一個字串：")
pcounts = 0
for word in ps:
    if word == 'a':
        pcounts +=1
print ("輸入的字串中，a出現的次數："+str(pcounts))