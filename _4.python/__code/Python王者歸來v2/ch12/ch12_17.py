# ch12_17.py
class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name):
        self.name = animal_name         # 紀錄動物名稱
    def which(self):                    # 回傳動物名稱
        return 'My pet ' + self.name.title()
    def action(self):                   # 動物的行為
        return ' sleeping'

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name):       # 紀錄動物名稱
        super().__init__(dog_name.title())
    def action(self):                   # 動物的行為
        return ' running in the street'

class Monkeys():
    """猴子類別, 這是其他類別 """
    def __init__(self, monkey_name):    # 紀錄動物名稱
        self.name = 'My monkey ' + monkey_name.title()
    def which(self):                    # 回傳動物名稱
        return self.name
    def action(self):                   # 動物的行為
        return ' running in the forest'
    
def doing(obj):                         # 列出動物的行為
    print(obj.which(), "is", obj.action())
    
my_cat = Animals('lucy')                # Animals物件
doing(my_cat)
my_dog = Dogs('gimi')                   # Dogs物件
doing(my_dog)
my_monkey = Monkeys('taylor')           # Monkeys物件
doing(my_monkey)


