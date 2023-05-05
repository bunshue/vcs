print('建立一組密碼 並將此密碼拷貝至剪貼簿')
import random
import pyperclip
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
password = ''
for c in range(20):
   password += random.choice(chars)
print('建立一組密碼:\t%r, 並已拷貝至剪貼簿' %(password))
pyperclip.copy(password)


'''
import webbrowser
print('用預設的瀏覽器開啟網頁')
url = 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5'
print(url)
webbrowser.open(url)
'''

