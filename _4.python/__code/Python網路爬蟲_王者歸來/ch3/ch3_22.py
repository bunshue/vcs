# ch3_22.py
from urllib import parse

url = 'https://docs.python.org/3/search.html?q=parse&check_keywords=yes&area=default'
urp = parse.urlparse(url)
print(type(urp))
print(urp)
print('scheme   = ', urp.scheme)
print('netloc   = ', urp.netloc)
print('path     = ', urp.path)
print('params   = ', urp.params)
print('query    = ', urp.query)
print('fragment = ', urp.fragment)








    












