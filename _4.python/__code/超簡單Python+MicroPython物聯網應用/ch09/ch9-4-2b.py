import ujson

json_str = """{"device":"temperature","id":543,"values":[1,2,3]}"""
parsed = ujson.loads(json_str)
print(parsed["device"])
print(parsed["id"])
print(parsed["values"])
print(type(parsed["values"]))
