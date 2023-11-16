#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())



