print("|a1 b1|")
print("|a2 b2|")
arr=[[]*2 for i in range(2)]
arr=[[0,0],[0,0]]
arr[0][0]=int(input("請輸入a1:"))
arr[0][1]=int(input("請輸入b1:"))
arr[1][0]=int(input("請輸入a2:"))
arr[1][1]=int(input("請輸入b2:"))
ans= arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0] #求二階行列式的值
print("| %d %d |" %(arr[0][0],arr[0][1]))
print("| %d %d |" %(arr[1][0],arr[1][1]))
print("ans= %d" %ans)
