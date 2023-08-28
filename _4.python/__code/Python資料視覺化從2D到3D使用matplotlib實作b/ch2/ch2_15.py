# ch2_15.py
import matplotlib.pyplot as plt

d1 = [10 for y in range(1, 9)]          # data1線條之y值
d2 = [20 for y in range(1, 9)]          # data2線條之y值
d3 = [30 for y in range(1, 9)]          # data3線條之y值
d4 = [40 for y in range(1, 9)]          # data4線條之y值
d5 = [50 for y in range(1, 9)]          # data5線條之y值
d6 = [60 for y in range(1, 9)]          # data6線條之y值
d7 = [70 for y in range(1, 9)]          # data7線條之y值
d8 = [80 for y in range(1, 9)]          # data8線條之y值
d9 = [90 for y in range(1, 9)]          # data9線條之y值
d10 = [100 for y in range(1, 9)]        # data10線條之y值
d11 = [110 for y in range(1, 9)]        # data11線條之y值
d12 = [120 for y in range(1, 9)]        # data12線條之y值

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(seq,d1,'-1',seq,d2,'-2',seq,d3,'-3',seq,d4,'-4',
         seq,d5,'-s',seq,d6,'-p',seq,d7,'-*',seq,d8,'-+',
         seq,d9,'-D',seq,d10,'-d',seq,d11,'-H',seq,d12,'-h')   
plt.show()


