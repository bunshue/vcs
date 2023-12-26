# ch7_39.py
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
fruit = 'apple'
print("刪除前的fruits", fruits)
while fruit in fruits:      # 只要串列內有apple迴圈就繼續
    fruits.remove(fruit)
print("刪除後的fruits", fruits)
    


