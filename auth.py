from keys import REDDIT_CONFIG, TWEEPY_CONFIG
import tweepy
import praw


class Auth():
    def __init__(self):
        pass

    def reddit():
        reddit = praw.Reddit(
            client_id=REDDIT_CONFIG['client_id'],
            client_secret=REDDIT_CONFIG['client_secret'],
            password=REDDIT_CONFIG['password'],
            user_agent=REDDIT_CONFIG['user_agent'],
            username=REDDIT_CONFIG['username'])

        return reddit

    def twitter():
        auth = tweepy.OAuthHandler(
            TWEEPY_CONFIG['consumer_key'],
            TWEEPY_CONFIG['consumer_secret'])
        auth.set_access_token(TWEEPY_CONFIG['access_token'],
                                   TWEEPY_CONFIG['access_token_secret'])
        twitter = tweepy.API(auth)
        return twitter
