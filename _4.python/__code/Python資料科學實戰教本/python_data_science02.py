import requests

r = requests.get("http://www.google.com")
print(r.status_code)

print("------------------------------------------------------------")  # 60個

r = requests.get("http://www.google.com")
if r.status_code == 200:
    print("請求成功...")
else:
    print("請求失敗...")
     

print("------------------------------------------------------------")  # 60個

url_params = {'name': '陳會安', 'score': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
print(r.url)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-2-1c.py

from urlencode import urlencode 

url_params = {'name': '陳會安', 'score': 95}
print(urlencode(url_params))

print("------------------------------------------------------------")  # 60個

data = {'name': '陳會安', 'score': 95}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)

print("------------------------------------------------------------")  # 60個

post_data = {'name': '陳會安', 'score': 95}
r = requests.post("http://httpbin.org/post", data=post_data)
print(r.text)

print("------------------------------------------------------------")  # 60個

url = "https://www.googleapis.com/books/v1/volumes"

data = {'q': 'Python',
        'maxResults': 5, 
        'projection': 'lite'}
r = requests.get(url, params=data)
print(r.json())

print("------------------------------------------------------------")  # 60個

r = requests.get("https://fchart.github.io/test.html")
print(r.text)
print(r.encoding)

print("------------------------------------------------------------")  # 60個

r = requests.get("https://fchart.github.io/test.html")
print(r.text)
print("----------------------")

r = requests.get("https://fchart.github.io/test.html")
print(r.content)
print("----------------------")

r = requests.get("https://fchart.github.io/test.html", stream=True)
print(r.raw)
print(r.raw.read(15))

print("------------------------------------------------------------")  # 60個

r = requests.get("https://fchart.github.io/json/Example.json")
print(r.text)
print(type(r.text))
print("----------------------")
print(r.json())
print(type(r.json()))

print("------------------------------------------------------------")  # 60個

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.ok)

r = requests.get("http://www.google.com/404")
print(r.status_code)
print(r.status_code == requests.codes.ok)

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.all_good)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-3-3a.py

import requests

r = requests.get("http://www.google.com/404")
print(r.status_code)
print(r.status_code == requests.codes.ok)

print(r.raise_for_status())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-3-4.py

import requests 

r = requests.get("http://www.google.com")

print(r.headers['Content-Type'])
print(r.headers['Content-Length'])
print(r.headers['Date'])
print(r.headers['Server'])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-3-4a.py

import requests 

r = requests.get("http://www.google.com")

print(r.headers.get('Content-Type'))
print(r.headers.get('Content-Length'))
print(r.headers.get('Date'))
print(r.headers.get('Server'))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-4-1.py

import requests

url = "http://httpbin.org/cookies"

cookies = dict(name='Joe Chen')
r = requests.get(url, cookies=cookies)
print(r.text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-4-1a.py

import requests

session = requests.Session()
response = session.get("http://www.google.com")
v = session.cookies.get_dict()
print(v)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-4-2.py

import requests

url = "http://httpbin.org/user-agent"

r = requests.get(url)
print(r.text)
print("----------------------")

url_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
r = requests.get(url, headers=url_headers)
print(r.text)

print("------------------------------------------------------------")  # 60個





#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-4-3.py

import requests

url = "https://www.googleapis.com/books/v1/volumes"

url_params = {'q': 'Python',
              'maxResults': 3, 
              'projection': 'lite'}
r = requests.get(url, params=url_params)
print(r.json())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-4-4.py

import requests

try: 
    r = requests.get("http://www.google.com", timeout=0.03)
    print(r.text)
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-4-5.py

import requests 

url = 'http://www.google.com/404'

try:
    r = requests.get(url, timeout=3)
    r.raise_for_status()
except requests.exceptions.RequestException as ex1:
    print("Http請求錯誤: " + str(ex1))
except requests.exceptions.HTTPError as ex2:
    print("Http回應錯誤: " + str(ex2))
except requests.exceptions.ConnectionError as ex3:
    print("網路連線錯誤: " + str(ex3))
except requests.exceptions.Timeout as ex4:
    print("Timeout錯誤: " + str(ex4))     

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-5-2.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-5-2_edge.py

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-5-2a.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print("-----------------------------")
print(driver.title)
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-5-2a_edge.py

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print("-----------------------------")
print(driver.title)
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-5-2b.py

import requests   

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
cookies = { "over18": "1" }
r = requests.get(url, cookies=cookies, headers=headers)
print(r.text)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\ch3-5-2c.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch03\urlencode.py

# -*- coding: utf-8 -*-
#
# Extracted from: https://github.com/micropython/micropython-lib/blob/master/collections.defaultdict/collections/defaultdict.py
# Extracted from: https://github.com/micropython/micropython-lib/blob/master/urllib.parse/urllib/parse.py
#
# urencode.py
_safe_quoters = {}
_ALWAYS_SAFE = frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                         b'abcdefghijklmnopqrstuvwxyz'
                         b'0123456789'
                         b'_.-')
