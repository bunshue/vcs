import matplotlib.pyplot as plt
import twstock
import time
#plt.figure(figsize=[12,30])
stock = twstock.Stock('2317') 
slist = []
for i in range(1,13):
    stocklist = stock.fetch(2019,i)
    [slist.append(s) for s in stocklist]
#    listx = [s.date.strftime('%d') for s in stocklist]
#    listy = [s.close for s in stocklist]
#    plt.subplot('62{}'.format(i))
#    plt.xticks(rotation=45)
#    plt.title(label="{}月".format(i))
#    plt.rcParams["font.sans-serif"] = "SimHei" 
#    plt.rcParams["axes.unicode_minus"] = False
#    plt.plot(listx, listy)
    print(len(slist))
    time.sleep(5)
    if i == 6:
        time.sleep(20)
    

#plt.show()

#lista = []
#list1 = [1,2,3,4,5]
#list2 = [7,8,9,10,11]
#list1.append(list2)
#list1
#%%
import csv
with open('2019_2330.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(slist)
#%%
import matplotlib.pyplot as plt
import csv
with open('2019_2330.csv', 'r', newline='') as f:
    datas = csv.reader(f)  
    listx = []
    listy = []
    for data in datas:
        listx.append(data[0])
        listy.append(data[5])

#    print(len(datas))
#    print(len(listx), len(listy))
    plt.figure(figsize=(20,5))
    plt.plot(listx, listy)
    plt.yticks(range(10,200,10))
    plt.show() 
#    print([x[6] for x in datas])

#    print(type(datas))
#%%
plt.figure(figsize=(20,5))
plt.plot([x.close for x in slist])
plt.show() 

#%%
for data in datas:
    print(data)
    
#%%
lsit1=[1,2,3,4]    
list1[0]