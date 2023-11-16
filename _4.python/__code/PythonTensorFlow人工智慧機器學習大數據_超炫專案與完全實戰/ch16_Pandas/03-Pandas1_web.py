#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import pandas as pd

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0].head(5) )


#df = pd.read_html('http://news.baidu.com/tech')
#print(df[0].head(5) )





