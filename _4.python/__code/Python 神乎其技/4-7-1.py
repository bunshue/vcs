# 4-7-1 類別與物件變數

class Dog:
    
    num_legs = 4
    
    def __init__(self, name):
        self.name = name


jack = Dog('傑克')
jill = Dog('吉兒')

print('jack.num_legs =', jack.num_legs)
print('jill.num_legs =', jill.num_legs)
print('Dog.num_legs =', Dog.num_legs)

Dog.num_legs = 6

print('jack.num_legs =', jack.num_legs)
print('jill.num_legs =', jill.num_legs)
print('Dog.num_legs =', Dog.num_legs)

Dog.num_legs = 4
jack.num_legs = 6

print('jack.num_legs =', jack.num_legs)
print('jack.__class__.num_legs =', jack.__class__.num_legs)
print('jill.num_legs =', jill.num_legs)
print('Dog.num_legs =', Dog.num_legs)