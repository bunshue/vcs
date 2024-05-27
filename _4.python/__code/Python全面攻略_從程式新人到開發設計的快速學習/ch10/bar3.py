import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='mingliu'

areas=['北部','中部','南部','東部']
data1=[800000,580000,640000,420000]
data2=[750000,460000,680000,340000]
plt.bar(areas,data1,label='上半年')
plt.bar(areas,data2,label='下半年',bottom=data1)

plt.legend()
plt.show()

