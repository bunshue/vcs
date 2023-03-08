import matplotlib.pyplot as plt

#在同一張圖 畫 兩條曲線

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1, listy1, 'r-.s', lw=2, ms=10, label="Male")

listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2, listy2, 'g--*', lw=2, ms=10, label="Female")

plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("費用", fontsize=18)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Money", fontsize=12)
plt.tick_params(axis='y', color='red')

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.show()
