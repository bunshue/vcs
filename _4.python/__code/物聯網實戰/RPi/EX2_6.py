# Homework 2-6
score = {'Chen':90, 'Chang':95, 'Lin':65, 'Wang':70, 'Huang':80}
average = 0
K = score.keys()
count = 0
for i in K:
    count = count + 1
    scoreValue = score.get(i)
    average = average + scoreValue
    print(i, scoreValue)
print('Average = {0} '.format(average/count))
