# ch10_26.py
X = frozenset([1, 3, 5])
Y = frozenset([5, 7, 9])
print(X)
print(Y)
print("交集  = ", X & Y)
print("聯集  = ", X | Y)
A = X & Y
print("交集A = ", A)
A = X.intersection(Y)
print("交集A = ", A)

