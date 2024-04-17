# Filename: ex06_18.py
# 模組與套件
import matplotlib.pyplot as plt
listx1=[1,5,10,15,20,25,30]
listy1=[2,5,7,8,9,13,6]
plt.plot(listx1, listy1, color="black", linewidth=1.0, linestyle="-", label="Boys")
plt.legend()
listx2=[1,5,10,15,20,25,30]
listy2=[4,8,9,12,15,14,8]
plt.plot(listx2, listy2, color="black", linewidth=1.0, linestyle="-.", label="Girls")
plt.legend()
plt.title("Score of Students")
plt.xlabel("No.")
plt.ylabel("Score")
plt.xlim(0,40)
plt.ylim(0,20)
plt.show()