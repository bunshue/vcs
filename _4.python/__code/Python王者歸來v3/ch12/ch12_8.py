# ch12_8.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.get_balance()
hungbank.__balance = 10000                  # 類別外直接竄改存款餘額
hungbank.get_balance()











