import pandas as pd
import numpy as np
import re
from collections import Counter

with open(
    "D:/_git/vcs/_1.data/______test_files1/Determinant.txt", "r", encoding="UTF-8"
) as f:
    words = f.read().lower()

rule = re.compile(r"w+")
words = re.findall(rule, words)

counter_words = Counter(words)

common_words = counter_words.most_common(10)
