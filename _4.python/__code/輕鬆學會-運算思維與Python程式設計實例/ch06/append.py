num=int(input('請輸入總人數: '))
student = [] #建立空的list串列
print('請輸入{0}個數值：'.format(num))

# 以for/in廻圈依序讀取要輸入的分數
for item in range(1,num+1):
    score = int(input()) #取得輸入數值
    student.append(score) #將輸入數值新增到串列

print('已輸入完畢')
#輸出資料
print('總共輸入的分數', end = '\n')
for item in student:   
    print('{:3d} '.format(item), end = '')
