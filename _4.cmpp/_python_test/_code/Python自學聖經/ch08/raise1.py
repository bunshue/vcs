def CheckSpeed(speed): #檢查速度
    if speed < 70:
        raise Exception("速度太慢了!") # 拋出 Exception 型別例外
    if speed > 110:
        raise Exception("已經超速了!") # 拋出 Exception 型別例外 

for speed in (60,100,150):       
    try:
        CheckSpeed(speed) #檢查速度
    except Exception as e: #接收 Exception的例外
        print("現在速度：{}，{}" .format(speed,e))
    else:
        print("目前時速：{}" .format(speed))