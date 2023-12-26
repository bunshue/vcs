# ch11_24.py
def make_icecream(icecream_type, *toppings):
    """ 列出製作冰淇淋的配料 """
    print("這個 ", icecream_type, " 冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('香草', '草莓醬')
make_icecream('芒果', '草莓醬', '葡萄乾', '巧克力碎片')

