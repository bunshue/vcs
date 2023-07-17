import pandas as pd
import re
import matplotlib.pyplot as plt

#繪圖中文字型
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
salarylist = []
for i in range(len(city)):
    df1 = df[(df['工作地點'].str.contains(city[i])) & (df['薪資'].str.contains('月薪'))]
    indexlist = df1.index  #取得資料索引
    total = 0  #薪資總額
    for j in range(len(df1)):
        salarytem = df1['薪資'][indexlist[j]].replace(',', '')  #以資料索引取得資料
        salanum = re.findall(r"\d+\.?\d*",salarytem)  #取出資料中的數值
        if len(salanum) == 1:  #若是1個數值即為薪資
            salary = int(salanum[0])
        else:  #若是2個數值則取平均數
            salary = (int(salanum[0])+int(salanum[1]))/2
        total += salary
    salarycity = int(total/len(df1))  #平均薪資
    salarylist.append(salarycity)

ser = pd.Series(salarylist, index=city)  #串列轉Series
print(ser)
plt.ylabel('單位：元')
ser.plot(kind='bar', title='六都電腦職缺薪資', figsize=(5, 5))  #繪製長條圖
