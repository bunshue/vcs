import pandas as pd

products = pd.DataFrame({
        "分類": ["居家", "居家", "娛樂", "娛樂", "科技", "科技"],
        "商店": ["家樂福", "頂好", "家樂福", "全聯", "頂好","家樂福"],
        "價格":[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
        "測試分數": [4, 3, 5, 7, 5, 8]})
print(products)
products.to_html("ch8-5-2-01.html")
print("---------------------------")
# 呼叫 pivot_table() 方法
pivot_products = products.pivot_table(index='分類',columns='商店',values='價格')
print(pivot_products)
pivot_products.to_html("ch8-5-2-02.html")