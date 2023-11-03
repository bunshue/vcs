# F1750 練習 02

def my_sum(*numbers):
    output = 0
    for n in numbers:
        output += n
    return output

print(my_sum(10, 20, 30, 40, 50))