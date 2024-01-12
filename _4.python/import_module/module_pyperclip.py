import pyperclip  # 將文字拷貝至剪貼簿的模組

string1 = "秦時明月漢時關，萬里長征人未還。但使龍城飛將在，不教胡馬度陰山。"

print('將字串拷貝至剪貼簿')
pyperclip.copy(string1)

print('將剪貼簿的內容讀出來')
string2 = pyperclip.paste()
print(string2)

