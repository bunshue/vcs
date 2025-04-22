"""
test_my_module

"""

import os
import sys

print("使用自定義模組")

# 匯入 指定目錄下的模組
sys.path.append(r"C:\_git\vcs\_4.python\import_module\mm")
# print(sys.path)

import mm

mm.show()
print(mm.name)
mm.name = "usemodule.py"
print(mm.name)

print("------------------------------------------------------------")  # 60個

from mm import say_hello

say_hello()

mm.say_hello()

print("------------------------------------------------------------")  # 60個

cc = mm.numRand2(14, 52)
print(cc)

print(mm.__name__)

print(__name__)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 取得另外一個檔案內的資料

from mm import (
    sales_data,
    inventory_data,
    product_data,
    sales_year_data,
    inventory_month_data,
)

print(sales_data)
print(inventory_month_data)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
