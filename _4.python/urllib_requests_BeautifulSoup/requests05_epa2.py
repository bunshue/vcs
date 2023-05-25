# PM2.5即時監測顯示器

def get_epa_key():
    filename = 'C:/_git/vcs/_1.data/______test_files1/_key/epa_key.txt'

    import os
    filename = os.path.abspath(filename)
    if not os.path.exists(filename): #檢查檔案是否存在
        print('EPA_KEY 檔案不存在, 離開, 檔案 : ' + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, 'r')
    epa_key = fo.read()
    fo.close()

    length = len(epa_key)
    if length != 36:
        print('EPA_KEY 錯誤, 離開')
        return ""
    return epa_key

epa_key = get_epa_key()
length = len(epa_key)
if length != 36:
    print('EPA_KEY 錯誤, 離開')
    sys.exit(1)	#立刻退出程式


def rbCity():  #點選縣市選項按鈕後處理函式
    global sitelist, listradio
    sitelist.clear()  #清除原有測站串列
    for r in listradio:  #移除原有測站選項按鈕
        r.destroy()
    n=0
    for c1 in data["county"]:  #逐一取出選取縣市的測站
        if(c1 == city.get()):
            sitelist.append(data.iloc[n, 0])
        n += 1    
    sitemake()  #建立測站選項按鈕
    rbSite()  #顯示PM2.5訊息

def rbSite():  #點選測站選項按鈕後處理函式
    n = 0
    for s in data.iloc[:, 0]:  #逐一取得測站
        if(s == site.get()):  #取得點選的測站
            pm = data.iloc[n, 2]  #取得PM2.5的值
            if(pm=='' or pm=='ND'):  #如果沒有資料
                result1.set(s + "站的 PM2.5 值目前無資料！")
            else:  #如果有資料
                if(int(pm) <= 35):  #轉換為等級
                    grade1 = "低"
                elif(int(pm) <= 53):
                    grade1 = "中"
                elif(int(pm) <= 70):
                    grade1 = "高"
                else:
                    grade1 = "非常高"
                result1.set(s + "站的 PM2.5 值為「" + str(pm) + "」：「" + grade1 + "」等級")
            break  #找到點選測站就離開迴圈
        n += 1
    
def clickRefresh():  #重新讀取資料
    global data
    data = pd.read_csv(url)
    rbSite()  #更新測站資料

def sitemake():  #建立測站選項按鈕
    global sitelist, listradio
    for c1 in sitelist:  #逐一建立選項按鈕
        rbtem = tk.Radiobutton(frame2, text=c1, variable=site, value=c1, command=rbSite)  #建立選項按鈕
        listradio.append(rbtem)  #加入選項按鈕串列
        if(c1==sitelist[0]):  #預設選取第1個項目         
            rbtem.select()
        rbtem.pack(side="left")  #靠左排列

import tkinter as tk
import pandas as pd

DataID = 'AQX_P_432'
format = 'csv'
year_month = '2023_04'
offset = '0'
limit = '100'
api_key = epa_key

url = f'https://data.epa.gov.tw/api/v2/{DataID}?format={format}&api_key={api_key}'
print(url)

data = pd.read_csv(url)

window = tk.Tk()
window.geometry("640x270")
window.title("PM2.5 實時監測")

city = tk.StringVar()  #縣市文字變數
site = tk.StringVar()  #測站文字變數
result1 = tk.StringVar()  #訊息文字變數
citylist = []  #縣市串列
sitelist = []  #鄉鎮串列
listradio = []  #鄉鎮選項按鈕串列

#建立縣市串列
for c1 in data["county"]:  
    if(c1 not in citylist):  #如果串列中無該縣市就將其加入
        citylist.append(c1)
#建立第1個縣市的測站串列
count = 0
for c1 in data["county"]:  
    if(c1 ==  citylist[0]):  #是第1個縣市的測站
        sitelist.append(data.iloc[count, 0])
    count += 1

label1 = tk.Label(window, text="縣市：", pady=6, fg="blue", font=("新細明體", 12))
label1.pack()
frame1 = tk.Frame(window)  #縣市容器
frame1.pack()
for i in range(0,3):  #3列選項按鈕
    for j in range(0,8):  #每列8個選項按鈕
        n = i * 8 + j  #第n個選項按鈕
        if(n < len(citylist)):
            city1 = citylist[n]  #取得縣市名稱
            rbtem = tk.Radiobutton(frame1, text=city1, variable=city, value=city1, command=rbCity)  #建立選項按鈕
            rbtem.grid(row=i, column=j)  #設定選項按鈕位置
            if(n==0):  #選取第1個縣市
                rbtem.select()

label2 = tk.Label(window, text="測站：", pady=6, fg="blue", font=("新細明體", 12))
label2.pack()
frame2 = tk.Frame(window)  #測站容器
frame2.pack()
sitemake()

btnDown = tk.Button(window, text="更新資料", font=("新細明體", 12), command=clickRefresh)
btnDown.pack(pady=6)
lblResult1 = tk.Label(window, textvariable=result1, fg="red", font=("新細明體", 16))
lblResult1.pack(pady=6)
rbSite()  #顯示測站訊息

window.mainloop()
