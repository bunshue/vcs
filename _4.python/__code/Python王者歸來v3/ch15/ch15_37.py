# ch15_37.py
user_input = input("Please enter a number: ")

try:
    # 嘗試將使用者輸入轉換為整數
    val = int(user_input)
    print(f"Valid number entered: {val}")
except ValueError:
    # 如果輸入不能轉換為整數，處理 ValueError
    print("That's not a number!")



