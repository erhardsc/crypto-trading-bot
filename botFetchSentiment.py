from auth import Auth


class BotFetchSentiment():
    def __init__(self, word):

        self.reddit = Auth.reddit()
        self.top_posts = self.reddit.subreddit(word).top()

        self.twitter = Auth.twitter()
        self.public_tweets = self.twitter.search(word)
