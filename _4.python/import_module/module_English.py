import pandas as pd
import numpy as np
import re
from collections import Counter

with open ("C:/______test_files/Determinant.txt",'r',encoding='UTF-8') as f:
    words=f.read().lower()

rule=re.compile(r'w+')
words=re.findall(rule,words)

counter_words=Counter(words)

common_words=counter_words.most_common(10)




