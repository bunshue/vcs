print(__file__)
print(__file__.upper())
print(__file__.lower())
print(__name__)


print(__name__)
#print(__name__._version)



import sys
print(sys.path)







string_data1 = '你好'

print('原字串 :', string_data1)
print('用 gb2312 編碼 ')
encode_data = string_data1.encode('gb2312')
print(encode_data)

print('再用 big5 解碼出來')
string_data2 = encode_data.decode('big5')
print(string_data2)

print('萬國碼 unicode, 我')
print('我'.encode('utf8'))

string_data1 = '扂砑腕善衄壽unicode腔垀衄砆牉訧蹋,掀:unicode 2.0 3.0 4.0 梗摯崋欴晤鎢.gb,big-5,gbk,脹脹.坳蠅眳潔腔梗摯薊炵..秪峈扂猁勤森輛俴惆豢,眕扂植懂羶衄勤晤鎢衄徹旃噶,腕悝.褫岆婓厙奻梑祥善涴笱砆牉腔恅梒..洷咡籵徹蠟夔腕善.郅郅!'

print('原字串 :', string_data1)
print('用 big5 編碼 ')
encode_data = string_data1.encode('big5')
print(encode_data)

print('再用 gb2312 解碼出來')
string_data2 = encode_data.decode('gb2312')
print(string_data2)




#強制離開程式, 並說明原因
sys.exit('強制離開程式, 並說明原因')



