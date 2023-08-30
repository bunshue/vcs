
print('------------------------------------------------------------')	#60個

def make_icecream(*toppings):
    # 列出製作冰淇淋的配料
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

def make_drink(size, drink):
    # 輸入飲料規格與種類,然後輸出飲料
    print("所點飲料如下")
    print("--- ", size.title())
    print("--- ", drink.title())

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
make_drink('large', 'coke')

print('------------------------------------------------------------')	#60個

import makefood         # 導入模組makefood.py

makefood.make_icecream('草莓醬')
makefood.make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
makefood.make_drink('large', 'coke')

print('------------------------------------------------------------')	#60個

from makefood import make_icecream  # 導入模組makefood.py的函數make_icecream

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
make_drink('large', 'coke')         # 因為沒有導入此函數所以會產生錯誤

print('------------------------------------------------------------')	#60個

# 導入模組makefood.py的make_icecream和make_drink函數
from makefood import make_icecream, make_drink  

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
make_drink('large', 'coke')         

print('------------------------------------------------------------')	#60個

from makefood import *      # 導入模組makefood.py所有函數

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
make_drink('large', 'coke')         

print('------------------------------------------------------------')	#60個


