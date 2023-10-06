# 4-6-3 加入靜態 method

import math

class Pizza:
    
    def __init__(self, radious, ingredients):
        self.ingredients = ingredients
        self.radious = radious
    
    def __repr__(self):
        return f'Pizza({self.radious!r}, {self.ingredients!r})'
    
    @classmethod
    def margherita(cls): # 瑪格麗塔披薩
        return cls(4, ['莫扎瑞拉起司', '番茄', '羅勒葉'])
    
    @classmethod
    def prosciutto(cls): # 帕馬火腿披薩
        return cls(4, ['莫扎瑞拉起司', '番茄', '帕馬火腿'])

    def area(self):
        return self.circle_area(self.radious)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


pizza = Pizza(4, ['莫扎瑞拉起司', '義式臘腸'])

print(pizza)
print(pizza.area())
