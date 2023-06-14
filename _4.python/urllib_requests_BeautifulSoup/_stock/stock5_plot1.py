import matplotlib.pyplot as plt
import numpy as np

print('讀取csv檔')

import matplotlib.pyplot as plt
import csv

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv'
with open(filename, 'r', newline='') as f:
    datas = csv.reader(f)  
    listx = []
    listy = []
    #debug
    #for data in datas:
    #    print(data)
    for data in datas:
        listx.append(data[0])
        listy.append(data[5])

#    print(len(datas))
#    print(len(listx), len(listy))
    plt.figure(figsize=(20,5))	#圖像大小[英吋]
    plt.plot(listx, listy)
    plt.yticks(range(10,200,10))
    plt.show() 
#    print([x[6] for x in datas])

#    print(type(datas))
#%%
#plt.plot([x.close for x in slist]) //tmp comment out
#plt.show() 

plt.show()

