import unittest
from tabero import tabero
import tests.data

class TestTabero(unittest.TestCase):
    def setUp(self):
        self.testFoodList = tabero.FoodList()

    def tearDown(self):
        pass

    def test_YahooApiResponseIsNotError(self):
        sentence = '庭には二羽ニワトリがいる。'
        responce = self.testFoodList.yapi_lang(sentence)
        self.assertFalse(responce in '<Error>')

    def test_YahooApiResponseParseFromXml(self):
        sentence = '庭には二羽ニワトリがいる。'
        responce = self.testFoodList.yapi_lang(sentence)
        nounList = list(self.testFoodList.Nouns(responce))
        self.assertEqual(['庭', '二羽' ,'ニワトリ'], nounList)

    def test_TweetsAnalys(self):
        responce = self.testFoodList.yapi_lang(tests.data.tweets_onlyFood)
        nounList = list(self.testFoodList.Nouns(responce))
        self.assertEqual(['トンカツ', 'おはぎ' ,'トンカツ', '朝ごはん'], nounList)

    def test_IsAlpha(self):
        word = 'abc'
        result = self.testFoodList.IsAlpha(word)
        self.assertTrue(result)

    def test_IsNotAlpha(self):
        word = 'あいう'
        result = self.testFoodList.IsAlpha(word)
        self.assertFalse(result)

    def test_IsNotAlpha2(self):
        word = 'abcあいう'
        result = self.testFoodList.IsAlpha(word)
        self.assertFalse(result)

    def test_TweetsAnalysQithNoise(self):
        self.testFoodList.Genarate(tests.data.tweets_withNoise)
        foodList = self.testFoodList.All
        self.assertEqual(['トンカツ', 'おはぎ' ,'トンカツ', '朝ごはん'], foodList)
        self.assertEqual('トンカツ', self.testFoodList.most)

    # def test_Tabetai(self):
    #     tabero.Tabetai()

if __name__ == '__main__':
        unittest.main()
