# ch16_30.py
import re

msg = '''02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        1234567899999,
        02 33887766 ext. 1234,
        02 33887799 ext. 12345,
        12345,
        123'''
pattern = r'''(
    (\d{2}|\(\d{2}\))?              # 區域號碼
    (\s|-)?                         # 區域號碼與電話號碼的分隔符號
    \d{8}                           # 電話號碼
    (\s*(ext|ext.)\s*\d{2,4})?      # 2-4位數的分機號碼
    )'''
phoneNum = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])




