for a in range(1,6): #外層for迴圈控制
    for b in range(1,a+1): #內層for迴圈控制
        if b==4:
            break
        print(b,end="") #印出b的值
    print()
