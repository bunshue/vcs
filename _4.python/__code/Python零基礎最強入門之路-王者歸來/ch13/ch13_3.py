# ch13_3.py
from makefood import make_icecream  # 導入模組makefood.py的函數make_icecream

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
make_drink('large', 'coke')         # 因為沒有導入此函數所以會產生錯誤

