import unittest
from tabero.twapi import Search

class TestTwApi(unittest.TestCase):
    def setUp(self):
        self.testSearch = Search('#pebble', 10)

    def test_GetSearchText(self):
        print(self.testSearch.rawResult)

if __name__ == '__main__':
        unittest.main()
