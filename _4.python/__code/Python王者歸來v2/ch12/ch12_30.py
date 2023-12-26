# ch12_30.py
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
    __repr__ = __str__

a = Name('Hung')
print(a)


