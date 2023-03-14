import matplotlib.pyplot as plt

print("subplot 範例")

plt.figure(figsize=[10,8])  #設定圖表大小

plt.subplot(231)
plt.title(label='Chart 231')
plt.plot([1,2,3],'r:o')

plt.subplot(232)
plt.title(label='Chart 232')
plt.plot([1,2,3],'g--o')

plt.subplot(233)
plt.title(label='Chart 233')
plt.plot([1,2,3],'b:o')

plt.subplot(234)
plt.title(label='Chart 234')
plt.plot([1,2,3],'y--o')

plt.subplot(235)
plt.title(label='Chart 235')
plt.plot([1,2,3],'r:o')

plt.subplot(236)
#plt.axes([0.2,0.2,0.4,0.4]) #設定顯示位置
plt.title(label='Chart 236')
plt.plot([1,2,3],'g--o')

plt.show()


