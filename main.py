import lithops
import tweepy
import data_crawling as dc
#import data_preprocessing as dp
from config.config import config



def my_function(x):
    return x + 7


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(config['tweepy']['API_KEY'], config['tweepy']['API_SECRET_KEY'])
    auth.set_access_token(config['tweepy']['ACCESS_TOKEN'], config['tweepy']['ACCESS_SECRET_TOKEN'])
    api = tweepy.API(auth)
    
    fexec = lithops.FunctionExecutor(config=config,runtime='arppi/sd-lithops-custom-runtime-38:0.3')
    
    data = (api, "corona")
    fexec.call_async(dc.search_tweets,data)
    #fexec.call_async(my_function, 3)
    print(fexec.get_result())


