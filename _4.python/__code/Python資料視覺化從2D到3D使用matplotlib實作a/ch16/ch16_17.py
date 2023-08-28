# ch16_17.py
import matplotlib.pyplot as plt

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]

bp = plt.boxplot(x,showmeans=True)
outliers = [y.get_ydata() for y in bp["fliers"]]
Q1 = [min(y.get_ydata()) for y in bp["boxes"]]
Q3 = [max(y.get_ydata()) for y in bp["boxes"]]
medians = [y.get_ydata()[0] for y in bp["medians"]]
means = [y.get_ydata()[0] for y in bp["means"]]
whiskers = [y.get_ydata() for y in bp["whiskers"]]
minimum = [y.get_ydata()[0] for y in bp["caps"][::2]]
maximum = [y.get_ydata()[0] for y in bp["caps"][1::2]]
print(f"異常值Outliers : {outliers}")
print(f"     Q1        : {Q1[0]}")
print(f"     Q3        : {Q3[0]}")
print(f"中位數Medians  : {medians[0]}")
print(f"均  值Means    : {means[0]}")
print(f"晶  鬚Whiskers : {whiskers}")
print(f"極小值mimimums : {minimum[0]}")
print(f"極大值maximums : {maximum[0]}")
plt.show()

  
      
