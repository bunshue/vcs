import random
import urllib
import re
import datetime

def prepare_record(text):
    text_list = text.split('\n')
    
    month = text_list[0].split(' ')[0].split('/')[0]
    day = text_list[0].split(' ')[0].split('/')[1]
    year = text_list[0].split(' ')[0].split('/')[2]
    d = datetime.date(int(year), int(month), int(day))
   
    record_list = []
    
    time_format = '%H:%M'
    
    for i in text_list[1:]:
        items = i.split(' ')
        
        name = items[0]
        training = items[1]
        
        start = datetime.datetime.strptime(items[2].split('-')[0], time_format)
        end = datetime.datetime.strptime(items[2].split('-')[1], time_format)
        duration = end - start
        
        record = (name, training, duration, d)
        record_list.append(record)
        
    return record_list


def image_search(engine, target):
    target = urllib.parse.quote(target)
    pattern_dict = {'Google': [f'https://www.google.com/search?q={target}&tbm=isch', 
                               '\["(https://[^?]*?)",\d*,\d*\]', 
                               '',
                               ''], 
                    'iStock': [f'https://www.istockphoto.com/photos/{target}?phrase={target}&sort=mostpopular', 
                               'src="(https://media.*?)"', 
                               'amp;', 
                               '']
                   }

    url = pattern_dict[engine][0]
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}

    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req).read()

    pattern = pattern_dict[engine][1]
    sub_str = pattern_dict[engine][2]
    repl_str = pattern_dict[engine][3]
    img_list = []
    
    for match in re.finditer(pattern, str(page, 'utf-8')):
        print(match.group(1))
        if sub_str:
            img_list.append(re.sub(sub_str, repl_str, match.group(1)))
        else:
            img_list.append(match.group(1))

    print(len(img_list))
    random_img_list = random.sample(img_list, k=5)

    return img_list[random.randint(0, len(img_list) - 1)], random_img_list