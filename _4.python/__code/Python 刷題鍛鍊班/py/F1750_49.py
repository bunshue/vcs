# F1750 練習 49

def num_generator(num):
    return (int(digit) for digit in str(num) if digit.isnumeric())

numbers = num_generator(3.14159)

for num in numbers:
    print(num)
