import pyperclip  # 將文字拷貝至剪貼簿的模組

string1 = "秦時明月漢時關，萬里長征人未還。但使龍城飛將在，不教胡馬度陰山。"

print("將字串拷貝至剪貼簿")
pyperclip.copy(string1)

print("將剪貼簿的內容讀出來")
string2 = pyperclip.paste()
print(string2)


import pyperclip

# 要複製到剪貼簿的文本
text_to_copy = "Hello, world!"

# 將文本複製到剪貼簿
pyperclip.copy(text_to_copy)

# 檢查剪貼簿中的文本是否與複製的文本相同
copied_text = pyperclip.paste()
print("Copied text:", copied_text)

"""
請注意，一旦您退出Python程序，剪貼簿中的內容就會被清除，這是操作系統的一種行為。
剪貼簿的內容通常不會在程序退出後保留。
如果您希望保存文本，您可能需要將文本保存到文件或者將其存儲在內存中，
以便在需要時進行檢索。
"""
