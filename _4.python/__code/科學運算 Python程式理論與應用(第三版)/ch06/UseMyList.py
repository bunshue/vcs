# -*- coding:utf-8 -*-
# file: UseMyList.py
# 
import MyList				# 匯入MyList模組
l = MyList.MyList(1,2,3,4,5)		# 呼叫MyList類別案例化產生l物件
l.show()				# 呼叫show方法
l + 10					# 此處將呼叫__add__方法
l.show()				# 呼叫show方法
l * 2					# 此處將呼叫__add__方法
l.show()				# 呼叫show方法
print(len(l))
l ** 3					# 此處將呼叫__add__方法
l.show()				# 呼叫show方法

