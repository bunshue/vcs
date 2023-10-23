#continue練習 
for a in range(10): #外層for迴圈控制y軸輸出
    for b in range(a+1): #內層for迴圈控制x軸輸出
        if b==6:
            continue
        print("%d " %b,end='')#印出b的值
    print()
