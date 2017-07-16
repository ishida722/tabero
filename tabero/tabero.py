#coding:utf-8

import urllib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as etree
from tabero.twapi import Search
import tabero.secret as secret
import re
from collections import Counter

class FoodList:

    def yapi_lang(self, sentence):
        url = 'http://jlp.yahooapis.jp/MAService/V1/parse?'
        appid = secret.YAHOO_API_ID
        params = urllib.parse.urlencode(
                {'appid': appid,
                 'sentence':sentence,
                 'results':'ma',
                 'filter':9,
                 })
        response = urllib.request.urlopen(url + params)
        return response.read().decode('utf-8')

    def Nouns(self, xml):
        tree = etree.fromstring(xml)
        for e in tree.iter("{urn:yahoo:jp:jlp}surface"):
            yield e.text

    def IsAlpha(self, word):
        alphaReg = re.compile(r'^[a-zA-Z]+$')
        return alphaReg.match(word) is not None

    def Genarate(self, tweets):
        self.All = []
        for tweet in tweets:
            for noun in self.Nouns(self.yapi_lang(tweet)):
                if self.IsAlpha(noun) == True : continue
                if len(noun) == 1 : continue
                self.All.append(str(noun))
        self.sortAll = self.SortMost(self.All)
        self.most = self.sortAll[0][0]

    def SortMost(self, lst):
        counter = Counter(lst)
        return counter.most_common()

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i >= len(self.sortAll):
            raise StopIteration
        ret =  self.sortAll[self._i][0]
        self._i += 1
        return ret

def Tabetai():
    tw = Search('食べたい', 100)
    foodList = FoodList()
    foodList.Genarate(list(tw))
    return foodList
