import ujson

dic = {"device":"temperature","id":543,"values":[1,2,3]}
json_str = ujson.dumps(dic)
print(json_str)
print(type(json_str))
