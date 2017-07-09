import unittest
from tabero.twapi import Search

class TestTwApi(unittest.TestCase):
    def setUp(self):
        self.testSearch = Search('食べたい', 10)

    def test_AssertSearchNumbers(self):
        self.assertEqual(10, len(self.testSearch))

    def test_ResultIsStrings(self):
        for tweet in self.testSearch:
            self.assertEqual(type('abc'), type(tweet))

if __name__ == '__main__':
        unittest.main()
