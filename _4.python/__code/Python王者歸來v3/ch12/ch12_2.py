# ch12_2.py
class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'    # 定義屬性
    def motto(self):            # 定義方法
        return "以客為尊"

userbank = Banks()              # 定義物件userbank
print("目前服務銀行是 ", userbank.bankname)
print("銀行服務理念是 ", userbank.motto())


