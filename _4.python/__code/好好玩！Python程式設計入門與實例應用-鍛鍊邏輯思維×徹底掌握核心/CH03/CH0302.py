'''
利用 表2-2所列的內建函數將輸入數值做轉換
'''

#int()函式將number轉為整數型別
number = int(input('輸入一個數值-> '))
print('型別：', type(number))
print('二進位：', bin(number))
print('八進位', oct(number))
print('十六進位', hex(number))
print('10進位：', number)

# 配合format函式去除前綴字元
print('二進位：', format(number, 'b'))
print('八進位：', format(number, 'o'))
print('十六進位：', format(number, 'x'))

