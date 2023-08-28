# ch13_7.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
colors = ['grey','grey','red','grey','grey']
courses = ['C++','Java','Python','C#','PHP']
students = [45, 52, 66, 32, 39]
plt.bar(courses,students,color=colors)
plt.title("修課報表", fontsize=24, color='b')
plt.xlabel("課程名稱", fontsize=14, color='b')
plt.ylabel("修課人數", fontsize=14, color='b')
plt.show()


      
