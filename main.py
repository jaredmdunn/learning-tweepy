import tweepy
import os

from dotenv import load_dotenv

load_dotenv()

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_SECRET_KEY"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# OAuth1 Authentication (application-user)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# OAuth2 Authentication (application-only)
# auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

# setting api
api = tweepy.API(auth)

# print ten tweets related to karen
# print("-- Karen search --")
# for tweet in tweepy.Cursor(api.search, q="karen").items(10):
#     print(tweet.text)

# Timeline tweets
# print("-- Timeline tweets --")
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name}: {tweet.text}")

# Attempt to follow Nat
# api.create_friendship("natdunn")

# Getting user
print("-- Nat ---")
nat = api.get_user("natdunn")
print(nat.name)
for follower in nat.followers():
    print(follower.name)
