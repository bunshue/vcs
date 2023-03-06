# python import module : matplotlib bar

'''
#導入模組
import matplotlib.pyplot as plt

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
'''

'''
#目前無法正常顯示中文
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
'''

'''
#將圖表顯示出來
plt.show()
'''


#疊加長條圖的應用

#疊加長條圖是繪製出兩個長條圖，並以推疊的方式繪製而出的

#導入模組

import matplotlib.pyplot as plt

#設定將使用的數值，因為這邊需要兩組數值，因此有 y1, y2

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
#將圖表顯示出來
plt.show()



