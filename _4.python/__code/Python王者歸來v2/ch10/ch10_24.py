# ch10_24.py
cars1 = {'Audi', 'Ford', 'Toyota'}
cars2 = {'Nissan', 'Toyota'}
print("執行difference_update( )前列出cars1和cars2內容")
print("cars1 = ", cars1)
print("cars2 = ", cars2)
cars1.difference_update(cars2)
print("執行difference_update( )後列出cars1和cars2內容")
print("cars1 = ", cars1)
print("cars2 = ", cars2)


