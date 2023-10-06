import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.7,0.7])
colors = ['b','g','r','y','c']
courses = ['C++','Java','Python','C#','PHP']
students = [45, 52, 66, 32, 39]
plt.barh(courses,students,color=colors)

plt.title("修課報表", fontsize=24, color='b')
plt.xlabel("修課人數", fontsize=12, color='b')
plt.ylabel("課程名稱", fontsize=12, color='b')

plt.show()


      
