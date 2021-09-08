import math
import string
import numpy as np
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyse(text):
    pol = SentimentIntensityAnalyzer().polarity_scores(text)
    return max(zip(pol.values(), pol.keys()))[1]


def compare(star, sentiment):
    if (star <= 2 and sentiment == 'neg') or (star == 3 and sentiment == 'neu') or (star >= 4 and sentiment == 'pos'):
        return "Matched"
    else:
        return "Not Matched"


def fun(data):
    # fill the null value of the text data with "Not Available"
    data['Text'].fillna("Data not Available", inplace=True)
    # data = data['Star'].fillna(0,inplace = True)
    # find the sentiment of each text in the data set
    data['sent'] = data['Text'].apply(lambda x: analyse(x))

    # comapre the sentiment

    data['status'] = data.apply(lambda x: compare(x.Star, x.sent), axis=1)

    return data
