# ch6_23.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
print("使用remove( )刪除串列元素")
expensive = 'bmw'
cars.remove(expensive)            # 刪除第一次出現的元素bmw
print("所刪除的內容是: " + expensive.upper( ) + " 因為太貴了" )
print("新的串列內容",cars)

    
