import matplotlib.pyplot as plt
import pandas as pd

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}

df = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df)
df.plot(xticks=range(len(df.index)),
        use_index=True)

df.plot(xticks=range(len(df.index)),
        use_index=True,
        rot=90)
plt.show()