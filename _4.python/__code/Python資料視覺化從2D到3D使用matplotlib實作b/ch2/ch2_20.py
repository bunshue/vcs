# ch2_20.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

temperature = [23, 22, 20, 24, 22, 22, 23, 20, 17, 18,
               20, 20, 16, 14, 14, 20, 20, 20, 15, 14,
               14, 14, 14, 16, 16, 16, 18, 21, 21, 20,
               16]
x = [x for x in range(1,len(temperature)+1)]        
plt.plot(x, temperature)
plt.title("天氣報表", fontsize=24)
plt.xlabel('日期')
plt.ylabel('溫度')
plt.savefig('out2_20.png')      # 儲存圖表檔案
plt.show()


