# 5-7-1 list - 麻煩的優先佇列

q = []
q.append((2, '寫程式'))
q.append((1, '吃飯'))
q.append((3, '睡覺'))

q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)