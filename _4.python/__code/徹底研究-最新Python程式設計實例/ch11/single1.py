class MobilePhone: #基礎類別
    def touch(self):
        print('我能提供螢幕觸控操作的功能')
        
class HTC(MobilePhone): #衍生類別
    def touch(self):
        MobilePhone.touch(self)
        print('我也能提供多點觸控的操作方式')

#產生子類別實體
u11 = HTC()
u11.touch()
