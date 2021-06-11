from sentiment_analysis_spanish import sentiment_analysis
import pandas

df = pandas.read_csv('data.csv')

sentiment = sentiment_analysis.SentimentAnalysisSpanish()
df['sentiment_analysis'] = df['text'].apply(lambda i: sentiment.sentiment(i))

df.to_csv('data_with_sentiment.csv')
