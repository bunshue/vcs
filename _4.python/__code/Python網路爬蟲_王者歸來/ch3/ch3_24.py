# ch3_24.py
from urllib import parse

scheme = 'https'
netloc  = 'docs.python.org'
path = '/3/search.html'
params = ''
query = 'q=parse&check_keywords=yes&area=default'
frament = ''
url_unparse = parse.urlunparse((scheme,netloc,path,params,query,frament))
print(url_unparse)
url_unsplit = parse.urlunsplit([scheme,netloc,path,query,frament])
print(url_unsplit)






    












