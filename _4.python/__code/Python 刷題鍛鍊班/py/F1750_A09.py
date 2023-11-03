# F1750 附錄 A-9

def reverse_binary(n):
    binary = f'{n:08b}'
    return int(binary[::-1], 2)

print(reverse_binary(121))
