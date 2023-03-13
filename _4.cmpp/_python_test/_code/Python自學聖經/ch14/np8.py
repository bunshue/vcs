import numpy as np
np1 = np.array([1,2,3,4])	#使用list
np2 = np.array((5,6,7,8))	#使用tuple
print(np1)
print(np2)
print(type(np1), type(np2))


import numpy as np
na = np.array([1,2,3,4], dtype=int)
print(na)
na = np.array([1,2,3,4], dtype=float)
print(na)

import numpy as np
na = np.arange(0, 31, 2)
print(na)


import numpy as np
na = np.linspace(1, 15, 3)
print(na)

import numpy as np
a = np.zeros((5,))
print(a)

import numpy as np
b = np.ones((5,))
print(b)

import numpy as np
c = np.empty((5,))
print(c)

import numpy as np
listdata = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]]
na = np.array(listdata)
print(na)
print('維度', na.ndim)
print('形狀', na.shape)
print('數量', na.size)
