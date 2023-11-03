# F1750 附錄 A-6

def zeroes_to_the_end(data):
    for _ in range(data.count(0)):
        idx = data.index(0)
        data = data[:idx] + data[idx+1:] + data[idx:idx+1]
    return data

print(zeroes_to_the_end([2, 3, 0, 1, 0, 5]))
