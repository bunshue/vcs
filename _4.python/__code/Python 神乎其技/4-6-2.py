# 4-6-2 用 @classmethod 當作工廠函式

class Pizza:
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    
    @classmethod
    def margherita(cls):
        return cls(['莫扎瑞拉起司', '番茄', '羅勒葉'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['莫扎瑞拉起司', '番茄', '帕馬火腿'])


pizza1 = Pizza.margherita()
pizza2 = Pizza.prosciutto()
pizza3 = Pizza(['莫扎瑞拉起司', '義式臘腸'])

print(pizza1)
print(pizza2)
print(pizza3)