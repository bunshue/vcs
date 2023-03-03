# while-loop

print("while迴圈")
i = 10
while i < 30:
    print(i)
    i += 5
    if( i == 20):
        break


print("語法 : while")
a = 0;
story = "";
while a < 10:
    a = a + 1;
    story += "hello" + " "
    #print("hello")
    #print("");  #空白一行
print(story)




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


