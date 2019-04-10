# General IO

a = 0;
#while True:

story = "";
while a < 10:
    a = a + 1;
    story += "hello" + " "
    #print("hello")
    #print("");  #空白一行
print(story)

userName = input("What is your name? ")
message = input("Enter a message: ")
while message != "exit":
    print(userName + ": " + message)
    message = input("Enter a message: ")


print("How old are you?"),
age = input()
print ("so %s old" %age )


ans = input("Are you all right? ")
if ans == "Yes":
    print("Great")
elif ans == "yes":
    print("Yahoo")
else:
    print("Fine")
    

shipName = "Nastrama"
password = "123"
pAttempt = input("Enter the password: (123)")
while pAttempt != password:
    print("Password incorrect")
    pAttempt = input("Enter the password: ")
print("Password correct. Welcome to the " + shipName)





import time
a = 0;
while a < 5:
    a += 1;
    print("hello")
    time.sleep(1)


number = int(input("Please input a number : "))

for nn in range(number):
    print(nn)
    #print("")





