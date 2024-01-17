# makefood.py
# 這是一個包含2個函數的模組(module)
def make_icecream(*toppings):
    ''' 列出製作冰淇淋的配料 '''
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

def make_drink(size, drink):
    ''' 輸入飲料規格與種類,然後輸出飲料 '''
    print("所點飲料如下")
    print("--- ", size.title())
    print("--- ", drink.title())






