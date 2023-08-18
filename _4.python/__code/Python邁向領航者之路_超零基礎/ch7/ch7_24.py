# ch7_24.py
sum = 0
for i in range(64):
    if i == 0:
        wheat = 1
    else:
        wheat = 2 ** i
    sum += wheat       
print('麥粒總共 = {}'.format(sum))







        





