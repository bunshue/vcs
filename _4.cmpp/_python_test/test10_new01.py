# Python 新進測試 01

print("歡迎光臨 Python")

yourName = input("What is your name? ")
print("Hello " + yourName)

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



    




