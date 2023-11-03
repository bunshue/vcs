# F1750 附錄 A-8

def reverse_num_digits(x):
    answer = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
    return answer

print(reverse_num_digits(-123))
