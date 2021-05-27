import tweepy
from config.config import config

auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])

api = tweepy.API(auth)


#All the information of the user
#user = api.get_user('arnauuau')
#geocode="41.8204600 1.8676800 300km"

tweet = api.search(q="Covid", geocode="41.8204600, 1.8676800, 300km", lang="es", count=100, tweet_mode="extended", include_entities="false")
for tw in tweet:
    id = tw.id
    status = api.get_status(id, tweet_mode = "extended")
    try:
        print(status.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        print(status.full_text)
