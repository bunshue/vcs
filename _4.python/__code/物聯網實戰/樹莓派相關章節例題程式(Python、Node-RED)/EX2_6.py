# Example 2.6
score = {'Chen':90, 'Chang':95, 'Lin':65, 'Wang':70, 'Huang':80}
average = 0
K = score.keys()
for i in K:
    scoreValue = score.get(i)
    average = average + scoreValue
    print(i, scoreValue)
print('Average = {0} '.format(average/len(K)))
