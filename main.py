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
    
    
    fexec = lithops.FunctionExecutor(config=config,runtime='arppi/sd-lithops-custom-runtime-39:0.3')
    #fexec = lithops.FunctionExecutor(config=config,runtime='arppi/sd-lithops-custom-runtime-38:0.4')
    
    cos = cosBackend(config)
    
    #Stage 1

    """
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
        cos.put_object(prefix=iterHashtag[i][0], name='', ext=iterHashtag[i][2], body=iterHashtag[i][3])
        i += 1
        print(tweet)
    
    
    #Stage 2
    
    tweets = [ [] ]
   
    keys = cos.list_keys(prefix='data')
    print(keys)

    i = 0
    for key in keys:
        object = cos.get_object(key)
        s = object.decode()
        for sin in s.splitlines()[1:]:
            if len(tweets[i]) == 1000:
                i += 1
                tweets.append([])

            tweets[i].append(sin.split(maxsplit=5)[1:])
    
    for tweet in tweets:
        dfObj = pd.DataFrame(tweet, columns = ['date' , 'time', 'geo', 'url', 'text'])
        df_sentiment = dp.sentiment_analysis(dfObj)
        cos.put_object(prefix='preprocess', name='', ext='csv', body=df_sentiment.to_string())
    """
    
    #Stage 3

    all_tweets = []
    process_keys = cos.list_keys(prefix='preprocess')
   
    for k in process_keys:
        data = cos.get_object(k)
        tw = data.decode()
        for idk in tw.splitlines()[1:]:
            all_tweets.append(idk.split(maxsplit=5))        #El camp de sentiment analysis es mostra junt amb el text
            #countwords amb diccionari per cada paraula
            #Fer el wordcloud
            #Generar plots amb diferentes dates i afegir a notebooks
            #Permetre buscar dades a partir de queries

        print(all_tweets)
            
    
        
        



