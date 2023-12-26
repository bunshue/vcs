# ch16_32.py
import re

msg = '''txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         abcdefg'''
pattern = r'''(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )'''
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])



