import requests
import codecs

api_base_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
wiki_data = requests.get(api_base_url, params = api_params)
fo = codecs.open('wiki搜尋結果1.html', 'w', 'utf-8')
#fo = open('wiki搜尋結果222.html', 'w')
fo.write(wiki_data.text)
fo.close()


import requests
import codecs

search_word = 'lion'

api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
wiki_data = requests.get(api_url, params = api_params)
fo = codecs.open('wiki搜尋結果2' + search_word + '.html', 'w', 'utf-8')
#fo = open('bbbbb'+ search_word + '.html', 'w')
fo.write(wiki_data.text)
fo.close()


