import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


def sentiment_analysis(df: pd.DataFrame):
    sid = SentimentIntensityAnalyzer()
    df['sentiment_analysis'] = df['text'].apply(
        lambda i: sid.polarity_scores(i))
    return df


if __name__ == "__main__":
    print('Data Preprocessing')
    df = pd.read_csv('data.csv')
    df = (sentiment_analysis(df))
    print(df)
