import unittest
from tabero.twapi import TwApi

class TestTwApi(unittest.TestCase):
    def setUp(self):
        self.tw = TwApi()

    # def test_search(self):
    #     search = self.tw.search('食べたい')
    #     k = list(search['statuses'].keys())
    #     print(search['statuses'][0]['text'])
    #     print(len(search['statuses']))
    #     for status in search['statuses']:
    #         print(status['text'])

    def test_GetSearchText(self):
        print(self.tw.GetSearchText('#pebble'))
        self.assertEqual(self.tw.searchCount, 100)

if __name__ == '__main__':
        unittest.main()
