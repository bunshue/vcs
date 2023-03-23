from urllib import parse

url = 'https://www.cnblogs.com/angelyan/'

result = parse.urlparse(url=url,scheme='http',allow_fragments=True)

print(result)
print(result.scheme)

