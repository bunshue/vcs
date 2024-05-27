import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='DFKai-SB'

plt.plot(['A','B','C','D'],[76,85,64,92],label='數學')
plt.plot(['A','B','C','D'],[100,75,84,54],'--',label='英語')
plt.plot([86,90,48,88],'-.',label='電腦')		#X軸資料相同時可省略

plt.legend()    # 使用legend()方法顯示圖例
plt.show()

