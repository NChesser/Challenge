
import tweepy

from twitter_access import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

"""
api = tweepy.API(auth)
#api.update_status('Updating this using Python')

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

telstra = api.get_user('Telstra')

print(telstra.screen_name)
print(telstra.followers_count)

for friend in telstra.followers():
    print(friend.screen_name)
"""
import json

class UserTweets(object):
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""
    def __init__(self, handle, max_id=0):
        self._api = tweepy.API(auth)
        self._handle = handle
        self._tweets = list(self.get_tweets())
        self.save_tweets()
    
    def get_tweets(self):
        # get users tweets
        tweets = [tweet for tweet in self._api.user_timeline(self._handle)]
        """tweet_content = {}

        for content in tweets:
            json_content = content._json
            print(json_content['text'])"""
        return tweets
    
    def save_tweets(self):
        # save tweets to csv
        pass

    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        return len(self._tweets)
    
    def __getitem__(self):
        pass


if __name__ == "__main__":
    
    handle = 'telstra'
    print('--- {} ---'.format(handle))
    user = UserTweets(handle)
    #user.get_tweets()
    print(user.__len__())