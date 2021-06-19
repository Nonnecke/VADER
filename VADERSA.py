import pandas as pd
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

with open('tweet_text.csv', "r", errors='ignore') as f:
    reader = csv.reader(f)
    your_list = list(reader)

analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(alist):
    for aSentence in alist: 
        aSnt = analyser.polarity_scores(aSentence[0])
        print(str(aSnt))

df_before = print_sentiment_scores(your_list)

print_sentiment_scores(your_list)


def print_sentiment_scores(alist):
    polarity_scores = []
    for aSentence in alist: 
        aSnt = analyser.polarity_scores(aSentence[0])
        print(str(aSnt))
        polarity_scores += [aSnt]

    return polarity_scores

output_df = pd.DataFrame(print_sentiment_scores(your_list))
output_df.to_csv('SATweets.csv')