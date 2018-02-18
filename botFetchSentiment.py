import config
from keys import REDDIT_CONFIG, TWEEPY_CONFIG
import tweepy
import praw


class BotFetchSentiment():
    def __init__(self, word):

        self.reddit = praw.Reddit(
            client_id=REDDIT_CONFIG['client_id'],
            client_secret=REDDIT_CONFIG['client_secret'],
            password=REDDIT_CONFIG['password'],
            user_agent=REDDIT_CONFIG['user_agent'],
            username=REDDIT_CONFIG['username'])
        self.top_posts = self.reddit.subreddit(word).top()

        self.auth = tweepy.OAuthHandler(
            TWEEPY_CONFIG['consumer_key'],
            TWEEPY_CONFIG['consumer_secret'])
        self.auth.set_access_token(TWEEPY_CONFIG['access_token'],
                                   TWEEPY_CONFIG['access_token_secret'])
        self.api = tweepy.API(self.auth)
        self.public_tweets = self.api.search(word)
