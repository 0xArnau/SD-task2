import lithops
import tweepy
import data_crawling as dc
from config.config import config
import pandas as pd
import data_preprocessing as dp
from io import StringIO
import csv

from backend import cosBackend


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
    auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])
    api = tweepy.API(auth)
    
    fexec = lithops.FunctionExecutor(config=config,runtime='arppi/sd-lithops-custom-runtime-39:0.2')
    
    cos = cosBackend(config)

    '''
    fexec.call_async(dc.search_tweets,(api, 100,"coronavirus"))
    cos.put_object(prefix='data/coronavirus', name='', ext='csv', body=fexec.get_result().to_string())
    
    fexec.call_async(dc.search_tweets,(api, 100,"covid19"))
    cos.put_object(prefix='data/covid19', name='', ext='csv', body=fexec.get_result().to_string())

    fexec.call_async(dc.search_tweets,(api, 100,"covid-19"))
    cos.put_object(prefix='data/covid-19', name='', ext='csv', body=fexec.get_result().to_string())

    fexec.call_async(dc.search_tweets,(api, 100,"SARS-CoV-2"))
    cos.put_object(prefix='data/SARS-CoV-2', name='', ext='csv', body=fexec.get_result().to_string())
    '''

    key = 'data/coronavirus/0002.csv'
    print(key)
    objects = cos.get_object(key)
    s = objects.decode()
    for sin in s.splitlines()[1:]:
        print(sin.split(maxsplit=5)[5])
    
    

        
            
    
        
        



