A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("A = " + str(A))
print("B = " + str(B))
# 交集
C = A & B
print("A & B = " + str(C))
C = A.intersection(B)
print("A.intersection(B) = " + str(C))
# 聯集
C = A | B
print("A | B = " + str(C))
C = A.union(B)
print("A.union(B) = " + str(C))
# 差集
C = A - B
print("A - B = " + str(C))
C = A.difference(B)
print("A.difference(B) = " + str(C))
# 對稱差集
C = A ^ B
print("A ^ B = " + str(C))
C = A.symmetric_difference(B)
print("A.symmetric_difference(B) = " + str(C))