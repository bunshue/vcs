# F1750 附錄 A-3

def find_missing_nums(data):
    all_data = set(range(1, len(data) + 1))
    return list(all_data - set(data))

print(find_missing_nums([1, 2, 8, 5, 1, 6, 4, 9, 5]))
