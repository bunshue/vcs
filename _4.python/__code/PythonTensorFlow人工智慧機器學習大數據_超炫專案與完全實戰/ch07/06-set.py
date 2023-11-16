A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
#print(A + B)
print(A & B)
print(A | B)
print(A.union(B))
print(A.intersection(B))

print(A)
A.discard(2)
print(A)
A.remove(4)
print(A)
A.add(4)
print(A)
A.update([2,3,4])
print(A)
