import unittest
from tabero.tabero import Tabero

class TestTabero(unittest.TestCase):
    def setUp(self):
        self.testTabero = Tabero()

    def tearDown(self):
        pass

    def test_YahooApiResponseIsNotError(self):
        sentence = '庭には二羽ニワトリがいる。'
        responce = self.testTabero.yapi_lang(sentence)
        self.assertFalse(responce in '<Error>')

    def test_YahooApiResponseParseFromXml(self):
        sentence = '庭には二羽ニワトリがいる。'
        responce = self.testTabero.yapi_lang(sentence)
        nounList = list(self.testTabero.Nouns(responce))
        self.assertEqual(['庭', '二羽' ,'ニワトリ'], nounList)



if __name__ == '__main__':
        unittest.main()
