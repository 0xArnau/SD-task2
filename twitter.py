import tweepy
from config.config import config

auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])

api = tweepy.API(auth)

#Initialize a dictionary where we will save all the tweets in order to avoid repeated
tweet_dict = {}



#search tweets with a specific gelocation, language an words
def search_tweets(count):

    for i in range(count):
        tweet = api.search(q="Covid,coronavirus", geocode="41.8204600,1.8676800,300km", lang="es", count=100, result_type="recent", tweet_mode="extended", include_entities="false")

        for tw in tweet:
            id = tw.id
            status = api.get_status(id, tweet_mode = "extended")
            try:
                #print(status.retweeted_status.full_text)
                if id not in tweet_dict.keys():
                    tweet_dict[id] = status.retweeted_status.full_text
                
            except AttributeError:  # Not a Retweet
                #print(status.full_text)
                if id not in tweet_dict.keys():
                    tweet_dict[id] = status.full_text

    print(tweet_dict)


search_tweets(1)
            
