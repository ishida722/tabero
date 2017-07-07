import tabero.secret as secret
import twitter
import json

class API:
    api = twitter.Api(
            consumer_key=secret.TWITTER_CONSUMER_KEY,
            consumer_secret=secret.TWITTER_CONSUMER_SECRET,
            access_token_key=secret.TWITTER_ACCESS_TOKEN,
            access_token_secret=secret.TWITTER_ACCESS_TOKEN_SECRET)

class Search(API):

    def __init__(self, query, count):
        self.rawResult = self.api.GetSearch(term=query, count=count, result_type='recent')
        self._i = 0

    def __iter__(self):
        return self

    def next(self):
        return self


    def GetSearchText(self, word):
        tweetList = []
        search = self.search(word)
        for status in search['statuses']:
            tweetList.append(status['text'])
        self.searchCount = len(search['statuses'])
        return tweetList
