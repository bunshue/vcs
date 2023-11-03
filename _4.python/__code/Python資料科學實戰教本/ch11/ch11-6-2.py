import random

def dice_roll():
    v = random.randint(1, 6)
    return v
    
trials = []    
num_of_trials = 100
for trial in range(num_of_trials):
    trials.append(dice_roll())
print(sum(trials)/float(num_of_trials))
