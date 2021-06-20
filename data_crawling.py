import tweepy
import pandas as pd


def search_tweets(api, count: int, queries: str):
    tweet_dict = {}
    tweet = api.search(q=queries, lang="en", count=count, result_type="recent",
                       tweet_mode="extended", include_entities="false")
    for tw in tweet:
        id = tw.id
        status = api.get_status(id, tweet_mode="extended")
        if id not in tweet_dict.keys():
            tweet_dict[id] = status
    return select_data(tweet_dict)


def select_data(tweet_dict: dict):
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
                tweet_dict_data['geo'].append(str(status.coordinates))
                tweet_dict_data['url'].append(
                    'https://twitter.com/twitter/statuses/' + str(IDtw))
                tweet_dict_data['text'].append(
                    status.retweeted_status.full_text)
        except AttributeError:  # Not a Retweet
            if not status.full_text == '':
                tweet_dict_data['date'].append(str(status.created_at))
                tweet_dict_data['geo'].append('ES:' + str(status.coordinates))
                tweet_dict_data['url'].append(
                    'https://twitter.com/twitter/statuses/' + str(IDtw))
                tweet_dict_data['text'].append(status.full_text)

    return (pd.DataFrame(tweet_dict_data))


if __name__ == "__main__":
    from config.config import config
    print('Data Crawling')
    auth = tweepy.OAuthHandler(
        config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
    auth.set_access_token(
        config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])

    api = tweepy.API(auth)

    print(search_tweets(api, 1, "Coronavirus"))
