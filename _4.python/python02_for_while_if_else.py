print("for迴圈 while迴圈 if-else 的寫法")

print("------------------------------------------------------------")  # 60個

print("for迴圈的寫法")

# range(N) = range(0, N) 回傳 0 ~ (N - 1) 之不可變數列(sequence)

# 0 ~ (N-1)
N = 6
for i in range(N):
    print(i)

print("------------------------------------------------------------")  # 60個

N = 6
# 0 ~ (N-1)
for i in range(0, N):
    print(i)

print("------------------------------------------------------------")  # 60個

N1, N2 = 3, 6
# N1 ~ (N2-1)
for i in range(N1, N2):
    print(i)

print("------------------------------------------------------------")  # 60個

N1, N2, INC = 3, 17, 3
# 3 ~ (N-1), 每次加3
for i in range(N1, N2, INC):
    print(i)

print("------------------------------------------------------------")  # 60個

total = 7
for i in range(0, (total + 1)):
    # print(i)	# 0 ~ 7
    print("download: " + str(100 * i / total) + " %.")

print("------------------------------------------------------------")  # 60個

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for index in range(len(days)):
    print("index = ", str(index), ", day = ", days[index])

for letter in "Hello Python":
    print("Current Letter :", letter)


for letter in "Hello Python":
    if letter == "h":
        pass  # 空指令
    else:
        print("Current Letter :", letter)

print("------------------------------------------------------------")  # 60個

for i in range(2, 9):
    if i != 2 and i != 6:
        continue
    for j in range(1, 10):
        for k in range(i, i + 5):
            print("{}x{}={:>2}    ".format(k, j, k * j), end="")
        print()
    print()

print("------------------------------------------------------------")  # 60個

for i in range(2, 7, 4):
    for j in range(1, 10):
        for k in range(i, i + 5):
            print("{}x{}={:>2}    ".format(k, j, k * j), end="")
        print()
    print()

print("------------------------------------------------------------")  # 60個

for i in range(2, 7, 4):
    for j in range(1, 10):
        print("{}x{}={:>2}    ".format(i, j, i * j), end="")
        print("{}x{}={:>2}    ".format(i + 1, j, (i + 1) * j), end="")
        print("{}x{}={:>2}    ".format(i + 2, j, (i + 2) * j), end="")
        print("{}x{}={:>2}    ".format(i + 3, j, (i + 3) * j))
    print()


print("------------------------------------------------------------")  # 60個
print("語法 : 取得數字")
number = int(input("請輸入一個數字 : "))
print("取得數字" + str(number))
for nn in range(number):
    print(nn)
    # print("")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("while迴圈的寫法")

import time

print("while迴圈")
i = 10
while i < 30:
    print(i)
    i += 5
    if i == 20:
        break

print("------------------------------------------------------------")  # 60個

print("語法 : while")
a = 0
story = ""
while a < 10:
    a = a + 1
    story += "hello" + " "
    # print("hello")
    # print("");  #空白一行
print(story)

cnt = 0
while True:
    for n in range(100, -1, -1):  # 燈漸亮
        # print('a')
        time.sleep(0.005)
    for n in range(100):  # 燈漸熄
        # print('b')
        time.sleep(0.005)
    cnt = cnt + 1
    if cnt == 5:
        break
    print("change " + str(cnt))

print("------------------------------------------------------------")  # 60個

print("語法 : input")
userName = input("What is your name? ")
message = input("請輸入一個訊息(輸入exit離開)")
while message != "exit":
    print(userName + ": " + message)
    message = input("Enter a message: ")


print("------------------------------------------------------------")  # 60個
print("語法 : 輸入帳號密碼")


id = input("請輸入帳號 : (david)")
print("使用者 : " + id)
password = "123"
pAttempt = input("請輸入密碼 : (123)")
while pAttempt != password:
    print("密碼錯誤")
    pAttempt = input("請輸入密碼 : (123)")
print("密碼正確, 歡迎 " + id + " 使用")


userName = input("What is your name? ")
message = input("Enter a message: ")
while message != "exit":
    print(userName + ": " + message)
    message = input("Enter a message: ")

print("------------------------------------------------------------")  # 60個

a = 0
while True:
    print("I'm in space " + str(a))
    a = a + 1
    if a > 5:
        break

print("------------------------------------------------------------")  # 60個

again = "yes"
while again == "yes":
    praiseType = input(
        "Select a type of praise \n a: personality \n b: appearance \n c: intelligence"
    )
    if praiseType == "a":
        print("You are an interesting person")
    elif praiseType == "b":
        print("You are smart")
    elif praiseType == "c":
        print("You look good")
    else:
        print("That wasn't an option")
    again = input("Would you like some more praise?")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("if-else的寫法")

print("語法 : while")
a = 0
story = ""
while a < 10:
    a = a + 1
    story += "hello" + " "
    # print("hello")
    # print("");  #空白一行
print(story)

print("------------------------------------------------------------")  # 60個

print("語法 : if-else")
ans = input("Are you all right? ")
if ans == "Yes":
    print("Great")
elif ans == "yes":
    print("Yahoo")
else:
    print("Fine")

print("------------------------------------------------------------")  # 60個

print("語法 : input")
userName = input("What is your name? ")
message = input("請輸入一個訊息(輸入exit離開)")
while message != "exit":
    print(userName + ": " + message)
    message = input("Enter a message: ")

print("------------------------------------------------------------")  # 60個

print("語法 : 輸入帳號密碼")

id = input("請輸入帳號 : (david)")
print("使用者 : " + id)
password = "123"
pAttempt = input("請輸入密碼 : (123)")
while pAttempt != password:
    print("密碼錯誤")
    pAttempt = input("請輸入密碼 : (123)")
print("密碼正確, 歡迎 " + id + " 使用")

print("------------------------------------------------------------")  # 60個

print("語法 : 取得數字")
number = int(input("請輸入一個數字 : "))
print("取得數字" + str(number))
for nn in range(number):
    print(nn)
    # print("")

print("------------------------------------------------------------")  # 60個

print("List測試")
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for index in range(len(days)):
    print("index = ", str(index), ", day = ", days[index])

for letter in "Hello Python":
    print("Current Letter :", letter)

print("------------------------------------------------------------")  # 60個

for letter in "Hello Python":
    if letter == "h":
        pass  # 空指令
    else:
        print("Current Letter :", letter)

print("------------------------------------------------------------")  # 60個

print("語法 : if-else")
ans = input("Are you all right? ")
if ans == "Yes":
    print("Great")
elif ans == "yes":
    print("Yahoo")
else:
    print("Fine")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
