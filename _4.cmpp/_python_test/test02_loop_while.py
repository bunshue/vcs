# while-loop

print("while�j��")
i = 10
while i < 30:
    print(i)
    i += 5
    if( i == 20):
        break


print("�y�k : while")
a = 0;
story = "";
while a < 10:
    a = a + 1;
    story += "hello" + " "
    #print("hello")
    #print("");  #�ťդ@��
print(story)




print("�y�k : input")
userName = input("What is your name? ")
message = input("�п�J�@�ӰT��(��Jexit���})")
while message != "exit":
    print(userName + ": " + message)
    message = input("Enter a message: ")



print("�y�k : ��J�b���K�X")


id = input("�п�J�b�� : (david)")
print("�ϥΪ� : "+id)
password = "123"
pAttempt = input("�п�J�K�X : (123)")
while pAttempt != password:
    print("�K�X���~")
    pAttempt = input("�п�J�K�X : (123)")
print("�K�X���T, �w�� " + id+ " �ϥ�")


