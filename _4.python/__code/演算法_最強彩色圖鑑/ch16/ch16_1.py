# ch16_1.py
def subset_generator(data):
    ''' 子集合生成函數, data須是可迭代物件 '''
    final_subset = [[]]            # 空集合也算是子集合
    for item in data:
        final_subset.extend([subset + [item] for subset in final_subset])
    return final_subset


data = ['a', 'b', 'c']             
subset = subset_generator(data)
for s in subset:
    print(s)







   















