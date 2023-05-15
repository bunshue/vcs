import datetime
import sys
from run_time import my_time
from crawler import PttSpider, Download, ArticleInfo


@my_time
def main():
    # python beauty_spider2.py [版名] [爬幾頁] [推文多少以上]
    # python beauty_spider2.py beauty 3 10
    board, page_term, push_rate = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    # board, page_term, push_rate = 'beauty', 5, 20  # for debugger
    print('start crawler ptt {}...'.format(board))
    crawler_datetime = datetime.datetime.now()
    spider = PttSpider(board=board,
                       parser_page=page_term,
                       push_rate=push_rate)
    spider.run()
    datetime_format = '%Y%m%d%H%M%S'
    crawler_time = '{}_PttImg_{:{}}'.format(spider.board, crawler_datetime, datetime_format)
    info = ArticleInfo.data_process(spider.info, crawler_time)
    download = Download(info)
    download.run()
    print("下載完畢...")


if __name__ == '__main__':
    main()
