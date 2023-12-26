# ch14_23.py
fn = 'out14_23.txt'
mystr = ['相見時難別亦難\n', '東風無力百花殘\n', '春蠶到死絲方盡']

with open(fn, 'w', encoding='cp950') as fObj:
    fObj.writelines(mystr)




