from matplotlib.animation import FuncAnimation 
import matplotlib.pyplot as plt   

# 輸出文字, 這個函數將被重複調用
def animate(i):
    label.set_text(string[:i + 1])      # 顯示字串

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 建立動畫需要的 Figure 物件和軸物件
fig, ax = plt.subplots()
# 建立軸物件與設定大小
ax.set(xlim=(-1,1), ylim=(-1,1))
string = '歡迎來到美國'  # 設定字串
# 使用水平與垂直置中在座標 0,0 位置顯示字串
label = ax.text(0,0,string[0],ha='center',va='center',
                fontsize=20, color="b")

# interval = 300, 相當於每隔 0.3 秒執行 animate()動畫
anim = FuncAnimation(fig,animate,
                     frames = len(string),# 字串長度當作frames數
                     interval = 300)
ax.axis('off')

plt.show()
