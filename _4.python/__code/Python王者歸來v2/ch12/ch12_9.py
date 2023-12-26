# ch12_9.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱
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
        
hungbank = Banks('hung')                    # 定義物件hungbank
usdallor = 50
print(usdallor, " 美金可以兌換 ", hungbank.usa_to_taiwan(usdallor), " 台幣") 











