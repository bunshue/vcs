import numpy as np

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均數:", sum(population)/10000.0)
  
size_range = [10, 100, 1000]
for sample_size in size_range:
    sample = np.random.choice(a=population, size=sample_size)    
    sample_mean = sample.mean()
    print(sample_size, "樣本平均數:", sample_mean)

