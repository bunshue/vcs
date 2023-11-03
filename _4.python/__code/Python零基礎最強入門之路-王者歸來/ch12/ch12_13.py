# ch12_12.py
class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.__title

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱
    def bank_title(self):                   # 獲得銀行名稱
        return self.title

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')             # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bank_title())   # 列印銀行名稱














