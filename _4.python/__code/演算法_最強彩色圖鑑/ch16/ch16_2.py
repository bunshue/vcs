# ch16_2.py
def subset_generator(data):
    final_subset = [[]]                     # 空集合也算是子集合
    for item in data:
        final_subset.extend([subset + [item] for subset in final_subset])
    return final_subset

data = ['電視', '音響', '筆電']
value = [40000, 50000, 20000]
weight = [3, 4, 1]
bags = subset_generator(data)
max_value = 0                               # 商品總值
for bag in bags:                            # 處理組合商品
    if bag:                                 # 如果不是空集合
        w_sum = 0                           # 組合商品總重量
        v_sum = 0                           # 組合商品總價值
        for b in bag:                       # 拆解商品
            i = data.index(b)               # 了解商品在data的索引
            w_sum += weight[i]              # 加總商品數量
            v_sum += value[i]               # 加總商品價值
            if w_sum <= 4:                  # 如果商品總重量小於4公斤
                if v_sum > max_value:       # 如果總價值大於目前最大價值
                    max_value = v_sum       # 更新最大價值
                    product = bag           # 紀錄商品
                    
print('商品組合 = {},\n商品價值 = {}'.format(product, max_value))



                

           
           
            
    



         



   















