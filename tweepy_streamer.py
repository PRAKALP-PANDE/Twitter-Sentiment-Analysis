import tweepy
from textblob import TextBlob
import twitter_credentials

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define the search query and collect tweets
search_query = 'ai'
tweet_count = 10
tweets = tweepy.Cursor(api.search_tweets, q=search_query).items(tweet_count)

# Perform sentiment analysis
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        print("Positive tweet:", tweet.text)
    elif sentiment < 0:
        print("Negative tweet:", tweet.text)
    else:
        print("Neutral tweet:", tweet.text)
