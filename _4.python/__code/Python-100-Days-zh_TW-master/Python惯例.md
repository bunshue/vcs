## Python慣例

“慣例”這個詞指的是“習慣的做法，常規的辦法，一貫的做法”，與這個詞對應的英文單詞叫“idiom”。由於Python跟其他很多編程語言在語法和使用上還是有比較顯著的差別，因此作為一個Python開發者如果不能掌握這些慣例，就無法寫出“Pythonic”的代碼。下面我們總結了一些在Python開發中的慣用的代碼。

1. 讓代碼既可以被導入又可以被執行。

   ```Python
   if __name__ == '__main__':
   ```


2. 用下面的方式判斷邏輯“真”或“假”。

   ```Python
   if x:
   if not x:
   ```

   **好**的代碼：

   ```Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': '駱昊', '1002': '王大錘'}
   if name and fruits and owners:
       print('I love fruits!')
   ```

   **不好**的代碼：

   ```Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': '駱昊', '1002': '王大錘'}
   if name != '' and len(fruits) > 0 and owners != {}:
       print('I love fruits!')
   ```

3. 善於使用in運算符。

   ```Python
   if x in items: # 包含
   for x in items: # 迭代
   ```

   **好**的代碼：

   ```Python
   name = 'Hao LUO'
   if 'L' in name:
       print('The name has an L in it.')
   ```

   **不好**的代碼：

   ```Python
   name = 'Hao LUO'
   if name.find('L') != -1:
       print('This name has an L in it!')
   ```

4. 不使用臨時變量交換兩個值。

   ```Python
   a, b = b, a
   ```

5. 用序列構建字符串。

   **好**的代碼：

   ```Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
   name = ''.join(chars)
   print(name)  # jackfrued
   ```

   **不好**的代碼：

   ```Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
   name = ''
   for char in chars:
       name += char
   print(name)  # jackfrued
   ```

6. EAFP優於LBYL。

   EAFP - **E**asier to **A**sk **F**orgiveness than **P**ermission.

   LBYL - **L**ook **B**efore **Y**ou **L**eap.

   **好**的代碼：

   ```Python
   d = {'x': '5'}
   try:
       value = int(d['x'])
       print(value)
   except (KeyError, TypeError, ValueError):
       value = None
   ```

   **不好**的代碼：

   ```Python
   d = {'x': '5'}
   if 'x' in d and isinstance(d['x'], str) \
   		and d['x'].isdigit():
       value = int(d['x'])
       print(value)
   else:
       value = None
   ```

7. 使用enumerate進行迭代。

   **好**的代碼：

   ```Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   for index, fruit in enumerate(fruits):
   	print(index, ':', fruit)
   ```

   **不好**的代碼：

   ```Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   index = 0
   for fruit in fruits:
       print(index, ':', fruit)
       index += 1
   ```

8. 用生成式生成列表。

   **好**的代碼：

   ```Python
   data = [7, 20, 3, 15, 11]
   result = [num * 3 for num in data if num > 10]
   print(result)  # [60, 45, 33]
   ```

   **不好**的代碼：

   ```Python
   data = [7, 20, 3, 15, 11]
   result = []
   for i in data:
       if i > 10:
           result.append(i * 3)
   print(result)  # [60, 45, 33]
   ```

9. 用zip組合鍵和值來創建字典。

   **好**的代碼：

   ```Python
   keys = ['1001', '1002', '1003']
   values = ['駱昊', '王大錘', '白元芳']
   d = dict(zip(keys, values))
   print(d)
   ```

   **不好**的代碼：

   ```Python
   keys = ['1001', '1002', '1003']
   values = ['駱昊', '王大錘', '白元芳']
   d = {}
   for i, key in enumerate(keys):
       d[key] = values[i]
   print(d)
   ```

> **說明**：這篇文章的內容來自於網絡，有興趣的讀者可以閱讀[原文](http://safehammad.com/downloads/python-idioms-2014-01-16.pdf)。

