print("求取兩正整數的最大公因數(g.c.d):")
print("輸入兩個正整數:")
#輸入兩數
Num1=int(input())
Num2=int(input())
if Num1 < Num2:
    TmpNum=Num1                           
    Num1=Num2
    Num2=TmpNum#找出兩數較大值
while Num2 != 0:
    TmpNum=Num1 % Num2            
    Num1=Num2                              
    Num2=TmpNum #輾轉相除法
print("最大公因數(g.c.d)的值為:%d" %Num1)
