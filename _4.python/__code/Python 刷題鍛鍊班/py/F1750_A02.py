# F1750 附錄 A-2

def find_majority_num(data):
    counter = [(data.count(i), i) for i in set(data)]
    return sorted(counter, reverse=True)[0][1]
    """
    import statistics
    return statistics.mode(data)
    """

print(find_majority_num([1, 2, 2, 3, 2, 3, 1]))
