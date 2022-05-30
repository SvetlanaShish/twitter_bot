import tweepy
import time


def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

consumer_API_key = input('Enter your Consumer API key')
consumer_API_secret_key = input('Enter your Consumer API secret key')
access_token = input('Enter your Access token')
access_token_secret = input('Enter your Access token secret')
usernamehere = input('Enter username for following')
auth = tweepy.OAuthHandler(consumer_API_key, consumer_API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) 
print (user.screen_name)
print (user.followers_count)

search = user.name
numberOfTweets = 1


for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == usernamehere:
    print(follower.name)
    follower.follow()


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break