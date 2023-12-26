# ch15_21.py
class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        assert money > 0, '存款money必需大於0'
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        assert money > 0, '提款money必需大於0'
        assert money <= self.balance, '存款金額不足'
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(300)                    # 存款300元
hungbank.get_balance()                      # 獲得存款餘額
hungbank.withdraw_money(700)                # 提款700元
hungbank.get_balance()                      # 獲得存款餘額




