'''
各種演算法
'''


def bubbleSort(list):
    needNextPass = True
    
    k = 1
    while k < len(list) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(list) - k): 
            if list[i] > list[i + 1]:
                # swap list[i] with list[i + 1]
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
          
                needNextPass = True # Next pass still needed

list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
bubbleSort(list)
for v in list:
    print(v)



def Fibonacci(n):  # 写出从第0项到第n项的Fibonacci系列
    a, b, i = 0, 1, 0 
    while i <= n:
        print(a, end=' ')
        a, b, i = b, a+b, i+1
    print()

print(Fibonacci(10))

    
