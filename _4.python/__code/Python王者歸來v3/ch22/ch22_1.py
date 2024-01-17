# ch22_1.py
import csv

fn = 'csvReport.csv'
with open(fn,encoding='utf-8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    
for row in listReport:                  # 迴圈輸出串列內容
    print(row)



# ch22_2.py
import csv

fn = 'csvReport.csv'
with open(fn,encoding='utf-8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    

print(listReport[0][1], listReport[0][2])
print(listReport[1][2], listReport[1][5])
print(listReport[2][3], listReport[2][6])



# ch22_3.py
import csv

fn = 'csvPeople.csv'
with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:               # 列出DictReader各列內容
        print(row)



# ch22_4.py
import csv

fn = 'csvPeople.csv'
with open(fn) as csvFile:                   # 開啟csv檔案
    csvDictReader = csv.DictReader(csvFile) # 讀檔案建立DictReader物件   
    for row in csvDictReader:               # 列出DictReader各列內容
        print(row['first_name'], row['last_name'])





# ch22_5.py
import csv

fn = 'out22_5.csv'
with open(fn,'w',newline='',encoding="utf-8") as csvFile: # 開啟csv檔案
    csvWriter = csv.writer(csvFile)                     # 建立Writer物件   
    csvWriter.writerow(['姓名', '年齡', '城市'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])


# ch22_6.py
import csv

infn = 'csvReport.csv'                          # 來源檔案
outfn = 'out22_6.csv'                           # 目的檔案
with open(infn,encoding='utf-8') as csvRFile:   # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)            # 讀檔案建立Reader物件
    listReport = list(csvReader)                # 將資料轉成串列 

with open(outfn,'w',newline='',encoding="utf-8") as csvOFile:  
    csvWriter = csv.writer(csvOFile)            # 建立Writer物件   
    for row in listReport:                      # 將串列寫入
        csvWriter.writerow(row)


# ch22_7.py
import csv

fn = 'out22_7.csv'
with open(fn, 'w', newline = '') as csvFile:        # 開啟csv檔案
    csvWriter = csv.writer(csvFile, delimiter='\t') # 建立Writer物件   
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])




# ch22_8.py
import csv

fn = 'out22_8.csv'
with open(fn, 'w', newline = '') as csvFile:                # 開啟csv檔案
    fields = ['Name', 'Age', 'City']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)  # 建立Writer物件

    dictWriter.writeheader()                                # 寫入標題
    dictWriter.writerow({'Name':'Hung', 'Age':'35', 'City':'Taipei'})
    dictWriter.writerow({'Name':'James', 'Age':'40', 'City':'Chicago'})




# ch22_9.py
import csv

# 定義串列,元素是字典
dictList = [{'姓名':'Hung','年齡':'35','城市':'台北'},  
          {'姓名':'James', '年齡':'40', '城市':'芝加哥'}]
          
fn = 'out22_9.csv'
with open(fn, 'w', newline = '', encoding = 'utf-8') as csvFile:  
    fields = ['姓名', '年齡', '城市']
    dictWriter = csv.DictWriter(csvFile,fieldnames=fields)  # 建立Writer物件
    dictWriter.writeheader()                                # 寫入標題
    for row in dictList:                                    # 寫入內容
        dictWriter.writerow(row)



# ch22_10.py
import csv

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)     # 讀取文件下一列
print(headerRow)

for i, header in enumerate(headerRow):
    print(i, header)


# ch22_11.py
import csv

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)         # 讀取文件下一列
    highTemps, lowTemps = [], []        # 設定空串列
    for row in csvReader:
        highTemps.append(row[1])        # 儲存最高溫
        lowTemps.append(row[3])         # 儲存最低溫

print("最高溫 : ", highTemps)
print("最低溫 : ", lowTemps)    




# ch22_19.py
import pickle
game_info = {
    "position_X":"100",
    "position_Y":"200",
    "money":300,
    "pocket":["黃金", "鑰匙", "小刀"]
}

fn = "data19.dat"
fn_obj = open(fn, 'wb')         # 二進位開啟
pickle.dump(game_info, fn_obj)
fn_obj.close()













