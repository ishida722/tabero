import unittest
from tabero.tabero import Tabero
import tests.data

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

    def test_TweetsAnalys(self):
        responce = self.testTabero.yapi_lang(tests.data.tweets_onlyFood)
        nounList = list(self.testTabero.Nouns(responce))
        self.assertEqual(['トンカツ', 'おはぎ' ,'トンカツ', '朝ごはん'], nounList)

    def test_IsAlpha(self):
        word = 'abc'
        result = self.testTabero.IsAlpha(word)
        self.assertTrue(result)


    # def test_TweetsAnalysQithNoise(self):
    #     self.testTabero.GenarateFoodList(tests.data.tweets_withNoise)
    #     self.assertEqual(['トンカツ', 'おはぎ' ,'トンカツ', '朝ごはん'], self.testTabero.foodList)




if __name__ == '__main__':
        unittest.main()
