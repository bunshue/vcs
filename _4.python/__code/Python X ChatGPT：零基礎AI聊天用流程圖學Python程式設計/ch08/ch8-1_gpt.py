# Step 1: 顯示提示文字"輸入數值"來輸入整數變數value的值。
value = int(input("輸入數值: "))

# Step 2: 如果value變數值小於0 :
if value < 0:
    # Step 2.1: 計算(-value)儲存至變數value。
    value = -value

# Step 3: 輸出文字內容"絕對值 = "和變數value的值。
print("絕對值 = ", value)
