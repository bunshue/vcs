# ch10_29.py
# 供應商 A 和 B 的產品列表
supplier_a_products = {"apple", "banana", "cherry", "date", "elderberry"}
supplier_b_products = {"banana", "cherry", "fig", "grape"}

# 找到共同產品
common_products = supplier_a_products.intersection(supplier_b_products)
print(f"共同產品 : {common_products}")

# 找到只由供應商 A 提供的獨特產品
unique_to_a = supplier_a_products - supplier_b_products
print(f"供應商 A 的獨特產品 : {unique_to_a}")

# 找到只由供應商 B 提供的獨特產品
unique_to_b = supplier_b_products - supplier_a_products
print(f"供應商 B 的獨特產品 : {unique_to_b}")

# 所有提供的產品
all_products = supplier_a_products.union(supplier_b_products)
print(f"所有產品 : {all_products}")


