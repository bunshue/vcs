# ch3_25.py
from urllib import parse

url_python = 'https://docs.python.org/3/search.html?'
query = {
         'q':'parse',
         'check_keywords':'yes',
         'area':'default'}
url = url_python + parse.urlencode(query)
print(url)






    












