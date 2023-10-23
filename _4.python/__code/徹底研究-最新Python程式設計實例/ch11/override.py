#子類別覆寫父類別的方法
class Normal(): #父類別
    def subsidy(self, income):
        self.money = income
        if self.money >= 500000:
            print('小康家庭補助金額：', end = ' ')
            return 5000
        
class Poor(Normal): #子類別
    def subsidy(self, income): #覆寫subsidy方法
        self.money = income
        if self.money < 300000:
            print('中低收入家庭補助金額：', end = ' ')
            return 10000

student1 = Normal()#建立父類別物件
print(student1.subsidy(780000),'元')

student2 = Poor()#建立子類別物件
print(student2.subsidy(250000),'元')
