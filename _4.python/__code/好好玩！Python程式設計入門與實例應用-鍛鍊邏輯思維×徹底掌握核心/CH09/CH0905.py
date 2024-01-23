# 產生父類別 或稱 基礎類別
class Father:
    def walking(self):
        print('多走路有益健康!')
        
#產生子類別 或稱 衍生類別
class Son(Father):
    pass

#產生子類別實體 - 即物件
Joe = Son()
Joe.walking()
