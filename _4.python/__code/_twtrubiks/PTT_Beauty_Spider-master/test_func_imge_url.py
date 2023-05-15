import unittest
from crawler import PttSpider


class TestCase(unittest.TestCase):

    def test_01(self):
        input_data = 'https://i.imgur.com/oqxkFn0.jpg'
        result = ['https://i.imgur.com/oqxkFn0.jpg']
        self.assertEqual(PttSpider.image_url(input_data), result)

    def test_02(self):
        input_data = 'https://i.imgur.com/oqxkFn0'
        result = ['https://i.imgur.com/oqxkFn0.jpg']
        self.assertEqual(PttSpider.image_url(input_data), result)

    def test_03(self):
        input_data = 'https://imgur.com/a/WKVB1Jc'
        result = []
        self.assertEqual(PttSpider.image_url(input_data), result)

    def test_04(self):
        input_data = 'http://imgur.com/GEQEdqy'
        result = ['http://imgur.com/GEQEdqy.jpg']
        self.assertEqual(PttSpider.image_url(input_data), result)

    def test_05(self):
        input_data = 'https://imgur.com/gallery/EuEjONQ'
        result = []
        self.assertEqual(PttSpider.image_url(input_data), result)

    def test_06(self):
        input_data = 'http://img.yaplog.jp/img/18/pc/l/p/-/lp-n-rena/1/1680_large.png'
        result = ['http://img.yaplog.jp/img/18/pc/l/p/-/lp-n-rena/1/1680_large.png']
        self.assertEqual(PttSpider.image_url(input_data), result)


if __name__ == '__main__':
    unittest.main()
