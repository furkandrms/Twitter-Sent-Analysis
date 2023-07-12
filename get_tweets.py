import sys
import csv
import tweepy
from sentiment_analysis import *

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_key = "YOUR_ACCESS_KEY"
access_secret = "YOUR_ACCESS_SECRET"

# Method to get a user's last tweets
def get_tweets(username, asData=True):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Set the number of tweets you want to retrieve
    number_of_tweets = 10

    tweets_for_csv = []
    try:
        # Retrieve tweets
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=username).items(number_of_tweets):
            tweets_for_csv.append(tweet.text)
    except tweepy.TweepError:
        print("Error: unable to get tweets for " + username)

    if asData:
        print(type(tweets_for_csv))
        return ""

    outfile = username + "_tweets.csv"

    with open(outfile, 'w+', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Tweet", "Score", "Status"])

        # Process and write tweets to the CSV file
        for tweet in tweets_for_csv:
            a = get_sentiment(tweet)
            b = (a.split(" ")[1])
            c = (a.split(" ")[2])
            writer.writerow([tweet, c, b])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print("Error: enter one username")
