import unittest
from tabero.twapi import Search

class TestTwApi(unittest.TestCase):
    def setUp(self):
        self.testSearch = Search('#pebble', 1)

    def test_GetSearchText(self):
        self.assertEqual('a', self.testSearch.rawResult[0])

if __name__ == '__main__':
        unittest.main()
