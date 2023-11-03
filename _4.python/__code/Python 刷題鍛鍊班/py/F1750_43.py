# F1750 練習 43

class Animal:
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num
    
    def __repr__(self):
        return f'{self.species}(color={self.color!r}, leg_num={self.leg_num})'

class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

elephant = Elephant('灰')
zebra = Zebra('黑白')
snake = Snake('綠')
parrot = Parrot('灰')

print(elephant)
print(zebra)
print(snake)
print(parrot)
