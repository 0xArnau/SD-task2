import lithops
import tweepy
import data_crawling as dc
#import data_preprocessing as dp
from config.config import config

from backend import cosBackend



if __name__ == '__main__':
    auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
    auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])
    api = tweepy.API(auth)
    
    fexec = lithops.FunctionExecutor(config=config,runtime='arppi/sd-lithops-custom-runtime-38:0.3')
    
    cos = cosBackend(config)

    fexec.call_async(dc.search_tweets,(api, 100,"coronavirus"))
    cos.put_object(prefix='data', name='coronavirus:', ext='csv', body=fexec.get_result().to_string())

    fexec.call_async(dc.search_tweets,(api, 100,"covid19"))
    cos.put_object(prefix='data', name='covid19:', ext='csv', body=fexec.get_result().to_string())

    fexec.call_async(dc.search_tweets,(api, 100,"covid-19"))
    cos.put_object(prefix='data', name='covid-19:', ext='csv', body=fexec.get_result().to_string())

    fexec.call_async(dc.search_tweets,(api, 100,"SARS-CoV-2"))
    cos.put_object(prefix='data', name='SARS-CoV-2:', ext='csv', body=fexec.get_result().to_string())
