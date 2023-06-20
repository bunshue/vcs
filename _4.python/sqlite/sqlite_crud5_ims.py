#同一個資料庫內 可以放多個table table名稱不同即可

#----------------------------------------------------------------

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/ims_20221218_1.csv'

import csv

with open(filename, encoding = 'big5') as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)    #將資料轉成list


length = len(listReport)

print('len = ', length)

#print(listReport)

for row in listReport:
    print(row)


    



#----------------------------------------------------------------




#----------------------------------------------------------------



