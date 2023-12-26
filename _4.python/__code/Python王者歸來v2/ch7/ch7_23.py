# ch7_23.py
print("測試1")
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit, end=', ')
print( )
print("測試2")
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end=', ')


