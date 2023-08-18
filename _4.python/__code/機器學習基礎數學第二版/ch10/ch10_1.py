# ch10_1.py
import matplotlib.pyplot as plt                                  
x = [x for x in range(0, 11)]                   
y = [7.5*y - 3.33 for y in x]
plt.axis([0, 4, 0, 25])
plt.plot(x, y)   
plt.plot(1, 5, '-o')
plt.plot(2, 10, '-o')
plt.plot(3, 20, '-o')
plt.xlabel('Times:unit=100')
plt.ylabel('Voucher:unit=100')
plt.grid()                              # 加格線
plt.show()


