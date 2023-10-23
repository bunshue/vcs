def Common_Divisor():
    print("請輸入兩個數值")
    Num1=int(input("數值 1："))
    Num2=int(input("數值 2："))
    print(Num1,'及',Num2)
    while Num2 != 0: #利用輾轉相除法計算最大公因數
        Temp=Num1 % Num2
        Num1 = Num2
        Num2 = Temp
    return Num1

Min=Common_Divisor(); #函數呼叫
print("的最大公因數為：",Min)
