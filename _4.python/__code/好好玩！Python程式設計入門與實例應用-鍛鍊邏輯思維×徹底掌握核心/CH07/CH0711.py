#自訂函式
def student(name, *score, subject = 4):
    if subject >= 1:        
        print(f'{name:6}{subject} 科', end = '')
        #print(f'{name}{subject}{*score}')
        print('分數 ', *score)
    total = sum(score) # 合計分數
    print(f'總分: {total}',
          f'平均: {total / subject:.4f}')

#呼叫函式
student('Peter', 65, 93, 82, 47)
print()
student('Judy', 85, 69, 79, subject = 3)
