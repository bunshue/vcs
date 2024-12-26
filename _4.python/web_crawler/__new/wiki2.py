import sys
import requests
import codecs

search_word = "椎名林檎"
api_url = "https://zh.wikipedia.org/w/api.php"
api_params = {
    "format": "xmlfm",
    "action": "query",
    "prop": "revisions",
    "rvprop": "content",
}
api_params["titles"] = search_word
wiki_data = requests.get(api_url, params=api_params)
# fo = codecs.open('C:\\Users\\Tristan\\Desktop\\'+ search_word + '.html', 'w', 'utf-8')
fo = codecs.open("wiki_page_" + search_word + ".html", "w", "utf-8")
fo.write(wiki_data.text)
fo.close()
