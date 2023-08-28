# ch16_16.py
import matplotlib.pyplot as plt

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]

bp = plt.boxplot(x,showmeans=True)
outliers = [y.get_ydata() for y in bp["fliers"]]
boxes = [y.get_ydata() for y in bp["boxes"]]
medians = [y.get_ydata() for y in bp["medians"]]
means = [y.get_ydata() for y in bp["means"]]
whiskers = [y.get_ydata() for y in bp["whiskers"]]
caps = [y.get_ydata() for y in bp["caps"]]
print(f"異常值Outliers : {outliers}")
print(f"盒  子Boxes    : {boxes}")
print(f"中位數Medians  : {medians}")
print(f"均  值Means    : {means}")
print(f"晶  鬚Whiskers : {whiskers}")
print(f"帽  子caps     : {caps}")
plt.show()


      
