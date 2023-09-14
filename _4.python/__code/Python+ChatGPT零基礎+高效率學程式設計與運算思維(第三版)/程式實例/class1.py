import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


# ex12_4.ipynb
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
    def taiwan_to_usa(self, usa_d):
        self.result = self.__newcal_rate(usa_d)
        return self.result
    def __newcal_rate(self, usa_d):
        return int(usa_d * self.__rate * (1 + self.__service_charge))
    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))
        
hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.save_money(5000)
hungbank.get_balance()
hungbank.withdraw_money(3000)
hungbank.get_balance()
hungbank.save_money(1500)
hungbank.get_balance()
print("購買100元美金")
changedallor = hungbank.taiwan_to_usa(100)
hungbank.withdraw_money(changedallor)
hungbank.get_balance()

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





