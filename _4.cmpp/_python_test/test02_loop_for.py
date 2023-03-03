# for-loop


print("for迴圈")

for i in range(10, 20, 3):
    print(i)




days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for index in range(len(days)):
   print('index = ', str(index), ', day = ', days[index])

for letter in 'Hello Python':
   print('Current Letter :', letter)


for letter in "Hello Python":
    if letter == 'h':
        pass   #空指令
    else:
        print('Current Letter :', letter)
   





for i in range(2,9):
    if i != 2 and i != 6 : continue
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}x{}={:>2}    ".format(k, j, k*j), end="")
        print()
    print()


for i in range(2,7,4):
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}x{}={:>2}    ".format(k, j, k*j), end="")
        print()
    print()




for i in range(2,7,4):
    for j in range(1,10):
        print("{}x{}={:>2}    ".format(i, j, i*j), end="")
        print("{}x{}={:>2}    ".format(i+1, j, (i+1)*j), end="")
        print("{}x{}={:>2}    ".format(i+2, j, (i+2)*j), end="")
        print("{}x{}={:>2}    ".format(i+3, j, (i+3)*j))
    print()


print("語法 : 取得數字")
number = int(input("請輸入一個數字 : "))
print("取得數字" + str(number))
for nn in range(number):
    print(nn)
    #print("")




