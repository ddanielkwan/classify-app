import pandas as pd
import nltk #natural language 
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score
from utils import get_polly_client
from pygame import mixer
import os
#polarity : 0 negative, 2 neutral, 4 positive
df = pd.read_csv("datasets/twitterSentimentdata.csv")
df = df[["Polarity", "Text"]]
print(df.columns)
#https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html
global vectorizer
#term frequency x inverse document frequenct
vectorizer = TfidfVectorizer(input = df['Text'].to_list(), lowercase = True, stop_words = 'english')
tfidf = vectorizer.fit_transform(df['Text']) #gives tf idf vector 

print(tfidf)
print(type(list(tfidf)))

kmeans = KMeans(n_clusters=2).fit(tfidf)
print(kmeans)

labels = kmeans.predict(vectorizer.transform(df['Text']))

clusters = {}
n = 0
for item in labels:
    print(item, end= " ")
    print(list(df['Text'])[n])
    n+=1
