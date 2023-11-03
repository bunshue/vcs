# -*- coding:utf-8 -*-
# file: prime.py
#
import math
# isprime函數判斷一個整數是否為質數。
# 若果i能被2到i的平方根內的任意一個數整除，
# 則i不是質數，傳回0，否則i是質數，傳回1。
def isprime(i):
	for t in range( 2, int(math.sqrt(i)) + 1 ):
		if i % t == 0:			
			return 0	
		else:
			return 1
print('100~110之間的質數有:')
for i in range(100,110):
	if isprime(i):
		print(i)
