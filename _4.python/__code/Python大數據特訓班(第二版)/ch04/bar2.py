import matplotlib.pyplot as plt

listy = ['c','c++','c#','java','python']
listx = [45,28,38,32,50]
plt.barh(listy, listx, height=0.5, color='rgb')
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" 
plt.rcParams["axes.unicode_minus"] = False
plt.show()