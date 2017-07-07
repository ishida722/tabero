#coding:utf-8

import sys
import csv
import random
import urllib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as etree
from tabero.twapi import Search
import collections
import tabero.secret as secret

class Tabero:
    def __init__(self):
        self.tw = Search('a', 10)

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

    def FetchFoodList(self):
        foodList = []
        for tweet in self.tw.GetSearchText('食べたい'):
            for food in self.ParsXml(self.yapi_lang(tweet)):
                foodList.append(str(food))
        return collections.Counter(foodList).most_common(1)[0][0]

    def GenarateFoodList(self, tweets):
        self.foodList = []
        for tweet in tweets:
            for noun in self.Nouns(self.yapi_lang(tweet)):
                if noun.isalpha() == True : continue
                if len(noun) == 1 : continue
                foodList.append(str(food))

    def Tabetai(self):
        self.GenarateFoodList(self.tw.GetSearchText('食べたい'))
        return self.foodList
