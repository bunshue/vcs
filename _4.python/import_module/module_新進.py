print('建立一組密碼 並將此密碼拷貝至剪貼簿')
import random
import pyperclip
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
password = ''
for c in range(20):
   password += random.choice(chars)
print('建立一組密碼:\t%r, 並已拷貝至剪貼簿' %(password))
pyperclip.copy(password)







