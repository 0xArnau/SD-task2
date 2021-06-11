import tweepy
import pandas
from config.config import config

auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])

api = tweepy.API(auth)

#Initialize a dictionary where we will save all the tweets in order to avoid repeated
tweet_dict = {}
tweet_dict_data = {
    'date': [],
    'geo': [],
    'url': [],
    'sentiment_Analysis': [],       #sentiment analysis
}


def search_tweets(count):
    for i in range(count):
        tweet = api.search(q="Covid,coronavirus", geocode="41.8204600,1.8676800,300km", lang="es", count=5, result_type="recent", tweet_mode="extended", include_entities="false")
    
        for tw in tweet:
            id = tw.id
            status = api.get_status(id, tweet_mode = "extended")
            if id not in tweet_dict.keys():
                tweet_dict[id] = status
    #for x in tweet_dict:
    #    print(f'ID: {x} --> {tweet_dict[x]}')


#search tweets with a specific gelocation, language an words
def data_tweets():
    for IDtw in tweet_dict:
        status = tweet_dict[IDtw]
        try:
            if not status.retweeted_status.full_text == '':
                tweet_dict_data['date'].append(str(status.created_at))
                tweet_dict_data['geo'].append('ES')
                tweet_dict_data['url'].append('https://twitter.com/twitter/statuses/' + str(id))
                tweet_dict_data['sentiment_Analysis'].append(status.retweeted_status.full_text)
        except AttributeError:  # Not a Retweet
            if not status.full_text == '':
                tweet_dict_data['date'].append(str(status.created_at))
                tweet_dict_data['geo'].append('ES')
                tweet_dict_data['url'].append('https://twitter.com/twitter/statuses/' + str(id))
                tweet_dict_data['sentiment_Analysis'].append(status.full_text)

    return pandas.DataFrame(tweet_dict_data)

#Write csv
search_tweets(1)
df = data_tweets()
print(df)
df.to_csv('data.csv')
            
