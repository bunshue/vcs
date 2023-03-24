# bar 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/popu.txt'

with open(filename, 'r') as fp:
	populations = fp.readlines()

city = list()
popu = list()

for p in populations:
	cc, pp = p.split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(len(city))

plt.bar(ind, popu)
plt.xticks(ind+0.5, city)
#plt.title('台灣各縣市人口統計')


#第二張圖
plt.subplot(232)

print("垂直/水平 長條圖");

#設定將使用的數值
x = ['Chinese', 'English', 'Math', 'Social', 'Nature']
y = [79, 63, 71, 83, 97]

print("垂直長條圖");
#繪製出垂直 Bar，這邊使用的是 bar 函數，設定的是 width 寬度
#plt.bar(x, y, width=0.5, color='red')

print("水平長條圖");
#繪製出水平 Bar，這邊使用的是 barh 函數，設定的是 height 寬度
plt.barh(x, y, height=0.5, color='blue')

#設定 x, y 及圖表標題
plt.xlabel('x label', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize="10") # 設定 y 軸標題標題內容及大小
plt.title('Bar title', fontsize="18") # 設定圖表標題內容及大小

plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")


#第三張圖
plt.subplot(233)


'''
#疊加長條圖的應用

#疊加長條圖是繪製出兩個長條圖，並以推疊的方式繪製而出的

#設定將使用的數值，因為這邊需要兩組數值，因此有 y1, y2
'''

x = ['Chinese', 'English', 'Math', 'Social', 'Nature']
y1 = [30, 26, 37, 22, 28]
y2 = [20, 31, 24, 24, 33]

#Step 3. 將兩條長條圖繪製出來，其中第二條 y2 的 y 軸基底座標是建立在 y1 上

plt.bar(x, y1, width=0.5, label='Male')
plt.bar(x, y2, width=0.5, bottom=y1, label='Female')

#設定 x, y 及圖表標題
plt.xlabel('x label', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize="10") # 設定 y 軸標題標題內容及大小
plt.title('Bar title', fontsize="18") # 設定圖表標題內容及大小

#Step 5. 將圖表顯示出來，並顯示圖例名稱
plt.legend()


#第四張圖
plt.subplot(234)

listx = ['c','c++','c#','java','python']
listy1 = [25,20,20,16,28]
listy2 = [20,8,18,16,22]

plt.bar(listx, listy1, width=0.5, label='男')
plt.bar(listx, listy2, width=0.5, bottom=listy1, label='女')

plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")


#第五張圖
plt.subplot(235)

width = 0.25
listx = ['c','c++','c#','java','python']
listx1 = [x - width/2 for x in range(len(listx))]
listx2 = [x + width/2 for x in range(len(listx))]
listy1 = [25,20,20,16,28]
listy2 = [20,8,18,16,22]

plt.bar(listx1, listy1, width, label='男')
plt.bar(listx2, listy2, width, label='女')

plt.xticks(range(len(listx)), labels=listx)
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")



#第六張圖
plt.subplot(236)


listx = ['c','c++','c#','java','python']
listy = [45,28,38,32,50]

#直式
#plt.bar(listx, listy, width=0.5, color='red')

#橫式
plt.barh(listx, listy, height=0.5, color='red')

plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")



plt.show()




