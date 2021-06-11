import tweepy
import pandas
from config.config import config


#
# Executar-ho cops al dia per crear arxius csv, juntar-ho en un i penjar-ho al clud
#


auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])

api = tweepy.API(auth)

#Initialize a dictionary where we will save all the tweets in order to avoid repeated
def search_tweets(count):
    tweet_dict = {}
    for _ in range(count):
        tweet = api.search(q="Covid,coronavirus", geocode="41.8204600,1.8676800,300km", lang="es", count=5, result_type="recent", tweet_mode="extended", include_entities="false")
        for tw in tweet:
            id = tw.id
            status = api.get_status(id, tweet_mode = "extended")
            if id not in tweet_dict.keys():
                tweet_dict[id] = status
    return tweet_dict


#search tweets with a specific gelocation, language an words
def data_tweets(tweet_dict: dict):
    tweet_dict_data = {
    'date': [],
    'geo': [],
    'url': [],
    'text': []       
    }
    for IDtw in tweet_dict:
        status = tweet_dict[IDtw]
        try:
            if not status.retweeted_status.full_text == '':
                tweet_dict_data['date'].append(str(status.created_at))
                tweet_dict_data['geo'].append('ES:' + str(status.coordinates))
                tweet_dict_data['url'].append('https://twitter.com/twitter/statuses/' + str(IDtw))
                tweet_dict_data['text'].append(status.retweeted_status.full_text)
        except AttributeError:  # Not a Retweet
            if not status.full_text == '':
                tweet_dict_data['date'].append(str(status.created_at))
                tweet_dict_data['geo'].append('ES:' + str(status.coordinates))
                tweet_dict_data['url'].append('https://twitter.com/twitter/statuses/' + str(IDtw))
                tweet_dict_data['text'].append(status.full_text)

    return pandas.DataFrame(tweet_dict_data)

#Write csv
df = data_tweets(search_tweets(1))
df.to_csv('data.csv')
            
