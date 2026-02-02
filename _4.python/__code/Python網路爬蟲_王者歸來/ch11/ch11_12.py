# ch11_12.py
import sqlite3
import matplotlib.pyplot as plt
from pylab import mpl

conn = sqlite3.connect("populations.db")    # 資料庫連線
results = conn.execute("SELECT * from population")

area, male, female, total = [], [], [], []
for record in results:                      # 將人口資料放入串列
    area.append(record[0])
    male.append(record[1])
    female.append(record[2])
    total.append(record[3])       
conn.close()                                # 關閉資料庫連線

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體
seq = area
linemale, = plt.plot(seq, male, '-*', label='男性人口數')
linefemale, = plt.plot(seq, female, '-o', label='女性人口數')
linetotal, = plt.plot(seq, total, '-^', label='總計人口數')

plt.legend(handles=[linemale, linefemale, linetotal], loc='best')
plt.title(u"台北市", fontsize=24)
plt.xlabel("2019年", fontsize=14)
plt.ylabel("人口數", fontsize=14)
plt.show()










