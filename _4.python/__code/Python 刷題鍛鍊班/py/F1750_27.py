# F1750 練習 27

import random

def set_password_source(source):
    def password_gen(length):
        output = []
        for i in range(length):
            output.append(random.choice(source))
        return ''.join(output)
    return password_gen

my_password_gen = set_password_source('0123456789abcdefghij')
print(my_password_gen(10))
