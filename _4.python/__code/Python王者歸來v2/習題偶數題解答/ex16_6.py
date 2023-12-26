# ex16_6.py
import re

msg = '''txt@deepstone.com.tw kkk@gmail.com
abc@me.com mymail@qq.com abc@abc@abc'''
pattern = r'''(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}                   # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4})?                # 國別
    )'''
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
for mail in eMail:
    print(mail[0])



