import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=0, high=2, size=num_throws)
    probability_of_throws = throws.sum()/num_throws
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲" : results})

df.plot(color="b")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()




#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-1-3a.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=1, high=7, size=num_throws)
    mask = (throws == 1)
    probability_of_throws = len(throws[mask])/num_throws    
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲" : results})

df.plot(color="r")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-1.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].mode())
print(s.mode())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-1a.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].median())
print(s.median())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-1b.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].quantile(q=0.25))
print(df["Age"].quantile(q=0.5))
print(df["Age"].quantile(q=0.75))
print(s.quantile(q=0.25))
print(s.quantile(q=0.5))
print(s.quantile(q=0.75))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-1c.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].mean())
print(s.mean())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-2.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].max() - df["Age"].min())
print(s.max() - s.min())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-2a.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].quantile(0.75) - df["Age"].quantile(0.25))
print(s.quantile(0.75) - s.quantile(0.25))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-2b.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].var())
print(s.var())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-2c.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].std())
print(s.std())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-5-2d.py

import pandas as pd

df = pd.read_csv("titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].describe())
print("---------------------------")
print(s.describe())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-2.py

import random

def dice_roll():
    v = random.randint(1, 6)
    return v
    
trials = []    
num_of_trials = 100
for trial in range(num_of_trials):
    trials.append(dice_roll())
print(sum(trials)/float(num_of_trials))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-2a.py

import random
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

def dice_roll():
    v = random.randint(1, 6)
    return v

num_of_trials = range(100, 10000, 10)
avgs = []
for num_of_trial in num_of_trials:  
    trials = []    
    for trial in range(num_of_trial):
        trials.append(dice_roll())
    avgs.append(sum(trials)/float(num_of_trial))

plt.plot(num_of_trials, avgs)
plt.xlabel("試驗次數")
plt.ylabel("平均")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-5.py

from scipy import stats

n = 5
p = 1/6
for k in range(n+1):
    v = stats.binom.pmf(k, n, p)
    print(k, v)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-5a.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

fair_dice_rolls = stats.binom.rvs(n=5, 
                                  p=1/6,
                                  size=10000)
print(fair_dice_rolls)
df = pd.DataFrame(fair_dice_rolls)
df.hist(range=(-0.5, 5.5), bins=6)
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-5b.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

fair_dice_rolls = stats.binom.rvs(n=10, 
                                  p=0.5,
                                  size=10000)
print(fair_dice_rolls)
df = pd.DataFrame(fair_dice_rolls)
df.hist(range=(-0.5, 10.5), bins=11)
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-5c.py

from scipy import stats

n = 10
p = 1/2
for k in range(n+1):
    v = stats.binom.pmf(k, n, p)
    print(k, v)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-5d.py

from scipy import stats

n = 14
p = 0.2
k = 3
v = stats.binom.pmf(k, n, p)
print(k, v)
 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-6.py

import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):
    pi = 3.1415926
    e = 2.718281
    f = (1./np.sqrt(2*pi*sigma**2))*e**(-(x-mu)**2/(2.*sigma**2))
    return f

ax = np.linspace(-5, 5, 100)
ay = [normal_pdf(x, 0, 1) for x in ax]  
plt.plot(ax, ay)
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch11\ch11-6-6a.py

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = [x/10.0 for x in range(-50, 60)]
plt.plot(x, stats.norm.pdf(x, 0, 1),
       'r-', lw=1, alpha=0.6, label='mu=0,sigma=1')
plt.plot(x, stats.norm.pdf(x, 0, 2),
       'b--', lw=1, alpha=0.6, label='mu=0,sigma=2')
plt.plot(x, stats.norm.pdf(x, 2, 1),
       'g-.', lw=1, alpha=0.6, label='mu=2,sigma=1')
plt.legend()
plt.title("常態分配PDF的機率")
plt.show()

print("------------------------------------------------------------")  # 60個

