import pandas as pd
import numpy as np
import random

my_array = np.arange(10)  # [0 1 2 3 4]

print('原list')
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

sum_my_array = sum(my_array)
print('和')
print(sum_my_array)

'''
index = []
ran = random.sample(range(0, 10),2)
for i in ran:
    index.append(i)
index.sort()
'''


'''

       
        

        rand = random.random() #輸出為0-1範圍的實數


            index = self.shuffle_index(self.total_size)
        
        self.shuffle_index(self.pop_size+self.crossover_size)

    def shuffle_mutation(self,p1,c1):
        for i in range(self.number_of_genes):
            self.chromosomes[c1][i] = self.chromosomes[p1][i]
        ran = random.sample(range(0,self.number_of_genes),12)
        for i in ran: #隨機選擇12個基因進行突變
            if(self.chromosomes[c1][i]==0):
                self.chromosomes[c1][i] = 1
            else:
                self.chromosomes[c1][i] = 0

pop_size = 2
selection_type = SelectionType.Stochastic
crossover_type = CrossoverType.more #single double more
crossover_rate = 1         
mutation_type = MutationType.Inversion
mutation_rate = 0.5
number_of_genes =60 
solver = GeneticAlgorithm(pop_size,number_of_genes,selection_type,
                          crossover_type,crossover_rate,
                          mutation_type,mutation_rate,
                          )
solver.initialize()
solver.evaluate_fitness()
for i in range(100):
    solver.perform_crossover_operation()
    solver.perform_mutation_operation()
    solver.update_best_solution()
    solver.perform_selection()

    if(i %10 ==0):
         print(F"iteration {i} :")
         print(f"{solver.best_chromosome}: {solver.countbyflexsim(solver.best_chromosome)}")
outdata = "exit"
s.send(outdata.encode())

'''



