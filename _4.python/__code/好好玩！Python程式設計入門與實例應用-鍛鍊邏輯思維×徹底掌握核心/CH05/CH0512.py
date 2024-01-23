# format()函式, f-string

#{}格式碼，欄寬分別為3，6，8 靠右對齊
print('{:>3}{:>6}{:>8}'.format('x', 'x*x', 'x*x*x'))

print('-'*20)
for item in range(1, 11):
    print(f'{item:3d} {item**2:5d} {item**3:7,d}')
