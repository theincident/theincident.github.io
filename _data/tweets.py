import tweepy
import yaml

# Load Twitter API credentials from YAML file
with open("_config.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
consumer_key = config["twitter"]["consumer_key"]
consumer_secret = config["twitter"]["consumer_secret"]
access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token_secret"]

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the last 5 tweets from the user's timeline
tweets = api.user_timeline(count=5)

# Convert tweet data to a YAML file
tweet_data = []
for tweet in tweets:
    tweet_data.append({"text": tweet.text, "created_at": tweet.created_at})
with open("_data/tweets.yml", "w") as f:
    yaml.dump(tweet_data, f)
