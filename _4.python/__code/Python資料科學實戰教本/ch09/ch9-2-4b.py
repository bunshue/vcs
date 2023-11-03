import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5, 6, 15, 3, 12, 4]
explode = (0, 0, 0, 0.2, 0, 0.2)
 
patches, texts = plt.pie(ratings, 
                         labels=labels,
                         explode=explode)
plt.legend(patches, labels, loc="best")
plt.title("程式語言的使用率") 
plt.axis("equal")
plt.show()
