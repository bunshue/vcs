# -*- coding: utf-8 -*-
name = ["東","西","南","北","中"]
data = [43.0, 45.4, 44.8, 47.4, 46.4, 47.5, 
      43.3, 44.1, 45.1, 37.2, 31.7, 37.6, 
      33.3, 31.9, 39.9, 38.2, 32.6, 38.5, 
      41.2, 40.2, 41.0, 32.7, 37.8, 34.7, 
      40.0, 37.9, 38.1, 42.0, 45.5, 41.2, 
      32.2, 39.9, 46.4, 44.5, 46.0, 47.9, 
      37.5, 31.4, 32.6, 42.6, 33.5, 45.4, 
      49.0, 42.7, 39.7]
value = []
i = 0
for x in range(5):
    value.append([])
    for y in range(3):
        lst = data[i : i + 3]
        i = i + 3
        high = max(lst)
        if (high >= 40):
            value[x].append(high)
for x in range(5):
    days = len(value[x])
    if (days == 0):
        print(f"{name[x]}區噪音值正常")
    else:
        for y in value[x]:
            print(y)
        print(f"{name[x]}區噪音值超標{days}天，平均值={sum(value[x])/days}")    