_ALWAYS_SAFE_BYTES = bytes(_ALWAYS_SAFE)

class defaultdict:

    @staticmethod
    def __new__(cls, default_factory=None, **kwargs):
        # Some code (e.g. urllib.urlparse) expects that basic defaultdict
        # functionality will be available to subclasses without them
        # calling __init__().
        self = super(defaultdict, cls).__new__(cls)
        self.d = {}
        return self

    def __init__(self, default_factory=None, **kwargs):
        self.d = kwargs
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return self.d[key]
        except KeyError:
            v = self.__missing__(key)
            self.d[key] = v
            return v

    def __setitem__(self, key, v):
        self.d[key] = v

    def __delitem__(self, key):
        del self.d[key]

    def __contains__(self, key):
        return key in self.d

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        return self.default_factory()
        
class Quoter(defaultdict):
    """A mapping from bytes (in range(0,256)) to strings.

    String values are percent-encoded byte values, unless the key < 128, and
    in the "safe" set (either the specified safe set, or default set).
    """
    # Keeps a cache internally, using defaultdict, for efficiency (lookups
    # of cached keys don't call Python code at all).
    def __init__(self, safe):
        """safe: bytes object."""
        self.safe = _ALWAYS_SAFE.union(safe)

    def __repr__(self):
        # Without this, will just display as a defaultdict
        return "<Quoter %r>" % dict(self)

    def __missing__(self, b):
        # Handle a cache miss. Store quoted string in cache and return.
        res = chr(b) if b in self.safe else '%{:02X}'.format(b)
        self[b] = res
        return res


def clear_cache():
    """Clear the quoters cache."""
    _safe_quoters.clear()


def quote(string, safe='/', encoding=None, errors=None):
    """quote('abc def') -> 'abc%20def'

    Each part of a URL, e.g. the path info, the query, etc., has a
    different set of reserved characters that must be quoted.

    RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
    the following reserved characters.

    reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
                  "$" | ","

    Each of these characters is reserved in some component of a URL,
    but not necessarily in all of them.

    By default, the quote function is intended for quoting the path
    section of a URL.  Thus, it will not encode '/'.  This character
    is reserved, but in typical usage the quote function is being
    called on a path where the existing slash characters are used as
    reserved characters.

    string and safe may be either str or bytes objects. encoding must
    not be specified if string is a str.

    The optional encoding and errors parameters specify how to deal with
    non-ASCII characters, as accepted by the str.encode method.
    By default, encoding='utf-8' (characters are encoded with UTF-8), and
    errors='strict' (unsupported characters raise a UnicodeEncodeError).
    """
    if isinstance(string, str):
        if not string:
            return string
        if encoding is None:
            encoding = 'utf-8'
        if errors is None:
            errors = 'strict'
        string = string.encode(encoding, errors)
    else:
        if encoding is not None:
            raise TypeError("quote() doesn't support 'encoding' for bytes")
        if errors is not None:
            raise TypeError("quote() doesn't support 'errors' for bytes")

    return quote_from_bytes(string, safe)


