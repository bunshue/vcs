import pandas as pd
import matplotlib.pyplot as plt

#繪圖中文字型
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
citycount = []  #存六都工作職缺數量的串列
for i in range(len(city)):
    df1 = df[df['工作地點'].str.contains(city[i])]  #取出包含指定地點的資料
    citycount.append(len(df1))

ser = pd.Series(citycount, index=city)  #串列轉Series
print(ser)
plt.axis('off')
ser.plot(kind='pie', title='六都電腦職缺數量', figsize=(6, 6))  #繪製圓餅圖
