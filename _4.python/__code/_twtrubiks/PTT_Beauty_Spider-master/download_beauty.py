import datetime
import sys
from crawler import ArticleInfo, PttSpider, Download
from run_time import my_time


def process(article):
    datetime_format = '%Y%m%d%H%M%S'
    crawler_datetime = datetime.datetime.now()
    ptt_spider = PttSpider()
    ptt_spider.run_specific_article(article)
    crawler_time = '{}_PttImg_{:{}}'.format(ptt_spider.board, crawler_datetime, datetime_format)
    info = ArticleInfo.data_process(ptt_spider.info, crawler_time)
    download = Download(info)
    download.run()


@my_time
def main():
    # 從.txt檔案中讀取 urls
    with open(sys.argv[1]) as lines:
        for url in lines:
            if PttSpider.ptt_head in url.strip():
                url = url.split(PttSpider.ptt_head)[-1].replace('\n', '')
                process(ArticleInfo(url=url))
    print('下載完畢...')


if __name__ == '__main__':
    main()
