import pandas as pd


def word_count(df: pd.DataFrame) -> dict:
    dict = {}
    df = df['text']
    for text in df:
        words = text.split()
        for word in words:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

    return dict


if __name__ == "__main__":
    print(word_count())
