# ch9_8.py
soldier0 = {'tag':'red', 'score':3, 'xpos':100,
            'ypos':30, 'speed':'slow' }
print("小兵的 x,y 舊座標  = ", soldier0['xpos'], ",", soldier0['ypos'] )
if soldier0['speed'] == 'slow':         # 慢
    x_move = 1
elif soldier0['speed'] == 'medium':     # 中
    x_move = 3
else:
    x_move = 5                          # 快
soldier0['xpos'] += x_move
print("小兵的 x,y 新座標  = ", soldier0['xpos'], ",", soldier0['ypos'] )