def quote_plus(string, safe='', encoding=None, errors=None):
    """Like quote(), but also replace ' ' with '+', as required for quoting
    HTML form values. Plus signs in the original string are escaped unless
    they are included in safe. It also does not have safe default to '/'.
    """
    # Check if ' ' in string, where string may either be a str or bytes.  If
    # there are no spaces, the regular quote will produce the right answer.
    if ((isinstance(string, str) and ' ' not in string) or
            (isinstance(string, bytes) and b' ' not in string)):
        return quote(string, safe, encoding, errors)

    if isinstance(safe, str):
        space = ' '
    else:
        space = b' '

    string = quote(string, safe + space, encoding, errors)
    return string.replace(' ', '+')


def quote_from_bytes(bs, safe='/'):
    """Like quote(), but accepts a bytes object rather than a str, and does
    not perform string-to-bytes encoding.  It always returns an ASCII string.
    quote_from_bytes(b'abc def\x3f') -> 'abc%20def%3f'
    """
    if not isinstance(bs, (bytes, bytearray)):
        raise TypeError("quote_from_bytes() expected bytes")

    if not bs:
        return ''

    if isinstance(safe, str):
        # Normalize 'safe' by converting to bytes and removing non-ASCII chars
        safe = safe.encode('ascii', 'ignore')
    else:
        safe = bytes([c for c in safe if c < 128])

    if not bs.rstrip(_ALWAYS_SAFE_BYTES + safe):
        return bs.decode()

    try:
        quoter = _safe_quoters[safe]
    except KeyError:
        _safe_quoters[safe] = quoter = Quoter(safe).__getitem__

    return ''.join([quoter(char) for char in bs])


def urlencode(query, doseq=False, safe='', encoding=None, errors=None):
    """Encode a dict or sequence of two-element tuples into a URL query string.

    If any values in the query arg are sequences and doseq is true, each
    sequence element is converted to a separate parameter.

    If the query arg is a sequence of two-element tuples, the order of the
    parameters in the output will match the order of parameters in the
    input.

    The components of a query arg may each be either a string or a bytes type.
    When a component is a string, the safe, encoding and error parameters are
    sent to the quote_plus function for encoding.
    """

    if hasattr(query, "items"):
        query = query.items()
    else:
        # It's a bother at times that strings and string-like objects are
        # sequences.
        try:
            # non-sequence items should not work with len()
            # non-empty strings will fail this
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
            # Zero-length sequences of all types will get here and succeed,
            # but that's a minor nit.  Since the original implementation
            # allowed empty dicts that type of behavior probably should be
            # preserved for consistency
        except TypeError:
            # ty, va, tb = sys.exc_info()
            raise TypeError("not a valid non-string sequence "
                            "or mapping object")  # .with_traceback(tb)

    l = []
    if not doseq:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
            else:
                v = quote_plus(str(v), safe, encoding, errors)

            l.append(k + '=' + v)
    else:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
                l.append(k + '=' + v)
            elif isinstance(v, str):
                v = quote_plus(v, safe, encoding, errors)
                l.append(k + '=' + v)
            else:
                try:
                    # Is this a sufficient test for sequence-ness?
                    _ = len(v)  # noqa
                except TypeError:
                    # not a sequence
                    v = quote_plus(str(v), safe, encoding, errors)
                    l.append(k + '=' + v)
                else:
                    # loop over the sequence
                    for elt in v:
                        if isinstance(elt, bytes):
                            elt = quote_plus(elt, safe)
                        else:
                            elt = quote_plus(str(elt), safe, encoding, errors)

                        l.append(k + '=' + elt)

    return '&'.join(l)

print("------------------------------------------------------------")  # 60個



