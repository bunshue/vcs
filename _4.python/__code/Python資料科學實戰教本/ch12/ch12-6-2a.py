import numpy as np
import pandas as pd

voter_gender = np.array((["男"]*352)+(["男"]*315)+ \
                        (["女"]*217)+(["女"]*331))
voter_favorite = np.array((["喜歡"]*352)+(["不喜歡"]*315)+ \
                          (["喜歡"]*217)+(["不喜歡"]*331))
voters = pd.DataFrame({"gender":voter_gender,
                       "favorite":voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)
print("---------------------------")
expected = np.outer(voter_tab["小計"][0:2],
                    voter_tab.loc["小計"][0:2]) / 1215
expected = pd.DataFrame(expected)
expected.columns = ["喜歡", "不喜歡"]
expected.index = ["男", "女"]                   
print(expected)
 