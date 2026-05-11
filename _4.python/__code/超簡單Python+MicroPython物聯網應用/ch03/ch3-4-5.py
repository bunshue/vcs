i = 1
while True:
    print(i, end=" ")
    i = i + 1
    if i > 5:
        break
print("\n----------------")
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i, end=" ")
    