# ch12_5.py
class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'                # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
johnbank = Banks('john', 300)               # 定義物件johnbank
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額
hungbank.save_money(100)                    # hung存款100
johnbank.withdraw_money(150)                # john提款150
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額








