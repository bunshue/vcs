import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='mingliu'

areas=['北部','中部','南部','東部']
width=0.4
x1=[x-width/2 for x in range(len(areas))]
x2=[x+width/2 for x in range(len(areas))]
data1=[800000,580000,640000,420000]
data2=[750000,460000,680000,340000]
plt.bar(x1,data1,width,label='上半年')
plt.bar(x2,data2,width,label='下半年')
plt.xticks(range(len(areas)),labels=areas)

plt.legend()
plt.show()
