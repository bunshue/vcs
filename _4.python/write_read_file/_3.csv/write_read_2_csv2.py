from pathlib import Path
import csv

infile = "data/namelist.csv"
f = Path(infile).open(encoding="UTF-8")
dataReader = csv.reader(f)
for row in dataReader:          #取得每一列資料
    for value in row:           #取得資料時，以逗號間隔
        print(value)
        
print("------------------------------------------------------------")  # 60個

from pathlib import Path
import csv

infile = "xxxxx.csv"
try:
    f = Path(infile).open(encoding="UTF-8")
    dataReader = csv.reader(f)
    for row in dataReader:          #取得每一列資料
        for value in row:           #取得資料時，以逗號間隔
            print(value)
except:
    print("無法載入檔案。")

print("------------------------------------------------------------")  # 60個


