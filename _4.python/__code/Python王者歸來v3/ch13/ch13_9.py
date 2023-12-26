# ch13_9.py
from banks import Banks                     # 導入banks模組的Banks類別

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
jamesbank.save_money(500)                   # 存錢
jamesbank.get_balance()                     # 列出存款金額

















