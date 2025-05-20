import time
print("========== 計時開始 ==========")
ts = time.time()
print("epoch秒數", ts)
input("計算按下Enter鍵之前的時間")
te = time.time()
print("epoch秒數", te)
print("========== 計時結束 ==========")
print("遊戲秒數", int(te-ts))
