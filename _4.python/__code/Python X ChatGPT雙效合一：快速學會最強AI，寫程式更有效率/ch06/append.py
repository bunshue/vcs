num=int(input('請輸入總人數: '))
student = [] 
print('請輸入{0}個數值：'.format(num))

# 依序讀取分數
for item in range(1,num+1):
    score = int(input()) #取得輸入數值
    student.append(score) #新增到串列

print('總共輸入的分數', end = '\n')
for item in student:   
    print('{:3d} '.format(item), end = '')
