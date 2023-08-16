'''
無 numpy 的 matplotlib

'''

import matplotlib.pyplot as plt

selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

data = [-1, -4.3, 15, 21, 31]

plt.plot(data, "o-r")

plt.show()

print('------------------------------------------------------------')	#60個

days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius)
plt.show()

print('------------------------------------------------------------')	#60個

days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "r-o")
plt.show()


print('------------------------------------------------------------')	#60個

days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "r-o")
plt.grid(True)
plt.show()

print('------------------------------------------------------------')	#60個


days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "g--s")
plt.xlabel("日數")
plt.ylabel("攝氏溫度")
plt.show()

print('------------------------------------------------------------')	#60個

days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "g--s")
print(plt.axis())
plt.show()



print('------------------------------------------------------------')	#60個


days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "g--s")
xmin, xmax, ymin, ymax = 0.5, 6.5, 15, 32.5
plt.axis([xmin, xmax, ymin, ymax])
plt.show()


print('------------------------------------------------------------')	#60個


days = range(1, 7)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日數")
plt.ylabel("攝氏溫度")
plt.axis([0.5, 6.5, 15, 35])
plt.show()





print('------------------------------------------------------------')	#60個

fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
plt.show()


print('------------------------------------------------------------')	#60個

fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Cos(x)", color="blue")
ax2.legend(loc="best")
plt.show()



print('------------------------------------------------------------')	#60個










print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





