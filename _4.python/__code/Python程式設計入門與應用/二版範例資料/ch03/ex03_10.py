# Filename: ex03_10.py
# while迴圈數值系統轉換十進位至二進位
pnum = int(input("請輸入需要轉換的十進位數值:"))        
# 宣告儲存資料的串列array to store 
# 二進位的數值binary number 
pbin = [0] * pnum; 
# 轉換至二進位counter for binary array 
i = 0; 
while (pnum > 0):  
    # 儲存餘數至二進位的串列
    pbin[i] = pnum % 2; 
    pnum = int(pnum / 2); 
    i += 1;
# 將串列反向印出
j=i-1    
while (j>-1):
    print(pbin[j], end = "");
    j -= 1;