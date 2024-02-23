import json
jsonStr='''
{"編號":"E01","姓名": "王小明",
"性別": true, "電話":["0912345678","0978123321"]}
'''
print("jsonStr字串：", jsonStr)
print("jsonStr型別：", type(jsonStr))
print()
pObj=json.loads(jsonStr)
print("pObj物件：", pObj)
print("pObj型別：", type(pObj))
for key in pObj:
    print(key,":", pObj[key],' value的型別：',type(pObj[key]))
