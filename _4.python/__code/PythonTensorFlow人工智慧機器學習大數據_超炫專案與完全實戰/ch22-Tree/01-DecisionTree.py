#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


def gini_index(groups, classes):
    sumSample = float(sum([len(group) for group in groups])) # 計算分割點的所有樣本
    gini = 0.0                                                                                       # 每組的加權基尼係數
    for group in groups:
        size = float(len(group))
        if size == 0:   # 避免除以零
            continue
        score = 0.0
        # 根據每個班級的分數對該組進行評分
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / sumSample) # 通過相對大小對組得分進行加權
    return gini

# 計算Gini
print(gini_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
print(gini_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))