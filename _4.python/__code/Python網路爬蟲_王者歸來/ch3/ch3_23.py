# ch3_23.py
from urllib import parse

url = 'https://docs.python.org/3/search.html?q=parse&check_keywords=yes&area=default'
urp = parse.urlsplit(url)
print(type(urp))
print(urp)
print('scheme   = ', urp.scheme)
print('netloc   = ', urp.netloc)
print('path     = ', urp.path)
print('query    = ', urp.query)
print('fragment = ', urp.fragment)








    












