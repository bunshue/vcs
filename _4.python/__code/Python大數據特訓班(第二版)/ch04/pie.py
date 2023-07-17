import matplotlib.pyplot as plt

sizes = [25, 30, 15, 10]
labels = ["北部", "西部", "南部", "東部"]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.2, 0)
plt.pie(sizes, 
	explode = explode, 
	labels = labels, 
	colors = colors,
	labeldistance = 1.1, 
	autopct = "%2.1f%%", 
	pctdistance = 0.6,
	shadow = True,
	startangle = 90)
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" 
plt.rcParams["axes.unicode_minus"] = False	
plt.show()