# Step 1：提示用戶輸入最大階層數，並將其轉換為整數儲存到變數m中
m = int(input("請輸入最大階層數: "))

# Step 2：初始化階層值r為1
r = 1

# Step 3：初始化計數器變數n為1
n = 1

# Step 4：計算n的階層值，直到n > m
while n <= m:
    # Step 4.1：計算r乘以n的值，存入r中
    r *= n
    # Step 4.2：將計數器變數n加1
    n += 1

# Step 5：輸出階層值r的值
print("階層值!= ", r)
