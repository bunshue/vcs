# while廻圈
number = 200; a, b = 2, 2 #宣告變數
result = a ** 2

# while廻圈 變數result小於number時，輸出運算結果
print('運算結果-->')
while result < number:
    result *= b
    print(result) #輸出後換行
    #print(result, end =', ') #輸出後不換行
