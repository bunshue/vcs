import numpy as np
na = np.arange(1, 17).reshape(4, 4)
print(na[2, 3])			#12
print(na[1, 1:3])		#[6,7]
print(na[1:3, 2])		#[7,11]
print(na[1:3, 1:3])		#[[6,7],[7,11]]
print(na[::2, ::2])		#[[1,3],[9,11]]
print(na[:, 2])			#[3,7,11,15]
print(na[1, :])			#[5,6,7,8]
print(na[:, :])			#矩陣全部