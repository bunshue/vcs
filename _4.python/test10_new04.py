'''
import urllib.request

url = 'https://upload.wikimedia.org/wikipedia/commons/6/6d/Le_Serment_du_Jeu_de_paume.jpg'
filename = '網球場宣言.jpg'

print(url)
urllib.request.urlretrieve(url, filename = filename)
#需指明下載後的檔名, 否則不知道存到哪?
'''

import sys
bytes = sys.maxsize  # smallest total size so far
print(bytes)

print("Best:", end=' ', file=sys.stderr)


