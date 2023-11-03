# F1750 附錄 A-1

def sum_of_two(data, k):
    for a_index, a_value in enumerate(data):
        for b_index, b_value in enumerate(data):
            if a_index != b_index and a_value + b_value == k:
                return [a_index, b_index]
    return []

print(sum_of_two([2, 7, 11, 15], 9))
