# ch12_3.py
class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def get_balance(self):                  # 獲得存款餘額
        return self.balance

hungbank = Banks('hung', 100)               # 定義物件hungbank
print(hungbank.name.title( ), " 存款餘額是 ", hungbank.get_balance())





