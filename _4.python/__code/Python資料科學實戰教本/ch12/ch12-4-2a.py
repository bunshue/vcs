import random

population = (["臺灣閩南語"]*7330) + (["臺灣客家語"]*1200) + \
             (["其他漢語方言"]*1300) + (["原住民語"]*170) 
sample_size = 1000    
sample = random.sample(population, sample_size)
for lang in set(sample):
    print(lang+"比例估計:", sample.count(lang)/sample_size)
    