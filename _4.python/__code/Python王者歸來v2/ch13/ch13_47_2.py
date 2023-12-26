# ch13_47_2.py
import itertools

single = 0                      # 單眼皮
double = 0                      # 雙眼皮
counter = 0                     # 組合計數
x = ['F', 'f', 'F', 'f']        # 基因組合
r = 2                           # 一對

for gene in itertools.combinations(x, r):
    if 'F' in gene:
        double += 1
    else:
        single += 1
    counter += 1
       
print("單眼皮機率 : %5.3f" % (single / counter))
print("雙眼皮機率 : %5.3f" % (double / counter))



        
















