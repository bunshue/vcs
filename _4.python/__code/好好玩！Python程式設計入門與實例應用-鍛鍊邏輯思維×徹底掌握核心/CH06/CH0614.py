#應用一：計算分數平均
score = [(85, 75, 46, 91), (49, 76, 87),
        (76, 93, 67)]
avg = [sum(item)/len(item) for item in score]
print(f'平均: {avg[0]:.3f}, {avg[1]:.3f},\
      {avg[2]:.3f}')
print() #換行

#應用二：讀取字串長度
fruit = ['lemon', 'apple', 'orange', 'blueberry']
print('%9s'%'字串', '%2s'%'長度')
print('*----------------*')
print('\n'.join(['%10s:%2d'%(
    item, len(item)) for item in fruit]))
