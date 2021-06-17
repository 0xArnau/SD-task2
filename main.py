import lithops
import tweepy
import data_crawling as dc
from config.config import config
import pandas as pd
import data_preprocessing as dp
import time

from backend import cosBackend


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
    auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])
    api = tweepy.API(auth)
    
    fexec = lithops.FunctionExecutor(config=config,runtime='arppi/sd-lithops-custom-runtime-39:0.2')
    cos = cosBackend(config)

    iterdata = [(api, 100,"coronavirus"), (api, 100,"covid19"), (api, 100,"covid-19"), (api, 100,"SARS-CoV-2")]
    
    fexec.map(dc.search_tweets, iterdata)
    result = (fexec.get_result())
    
    iterHashtag = [
                    ('data/coronavirus','','csv',result[0].to_string())
                    ,('data/covid19','','csv',result[1].to_string())
                    ,('data/covid-19','','csv',result[2].to_string()) 
                    ,('data/SARS-CoV-2','','csv',result[3].to_string())
    ]
    
    i = 0
    for tweet in result:
        print(f"\n{iterHashtag[i][0]}\n")
        print("Put Object")
        cos.put_object(prefix=iterHashtag[i][0], name='', ext=iterHashtag[i][2], body=iterHashtag[i][3])
        i += 1
        print(tweet)
    
        
    '''
    key = 'data/coronavirus/0002.csv'
    print(key)
    objects = cos.get_object(key)
    s = objects.decode()
    for sin in s.splitlines()[1:]:
        print(sin.split(maxsplit=5))
        '''
    
    

        
            
    
        
        



