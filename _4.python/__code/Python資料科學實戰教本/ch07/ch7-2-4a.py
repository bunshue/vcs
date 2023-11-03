import numpy as np 

a = np.array([[1, 2], [3, 4], [5, 6]])
for ele in a:
    print(ele)
print("---------------------------")
for ele in a:
    for item in ele:
        print(str(item) + " ", end="")