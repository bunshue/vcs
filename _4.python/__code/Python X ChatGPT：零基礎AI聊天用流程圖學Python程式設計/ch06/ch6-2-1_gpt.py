# Step 1：顯示提示文字"請輸入最大值: "來輸入整數變數m的值。
m = int(input("請輸入最大值: "))

# Step 2：指定整數變數total的值是0。
total = 0

# Step 3：指定計數器變數i的值是1。
i = 1

# Step 4：使用for迴圈重複執行直到變數i > m :
for i in range(1, m+1):
    # Step 4.1：計算出變數total加上變數i的和。
    total += i
    
    # Step 4.2：將計數器變數i的值加1。
    i += 1

# Step 5：輸出文字內容"總和= "和變數total的值。
print("總和= ", total)
