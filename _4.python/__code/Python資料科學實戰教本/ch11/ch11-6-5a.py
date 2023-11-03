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