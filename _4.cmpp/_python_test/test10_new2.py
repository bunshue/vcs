# Python 新進測試

import time

password = "123"
pAttempt = input("Enter the password:(123) ")
while pAttempt != password:
    print("Password incorrect")
    pAttempt = input("Enter the password: ")
print("Password correct")

        #time.sleep(5)
        #time.sleep(1)
      

personName = "lion"
anObject = "mouse"
place = "cat dog"
story = personName + " was walking through " + place + ". " + place + " was not usually very interesting. " + personName + " spotted a small " + anObject + ". Suddenly the " + anObject + " jumped up and ran away. " + personName + " decided not to go to " + place + " again."
print(story)



