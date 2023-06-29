import urllib, re

from zhtools.langconv import Converter

def cn_tw(word):
    word = Converter('zh-hant').convert(word)
    return word

def do_google_translate(target):
    # 確認查詢目標
    target_search = re.sub(' ', '+', target)

    # 設定查詢條件
    url = f'https://www.google.com/search?q={target_search}+%E4%B8%AD%E6%96%87'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
    print(url)

    # 開始查詢
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req).read()
    page_utf = str(page, 'utf-8')

    # 用來搜尋詞性、中文解釋、英文解釋的關鍵 pattern
    title_pattern = '<pre class="tw-data-text tw-text-large XcVN5d tw-ta" data-placeholder="Enter text" id="tw-source-text" style="text-align:left;display:none"><span>(\S*?)</span></pre>'
    pos_pattern = '<div class="tw-bilingual-pos">(\S*?)</div>'
    trans_pattern = '<span class="hrcAhc" lang="zh-CN">(\S*?)</span>'
    eng_pattern = '<div class="MaH2Hf" lang="en">(.*?)</div>'
    
    title = cn_tw(re.search(title_pattern, page_utf).group(1))

    reply_data = []
    # 搜尋詞性
    for match in re.finditer(pos_pattern, page_utf):
        print(match.start(1), match.group(1))
        reply_data.append([match.start(1), cn_tw(match.group(1)), 'pos'])

    # 搜尋中文解釋
    for match in re.finditer(trans_pattern, page_utf):
        print(match.start(1), match.group(1))
        reply_data.append([match.start(1), cn_tw(match.group(1)), 'trans'])

    # 搜尋英文解釋
    for match in re.finditer(eng_pattern, page_utf):
        print(match.start(1), match.group(1))
        reply_data.append([match.start(1), match.group(1), 'eng'])
        
    reply_data = sorted(reply_data)
    
    reply_dict = dict()
    
    for i in reply_data:
        if i[2] == 'pos':
            current_key = i[1]
            reply_dict[current_key] = [[], []]
        elif i[2] == 'trans':
            reply_dict[current_key][0].append(i[1])
        elif i[2] == 'eng':
            reply_dict[current_key][1].append(i[1])
    
    print(target, title, reply_dict)
    
    return target, title, reply_dict