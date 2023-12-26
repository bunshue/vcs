# ex5_4.py
i = input("溫度轉換選擇\n1:華氏溫度轉成攝氏溫度\n2:攝氏溫度轉華氏溫度\n= ")
if i == "1":
    f = input("請輸入華氏溫度：")
    c = ( int(f) - 32 ) * 5 / 9
    print(f"華氏 {f} 等於攝氏 {c:4.1f}")    
elif i == "2":    
    c = input("請輸入攝氏溫度：")
    f = int(c) * 9 / 5 + 32
    print(f"攝氏 {c} 等於華氏 {f:4.1f}")
else:
    print(f"輸入錯誤")


