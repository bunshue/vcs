# -*- coding: utf-8 -*-

__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
import numpy as np
DataFrame = pd.read_csv('ExpensesRecord.csv')
print(DataFrame["說明"])
print(DataFrame[["說明","支出金額"]] )


df = pd.DataFrame({'Math': [90, 91,92, 93, 94],'English': np.arange(80,85,1) })
print(df[["Math","English"]])

