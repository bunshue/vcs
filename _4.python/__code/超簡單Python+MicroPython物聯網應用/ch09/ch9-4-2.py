import ujson

json_str = """{"name":"John"}"""
parsed = ujson.loads(json_str)
print(parsed)
print(type(parsed))
