import tweepy
import praw
import config


class BotFetchSentiment():
    def __init__(self, word):

        self.reddit = praw.Reddit(
            client_id=config.REDDIT_CONFIG['client_id'],
            client_secret=config.REDDIT_CONFIG['client_secret'],
            password=config.REDDIT_CONFIG['password'],
            user_agent=config.REDDIT_CONFIG['user_agent'],
            username=config.REDDIT_CONFIG['username'])
        self.top_posts = self.reddit.subreddit(word).top()

        self.auth = tweepy.OAuthHandler(
            config.TWEEPY_CONFIG['consumer_key'],
            config.TWEEPY_CONFIG['consumer_secret'])
        self.auth.set_access_token(config.TWEEPY_CONFIG['access_token'],
                                   config.TWEEPY_CONFIG['access_token_secret'])
        self.api = tweepy.API(self.auth)
        self.public_tweets = self.api.search(word)
