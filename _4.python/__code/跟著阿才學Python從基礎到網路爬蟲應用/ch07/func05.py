# 定義GetMax()函式，可傳回n1和n2兩數的最大數
def GetMax(n1, n2) :
    if (n1>n2 ) :   
        vMax=n1
    else :
        vMax=n2
    return vMax

Max = GetMax(70, 9) 
print("70和 9最大值為", Max)
print("17和30最大值為", GetMax(17,30))  




