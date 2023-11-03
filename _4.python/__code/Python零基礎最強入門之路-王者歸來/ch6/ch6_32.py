# ch6_32.py
James = [['Lebron James','SF','12/30/84'],23,19,22,31,18] # 定義James串列
games = len(James)                                        # 求元素數量
score_Max = max(James[1:games])                           # 最高得分
i = James.index(score_Max)                                # 場次
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名     : ", name)
print("位置     : ", position)
print("出生日期 : ", born)
print("在第 %d 場得最高分 %d" % (i, score_Max))



    
