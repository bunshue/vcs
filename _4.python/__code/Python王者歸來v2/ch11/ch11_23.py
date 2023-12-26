# ch11_23.py
def make_icecream(*toppings):
    """ 列出製作冰淇淋的配料 """
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')

