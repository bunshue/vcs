def formula(x, y): #自訂函數
    return 3*x+2*y

formula = lambda x, y : 3*x+2*y  #表示lambda有二個參數
print(formula (5,10)) ##傳入兩個數值讓lambda()函數做運算，輸出數值35
