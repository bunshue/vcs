# while-loop

import time

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

cnt = 0;
while True:
    for n in range(100,-1,-1): #燈漸亮
        #print('a')
        time.sleep(0.005)
    for n in range(100):      #燈漸熄
        #print('b')
        time.sleep(0.005)
    cnt = cnt + 1
    if( cnt == 5):
        break
    print("change " + str(cnt))

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


userName = input("What is your name? ")
message = input("Enter a message: ")
while message != "exit":
    print (userName + ": " + message)
    message = input("Enter a message: ")


a=0;
while True:
    print("I'm in space " + str(a))
    a=a+1;
    if a>5:
        break
   
    
again = "yes"
while again == "yes":
    praiseType = input("Select a type of praise \n a: personality \n b: appearance \n c: intelligence")
    if praiseType == "a":
        print("You are an interesting person")
    elif praiseType == "b":
        print("You are smart")
    elif praiseType == "c":
        print("You look good")
    else:
        print("That wasn't an option")
    again = input("Would you like some more praise?")




