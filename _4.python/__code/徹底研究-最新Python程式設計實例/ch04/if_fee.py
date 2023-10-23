print("停車超過一小時,每小時收費40元")
t=int(input("請輸入停車幾小時: ")) #輸入時數	     
if t>=1:
    total=t*40 #計算費用
    print("停車%d小時,總費用為:%d元" %(t,total))
