import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_1.py

# ch21_1.py
import numpy as np

A = np.matrix([[1, 2, 3], [4, 5, 6]])
B = np.matrix([[4, 5, 6], [7, 8, 9]])

print('A + B = {}'.format(A + B))
print('A - B = {}'.format(A - B))












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_2.py

# ch21_2.py
import numpy as np

A = np.matrix([[1, 2, 3], [4, 5, 6]])

print('2 * A   = {}'.format(2 * A))
print('0.5 * A = {}'.format(0.5 * A))












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_3.py

# ch21_3.py
import numpy as np

A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[5, 6], [7, 8]])
print('A * B = {}'.format(A * B))

C = np.matrix([[1, 0, 2], [-1, 3, 1]])
D = np.matrix([[3, 1], [2, 1], [1, 0]])
print('C @ D = {}'.format(C @ D))


 









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_4.py

# ch21_4.py
import numpy as np

A = np.matrix([[2, 3, 1], [3, 2, 5]])
B = np.matrix([[30, 50], [60, 80], [50, 60]])
print('A * B = {}'.format(A * B))


 









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_5.py

# ch21_5.py
import numpy as np

A = np.matrix([[1, 2, 1], [2, 1, 2]])
B = np.matrix([[30], [50], [20]])
print('A * B = {}'.format(A * B))


 









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_6.py

# ch21_6.py
import numpy as np

A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[5, 6], [7, 8]])
print('A * B = {}'.format(A * B))
print('B * A = {}'.format(B * A))


 









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_7.py

# ch21_7.py
import numpy as np

A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[1, 0], [0, 1]])
print('A * B = {}'.format(A * B))
print('B * A = {}'.format(B * A))


 









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_8.py

# ch21_8.py
import numpy as np

A = np.matrix([[2, 3], [5, 7]])
B = np.linalg.inv(A)
print('A_inv = {}'.format(B))
print('E     = {}'.format((A * B).astype(np.int64)))





 









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_9.py

# ch21_9.py
import numpy as np

A = np.matrix([[3, 2], [1, 2]])
A_inv = np.linalg.inv(A)
B = np.matrix([[5], [-1]])
print('{}'.format(A_inv * B))






 









print('------------------------------------------------------------')	#60個


#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_10.py

# ch21_10.py
import numpy as np

A = np.array([[[1, 2],
                [3, 4]],
               [[5, 6],
                [7, 8]],
               [[9, 10],
                [11, 12]]])

print('{}'.format(A))
print('shape = {}'.format(np.shape(A)))






 









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch21\ch21_11.py

# ch21_11.py
import numpy as np

A = np.array([[0, 2, 4, 6],
              [1, 3, 5, 7]])              
B = A.T
print('{}'.format(B))
C = np.transpose(A)
print('{}'.format(C))








 









print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

