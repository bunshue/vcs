# ch10_13.py
cocktail = {
    'Blue Hawaiian':{'Rum','Sweet Wine','Cream','Pineapple Juice','Lemon Juice'},
    'Ginger Mojito':{'Rum','Ginger','Mint Leaves','Lime Juice','Ginger Soda'},
    'New Yorker':{'Whiskey','Red Wine','Lemon Juice','Sugar Syrup'},
    }
# 列出含有Lemon Juice的酒
print("含有Lemon Juice的酒 : ")
for name, formulas in cocktail.items():
    if 'Lemon Juice' in formulas:
        print(name)
# 列出含有Rum但是沒有薑的酒
print("含有Rum但是沒有薑的酒 : ")
for name, formulas in cocktail.items():
    if 'Rum' in formulas and not ('Ginger' in formulas):
        print(name)






