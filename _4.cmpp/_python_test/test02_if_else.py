# for-loop while-loop if-else

print("語法 : while")
a = 0;
story = "";
while a < 10:
    a = a + 1;
    story += "hello" + " "
    #print("hello")
    #print("");  #空白一行
print(story)

print("語法 : if-else")
ans = input("Are you all right? ")
if ans == "Yes":
    print("Great")
elif ans == "yes":
    print("Yahoo")
else:
    print("Fine")

print("語法 : input")
userName = input("What is your name? ")
message = input("請輸入一個訊息(輸入exit離開)")
while message != "exit":
    print(userName + ": " + message)
    message = input("Enter a message: ")

print("語法 : 輸入帳號密碼")

id = input("請輸入帳號 : (david)")
print("使用者 : "+id)
password = "123"
pAttempt = input("請輸入密碼 : (123)")
while pAttempt != password:
    print("密碼錯誤")
    pAttempt = input("請輸入密碼 : (123)")
print("密碼正確, 歡迎 " + id+ " 使用")

print("語法 : 取得數字")
number = int(input("請輸入一個數字 : "))
print("取得數字" + str(number))
for nn in range(number):
    print(nn)
    #print("")

print("List測試");
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
   

