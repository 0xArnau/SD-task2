import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas



def sentiment_analysis(df):
	sid = SentimentIntensityAnalyzer()
	df['sentiment_analysis'] = df['text'].apply(lambda i: sid.polarity_scores(i))
	return df

if __name__ == "__main__":
  print('Data Preprocessing')
  df = pandas.read_csv('data.csv')
  df = (sentiment_analysis(df))
  print(df)
  

