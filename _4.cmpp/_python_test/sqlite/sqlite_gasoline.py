import sqlite3
import numpy as np
import matplotlib.pyplot as plt

def disp_menu():
    print("中油歷年油價查詢系統")
    print("------------")
    print("1.顯示歷年油價資訊")
    print("2.最近10週油價資訊")
    print("3.油價走勢圖")
    print("0.結束")
    print("------------")

def disp_alldata():
    conn = sqlite3.connect('gasoline.sqlite')
    cursor = conn.execute('select * from prices order by gdate desc;')

    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". \
            format(row[0],row[1],row[2],row[3]))
        n = n + 1
        '''
        if n == 20:
            x = input("請按Enter鍵繼續...(Q:回主選單)")
            if x == 'Q' or x == 'q': break
            n = 0
        '''
def disp_10data():
    conn = sqlite3.connect('gasoline.sqlite')
    cursor = conn.execute('select * from prices order by gdate desc;')
    
    n = 0
    for row in cursor:
        print("日期：{}，92無鉛：{}，95無鉛：{}，98無鉛：{}". \
            format(row[0],row[1],row[2],row[3]))
        n = n + 1
        if n == 10:
            break

def chart():
    conn = sqlite3.connect('gasoline.sqlite')
    cursor = conn.execute('select * from prices order by gdate;')
    
    data = []
    for row in cursor:
        data.append(list(row))
    x = np.arange(0,len(data))
    dataset = [list(), list(), list()]
    for i in range(0, len(data)):
        for j in range(0,3):
            dataset[j].append(data[i][j+1])
    w = np.array(dataset[0])
    y = np.array(dataset[1])
    z = np.array(dataset[2])
    plt.ylabel("NTD$")
    plt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data)-1][0]))
    plt.plot(x, w, color="blue", label="92")
    plt.plot(x, y, color="red", label="95")
    plt.plot(x, y, color="green", label="98")
    plt.xlim(0,len(data))
    plt.ylim(10,40)
    plt.title("Gasoline Prices Trend (Taiwan)")
    plt.legend()
    plt.show()

while True:
    print()
    disp_menu()
    sel = input("請輸入您的選擇:")
    if sel < '0' or sel > '3':
        continue
    
    choice = int(sel)

    if choice == 0 :
        break
    if choice == 1: 
        disp_alldata()
    elif choice == 2:
        disp_10data()
    elif choice == 3:
        chart()
    else:
        break



