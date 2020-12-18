import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from secrets import consumer_key, consumer_secret
print("It is running\n")


api = tweepy.API(tweepy.AppAuthHandler(consumer_key, consumer_secret))
def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode = 'extended', lang= 'en').items(20):
        all_tweets.append(tweet.full_text)
    return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean

def get_sentiment(cleaned_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in cleaned_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def generate_avg_sentiment_score(keyword: str) -> int:
    
    return statistics.mean(get_sentiment(clean_tweets(get_tweets(keyword))))

#demo change
#print("Hello World folks")
if __name__ == "__main__":
    print("What does the world Prefer?")
    first_thing = input()
    print("...or....")
    second_thing = input()
    first_score = generate_avg_sentiment_score(first_thing)
    second_score = generate_avg_sentiment_score(second_thing)
    if first_score>second_score :
        print(f"{first_thing} wins over {second_thing} with a score of {first_score} against {second_score}")
    else:
        print(f"{second_thing} wins over {first_thing} with a score of {second_score} against {first_score}")