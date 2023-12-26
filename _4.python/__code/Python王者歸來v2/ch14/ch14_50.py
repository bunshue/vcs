# ch14_50.py
import pyperclip

pyperclip.copy('明志科大-勤勞樸實')     # 將字串拷貝至剪貼簿
string = pyperclip.paste()              # 從剪貼簿拷貝回string
print(string)                           # 列印
