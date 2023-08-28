#需安裝playsound:pip install playsound
import newspaper
from newspaper import Article
from google_trans_new import google_translator
import gtts
from playsound import playsound 

# paper = newspaper.build('http://cnn.com', language='en')
paper = newspaper.build('http://www.cnbc.com', language='en')
# paper = newspaper.build('http://www.bbc.co.uk', language='en')
# paper = newspaper.build('http://www.foxnews.com', language='en')
for article in paper.articles:
    url = article.url
    if '.html' in url:
        print(url)
        try:  #有時會產生無法擷取的錯誤,故使用try
            article = Article(url)
            article.download()
            article.parse()
            content = article.text
            if len(content)>0:
                if len(content)>5000: content = content[:4999]
                translator = google_translator()
                ret = translator.translate(content, lang_tgt='zh-TW')
                print(ret)
                tts = gtts.gTTS(text=ret, lang='zh-tw')
                tts.save('news.mp3')
                playsound('news.mp3')
        except:
            pass
