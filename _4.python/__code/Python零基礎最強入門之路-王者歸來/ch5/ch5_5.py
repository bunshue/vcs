# ch5_5.py
print("計算最終成績")
score = input("請輸入分數: ")
sc = int(score)
if (sc >= 90):
    print(" A")
elif (sc >= 80):
    print(" B")
elif (sc >= 70):
    print(" C")
elif (sc >= 60):
    print(" D")
else:
    print(" F")
    
