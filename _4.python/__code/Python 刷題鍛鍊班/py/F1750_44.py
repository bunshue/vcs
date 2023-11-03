# F1750 練習 44

class Animal():
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num
    
    def __repr__(self):
        return f'{self.color}色 {self.species} ({self.leg_num} 條腿)'

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

class Exhibit():
    def __init__(self, id_num):
        self.id_num = id_num
        self.animals = []
    
    def add_animals(self, *new_animals):
        for animal in new_animals:
            self.animals.append(animal)
    
    def __repr__(self):
        return f'展示區編號 {self.id_num}: ' + \
               f'{", ".join([str(animal) for animal in self.animals])}'

ex1 = Exhibit(1)
ex2 = Exhibit(2)

ex1.add_animals(Elephant('灰'), Zebra('黑白'))
ex2.add_animals(Snake('綠'), Parrot('灰'))

print(ex1)
print(ex2)
