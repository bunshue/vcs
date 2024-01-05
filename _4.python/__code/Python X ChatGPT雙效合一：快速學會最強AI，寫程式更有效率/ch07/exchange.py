def exchange(num):
    num[0],num[1]=num[1],num[0] #交換兩數過程

print("請輸入兩個數值: ")
num=[]
num.append(int(input()))
num.append(int(input()))
print('num[0]=',num[0])
print('num[1]=',num[1])
exchange(num)
print('------------- exchange()函數交換 ----------------')
print('num[0]=',num[0])
print('num[1]=',num[1])
