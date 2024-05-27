import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='DFKai-SB'

datas=[40, 45, 15]
lbls=['現金', '股票', '債券']
exps=[0.2, 0, 0]
clrs=['pink','lightblue','yellow']
plt.pie(datas, labels=lbls, colors=clrs, explode=exps, autopct='%2.1f%%',startangle=0, shadow=True)

plt.show()
