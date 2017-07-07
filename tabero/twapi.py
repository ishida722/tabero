import tabero.secret as secret
from twitter import *
import json

class TwApi:
    t = Twitter(
            auth=OAuth(secret.TWITTER_CONSUMER_KEY,
                       secret.TWITTER_CONSUMER_SECRET,
                       secret.TWITTER_ACCESS_TOKEN,
                       secret.TWITTER_ACCESS_TOKEN_SECRET))
    def __init__(self):
        pass

    def search(self, word):
        return self.t.search.tweets(q=word, count=10, resule_type='recent')

    def timeline(self):
        return self.t.statuses.home_timeline()

    def GetSearchText(self, word):
        tweetList = []
        search = self.search(word)
        for status in search['statuses']:
            # longstr = longstr + status['text']
            tweetList.append(status['text'])
        self.searchCount = len(search['statuses'])
        return tweetList
