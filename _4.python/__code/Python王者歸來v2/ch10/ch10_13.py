# ch10_13.py
# 賦值
numset = {1, 2, 3}
deep_numset = numset
deep_numset.add(10)
print("賦值   - 觀察numset        ", numset)
print("賦值   - 觀察deep_numset   ", deep_numset)

# 淺拷貝shallow copy
shallow_numset = numset.copy( )
shallow_numset.add(100)
print("淺拷貝 - 觀察numset        ", numset)
print("淺拷貝 - 觀察shallow_numset", shallow_numset)

