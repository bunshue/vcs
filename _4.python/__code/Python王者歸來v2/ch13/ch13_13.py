# ch13_13.py
from banks1 import Banks                # 導入banks模組的Banks類別
from shilin_Banks import Shilin_Banks   # 導入Shilin_Banks模組的Shilin_Banks類別

jamesbank = Banks('James')              # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
jamesbank.save_money(500)               # 存錢
jamesbank.get_balance()                 # 列出存款金額
hungbank = Shilin_Banks('Hung')         # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bank_title())   # 列印銀行名稱
















