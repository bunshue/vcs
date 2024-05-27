import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='mingliu'	#指定為明體字

plt.rcParams['font.sans-serif']='mingliu'
plt.plot(['A','B','C','D'],[76,85,64,92])
plt.title('班級成績比較表',fontsize=12)
plt.xlabel('班級')
plt.ylabel('分數')

plt.show()

