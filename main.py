import math
import string
import numpy as np
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


data = pd.read_csv(r"C:\Users\ShauryaPC\Downloads\chrome_reviews.csv")
df= data.copy()
sentiment_dic = {"Text": [], "sentiment": []}


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']

    if neg > pos:
        print("Negetive Sentiment")
        sentiment_dic["Text"].append(sentiment_text)
        sentiment_dic["sentiment"].append("neg")
    elif pos > neg:
        print("Positive Sentiment")
        sentiment_dic["Text"].append(sentiment_text)
        sentiment_dic["sentiment"].append("pos")
    else:
        print("neutral")
        sentiment_dic["Text"].append(sentiment_text)
        sentiment_dic["sentiment"].append("neu")
    print(score)
# sentiment_analyse(clean_text)

def isNaN(num):
    return num != num

for i,j in enumerate(df["Text"]):
    if isNaN(df["Text"][i])==True:
        sentiment_dic["Text"].append("Not Available")
        sentiment_dic["sentiment"].append("NAN")
    else:
        text_lower = df["Text"][i].lower()
        clean_text = text_lower.translate(str.maketrans("","",string.punctuation))
    #     print(clean_text)
        tokenised_words = word_tokenize(clean_text,"english")
        sentiment_analyse(clean_text)


sentiment_df=pd.DataFrame(sentiment_dic)
sentiment_df.drop("Text",axis=1,inplace=True)
rating_to_sent = {"rating_sent": []}


def converting_star(value):
    for i in value:
        if i <= 2:

            rating_to_sent["rating_sent"].append("neg")
        elif i == 3:

            rating_to_sent["rating_sent"].append("neu")
        else:

            rating_to_sent["rating_sent"].append("pos")

converting_star(df["Star"])
rating_df= pd.DataFrame(rating_to_sent)

df = data.copy()
df=pd.concat([df,sentiment_df,rating_df],join="outer",axis=1)

results ={"matches":[]}
for i in range(0,df.shape[0]):
    if df["sentiment"][i]==df["rating_sent"][i]:
        results["matches"].append("MATCHED")
    else:
        results["matches"].append("NOT MATCHED")

df=pd.concat([df,pd.DataFrame(results)],join="outer",axis=1)
print(df[df["matches"]=="NOT MATCHED"])