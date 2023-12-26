# ch13_39.py
from collections import Counter

fruits = ["apple","orange","apple"]
fruitsdict = Counter(fruits)
myfruits1 = fruitsdict.most_common()
print(myfruits1)
myfruits0 = fruitsdict.most_common(0)
print(myfruits0)
myfruits1 = fruitsdict.most_common(1)
print(myfruits1)
myfruits2 = fruitsdict.most_common(2)
print(myfruits2)

















