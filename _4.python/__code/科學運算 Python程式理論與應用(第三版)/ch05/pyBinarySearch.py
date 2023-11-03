# -*- coding:utf-8 -*-
# file: pyBinarySearch.py
#
def BinarySearch(l, key):						# 二分查詢
	low = 0
	high = len(l) - 1
	i = 0
	while (low <= high):
		i = i + 1
		mid = (high + low) // 2
		if (l[mid] < key):
			low = mid + 1
		elif (l[mid] > key):
			high = mid - 1
		else:
			print('use %d time(s)' % i)
			return mid
	return -1
if __name__ == '__main__':
	l = [1, 5, 6, 9, 10, 51, 62, 65, 70]				# 建構清單
	print(BinarySearch(l, 5))					# 在清單中查詢
	print(BinarySearch(l, 10))
	print(BinarySearch(l, 65))
	print(BinarySearch(l, 70))
