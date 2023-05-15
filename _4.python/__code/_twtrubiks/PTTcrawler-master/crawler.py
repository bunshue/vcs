import sys
import requests
import json
import urllib3
import logging
import re
import datetime

from bs4 import BeautifulSoup

urllib3.disable_warnings()
logging.basicConfig(level=logging.WARNING)
HTTP_ERROR_MSG = 'HTTP error {res.status_code} - {res.reason}'


class PttSpider:
    rs = requests.session()
    ptt_head = 'https://www.ptt.cc'
    ptt_middle = 'bbs'
    parser_page_count = 5

    def __init__(self, **kwargs):
        self._board = kwargs.get('board', None)
        self.parser_page = int(kwargs.get('parser_page', self.parser_page_count))

        self._soup = None
        self._index_seqs = None
        self._articles = []

    @property
    def info(self):
        return self._articles

    @property
    def board(self):
        return self._board.capitalize()

    def run(self):
        self._soup = self.check_board()
        self._index_seqs = self.parser_index()
        self._articles = self.parser_per_article_url()
        self.analyze_articles()
        self.crawler_data()

    def check_board(self):
        print('check board......')
        if self._board:
            return self.check_board_over18()
        else:
            print("請輸入看版名稱")
            sys.exit()

    def check_board_over18(self):
        load = {
            'from': '/{}/{}/index.html'.format(self.ptt_middle, self._board),
            'yes': 'yes'
        }
        try:
            res = self.rs.post('{}/ask/over18'.format(self.ptt_head), verify=False, data=load)
            res.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            logging.warning(HTTP_ERROR_MSG.format(res=exc.response))
            raise Exception('網頁有問題')
        return BeautifulSoup(res.text, 'html.parser')

    def parser_index(self):
        print('parser index......')
        max_page = self.get_max_page(self._soup.select('.btn.wide')[1]['href'])
        return (
            '{}/{}/{}/index{}.html'.format(self.ptt_head, self.ptt_middle, self._board, page)
            for page in range(max_page - self.parser_page + 1, max_page + 1, 1)
        )

    def parser_per_article_url(self):
        print('parser per article url......')
        articles = []
        for page in self._index_seqs:
            try:
                res = self.rs.get(page, verify=False)
                res.raise_for_status()
            except requests.exceptions.HTTPError as exc:
                logging.warning(HTTP_ERROR_MSG.format(res=exc.response))
            except requests.exceptions.ConnectionError:
                logging.error('Connection error')
            else:
                articles += self.crawler_info(res)
        return articles

    def analyze_articles(self):
        for article in self._articles:
            try:
                logging.debug('{}{} ing......'.format(self.ptt_head, article.url))
                res = self.rs.get('{}{}'.format(self.ptt_head, article.url), verify=False)
                res.raise_for_status()
            except requests.exceptions.HTTPError as exc:
                logging.warning(HTTP_ERROR_MSG.format(res=exc.response))
            except requests.exceptions.ConnectionError:
                logging.error('Connection error')
            else:
                article.res = res

    @staticmethod
    def check_format(soup, class_tag, index):
        # 避免有些文章會被使用者自行刪除 標題列 時間  之類......
        content = None
        try:
            content = soup.select(class_tag)[index].text
        except Exception as e:
            # print('checkformat error URL', link)
            logging.warning(e)
        return content

    @staticmethod
    def crawler_content(soup, time):
        main_content = None
        try:
            content = soup.find(id="main-content").text
            target_content = '※ 發信站: 批踢踢實業坊(ptt.cc),'
            content = content.split(target_content)
            content = content[0].split(time)
            main_content = content[1].replace('\n', '  ').strip()
        except Exception as e:
            logging.warning(e)
        return main_content

    @staticmethod
    def crawler_ip(soup):
        ip = None
        try:
            target_split = '※ 發信站: 批踢踢實業坊'
            ip = soup.find(string=re.compile(target_split))
            ip = re.search(r"[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*", ip).group()
        except Exception as e:
            logging.warning(e)
        return ip

    @staticmethod
    def crawler_push_data(soup):
        # message 推文內容
        num, g, b, n, message = 0, 0, 0, 0, dict()

        for tag in soup.select('div.push'):
            try:
                # push_tag  推文標籤  推  噓  註解(→)
                push_tag = tag.find("span", {'class': 'push-tag'}).text.strip()

                # push_userid 推文使用者id
                push_userid = tag.find("span", {'class': 'push-userid'}).text

                # push_content 推文內容
                push_content = tag.find("span", {'class': 'push-content'}).text.strip()
                push_content = push_content[1:].strip()

                # push-ipdatetime 推文時間
                push_ipdatetime = tag.find("span", {'class': 'push-ipdatetime'}).text
                push_ipdatetime = push_ipdatetime.strip()

                num += 1
                message[num] = {"狀態": push_tag,
                                "留言者": push_userid,
                                "留言內容": push_content,
                                "留言時間": push_ipdatetime}

                # 計算推噓文數量 g = 推 , b = 噓 , n = 註解
                if push_tag == '推':
                    g += 1
                elif push_tag == '噓':
                    b += 1
                else:
                    n += 1
            except Exception as e:
                logging.warning(e)

        message_num = {"g": g, "b": b, "n": n, "all": num}
        return message, message_num

    def crawler_data(self):
        for data in self._articles:
            print('crawler data......')
            soup = BeautifulSoup(data.res.text, 'html.parser')
            # 文章日期
            data.time = self.check_format(soup, '.article-meta-value', 3)
            if data.time:
                # 文章內文
                data.content = self.crawler_content(soup, data.time)
            # 文章ip
            data.ip = self.crawler_ip(soup)
            # 推文內容
            data.push_message, data.push_message_nums = self.crawler_push_data(soup)

    @staticmethod
    def crawler_info(res):
        logging.debug('crawler_info......{}'.format(res.url))
        soup = BeautifulSoup(res.text, 'html.parser')
        articles = []
        for r_ent in soup.find_all(class_="r-ent"):
            try:
                # 得到每篇文章的 url
                url = r_ent.find('a')['href']
                if not url:
                    continue
                # 文章標題
                title = r_ent.find(class_="title").text.strip()
                # 文章作者
                author = r_ent.find(class_="author").text.strip()
                articles.append(ArticleInfo(
                    title=title, author=author, url=url))
            except Exception as e:
                logging.debug('本文已被刪除')
                logging.debug(e)
        return articles

    @staticmethod
    def get_max_page(content):
        start_index = content.find('index')
        end_index = content.find('.html')
        page_number = content[start_index + 5: end_index]
        return int(page_number) + 1


class ArticleInfo:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.author = kwargs.get('author', None)
        self.url = kwargs.get('url', None)
        self.time = kwargs.get('time', None)
        self.ip = None
        self.push_message = dict()
        self.push_message_nums = dict()
        self.content = None
        self.res = None

    @staticmethod
    def data_process(info, board):
        data = []
        for index, article in enumerate(info):
            data.append(
                {
                    "a_ID": index,
                    "b_作者": article.author,
                    "c_標題": article.title,
                    "d_日期": article.time,
                    "e_ip": article.ip,
                    "f_內文": article.content,
                    "g_推文": article.push_message,
                    "h_推文總數": article.push_message_nums
                }
            )
        json_data = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        file_name = 'data-{}-{}.json'.format(board, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(json_data)
