from os.path import join, dirname
from dotenv import load_dotenv
from os import environ
import tweepy
from escpos.printer import Usb


def load_environment():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


class TwitterConsumer:

    def __init__(self):

        load_environment()

        auth = tweepy.OAuthHandler(environ.get("consumer_key"), environ.get("consumer_secret"))
        auth.set_access_token(environ.get("access_token"), environ.get("access_token_secret"))

        self.api = tweepy.API(auth)

    def get_tweets(self, user: str) -> tweepy.API.user_timeline:

        return self.api.list_timeline(owner_screen_name="BnMcG", slug="news")

class TweetLoader:

    def get(self, user: str):

        consumer = TwitterConsumer()
        tweets = consumer.get_tweets(user=user)

        latest_tweet = tweets[0]
        last_tweet = ""

        with open(join(dirname(__file__), "last.tweet"), "r") as last_in:
            last_tweet = last_in.read()
            print("LT: " + last_tweet)
        if last_tweet == latest_tweet.text:
            return None
        else:
            with open(join(dirname(__file__), "last.tweet"), "w") as out:
                out.write(latest_tweet.text)
            return latest_tweet.text


class TweetPrinter:

    def __init__(self):
        load_environment()
        printer = Usb(0x0416, 0x5011)

        tweets = TweetLoader()
        user = "bbcnews"
        tweet = tweets.get(user)

        if tweet is not None:
            printer.text("@bnmcg/news: " + tweet + "\n\n")
            # printer.cut()

TweetPrinter()
