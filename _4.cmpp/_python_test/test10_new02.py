# Python 新進測試 02

password = "123"
pAttempt = input("Enter the password:(123) ")
while pAttempt != password:
    print("Password incorrect")
    pAttempt = input("Enter the password: ")
print("Password correct")


personName = "lion"
anObject = "mouse"
place = "cat dog"
story = personName + " was walking through " + place + ". " + place + " was not usually very interesting. " + personName + " spotted a small " + anObject + ". Suddenly the " + anObject + " jumped up and ran away. " + personName + " decided not to go to " + place + " again."
print(story)



age = 70
if (18 <= age <= 59):
	print('票價為1800元')
elif (60 <= age):
	print('票價為1000元')
else:
	print('無法賣出電影票')


pointcard = True
count = 5
if ((pointcard == True) and (count == 5)):
	print('感謝您的長久惠顧，此次為1000元優惠價')

counter = 0
while (counter < 5):
	print(counter)
	counter = counter + 1

while(True):
	print('揮拳')
	print('腳踢')
	break
	print('必殺奧義')

power = 2

while(True):
	print('揮拳')
	print('腳踢')
	print('必殺奧義')
	power = power - 1
	if(power == 0):
		break
