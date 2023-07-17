def ctof(c):  #攝氏轉華氏
    f = c * 1.8 + 32
    return f

inputc = float(input("請輸入攝氏溫度："))
print("華氏溫度為：%5.1f 度" % ctof(inputc))