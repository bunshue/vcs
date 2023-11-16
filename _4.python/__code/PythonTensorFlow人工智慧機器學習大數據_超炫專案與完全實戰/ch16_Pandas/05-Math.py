# -*- coding: utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
DataFrame = pd.read_csv('ExpensesRecord.csv')
DataFrame["單價"]=DataFrame["支出金額"]/DataFrame["數量"]
print(DataFrame[["數量","支出金額","單價"]] )


