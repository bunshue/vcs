import sqlite3
import numpy as np
import matplotlib.pyplot as plt

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'

print("油價走勢圖")

print('建立資料庫連線, 資料庫 : ' + db_filename)
conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.execute('SELECT * FROM prices ORDER BY gdate;')

data = []
cnt = 0
for row in cursor:
    data.append(list(row))
    cnt = cnt + 1
    '''
    if cnt == 20:
        break
    '''
x = np.arange(0,len(data))
dataset = [list(), list(), list()]
for i in range(0, len(data)):
    for j in range(0,3):
        dataset[j].append(data[i][j + 1])
w = np.array(dataset[0])    #92
y = np.array(dataset[1])    #95
z = np.array(dataset[2])    #98
plt.ylabel("NTD$")
plt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data) - 1][0]))
plt.plot(x, w, color = "blue", label = "92")
plt.plot(x, y, color = "red", label = "95")
plt.plot(x, z, color = "green", label = "98")
plt.xlim(0,len(data))
plt.ylim(10,40)
plt.title("Gasoline Prices Trend (Taiwan)")
plt.legend()
plt.show()

