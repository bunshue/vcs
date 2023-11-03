# F1750 練習 29

def sum_numbers(data):
    return sum([int(d)
                for d in data.split()
                if d.isdigit()])

print(sum_numbers('10 abc 20 de44 30 55fg 40'))
