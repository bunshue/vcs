import random
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

def dice_roll():
    v = random.randint(1, 6)
    return v

num_of_trials = range(100, 10000, 10)
avgs = []
for num_of_trial in num_of_trials:  
    trials = []    
    for trial in range(num_of_trial):
        trials.append(dice_roll())
    avgs.append(sum(trials)/float(num_of_trial))

plt.plot(num_of_trials, avgs)
plt.xlabel("試驗次數")
plt.ylabel("平均")
plt.show()
