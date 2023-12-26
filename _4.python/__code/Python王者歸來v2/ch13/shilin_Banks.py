# shilin_banks.py
# 這是一個包含Shilin_Banks類別的模組(module)
from banks1 import Banks                     # 導入Banks類別

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱
    def bank_title(self):                   # 獲得銀行名稱
        return self.title

















