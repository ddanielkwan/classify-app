import pandas as pd
import nltk #natural language 
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score
from utils import get_polly_client
from pygame import mixer
import os
<<<<<<< HEAD
"""Program to preform exploratory data analysis on datasets/emails.csv data set."""
=======
"""Program to preform exploratory data analysis on emails.csv data set."""
>>>>>>> c790d8b0de90739e7041137d7ed6c9fda45e5c2b
global FILE
FILE = 'output.mp3'
def play_speech(text:str) -> None:
    """Uses AWS Polly to convert text to speech"""
    client = get_polly_client()
    speech_text = client.synthesize_speech(Text=f"You have entered: {text}",OutputFormat ='mp3',VoiceId = 'Joanna')

    with open(FILE, 'wb') as f:
        f.write(speech_text['AudioStream'].read())
        f.close()
    mixer.init()
    mixer.music.load(FILE)
    mixer.music.play()
    while mixer.music.get_busy(): 
        pass
    mixer.quit()
    os.remove(FILE)

#1 is spam, 0 is not spam
#read our data set into a pandas data frame
<<<<<<< HEAD
df = pd.read_csv("datasets/emails.csv")
=======
df = pd.read_csv("emails.csv")
>>>>>>> c790d8b0de90739e7041137d7ed6c9fda45e5c2b
print("Spam, Count")
print(df['spam'].value_counts())
print("-------") #we can clearly see that there is not an even amount of spam vs not spam, might be biased
#we can see that for every value in df['text'] that there is always either "Subject" or "re : "
#lets get rid of that
df['text'] = df['text'].str.replace("Subject:","")
df['text'] = df['text'].str.replace("re : ","")

#lets make word cloud to see spam vs not spam
def visualize(df: pd.DataFrame) -> None:
    """Visualization of text data"""
    #Lets first review spam and not spam data
    spam_data = df[df.spam == 1]
    not_spam_data = df[df.spam == 0]
    print(not_spam_data)
    print(spam_data)
    spam_emails = spam_data['text'].to_list()
    spam_emails = " ".join(spam_emails)
    not_spam_emails = not_spam_data['text'].to_list()
    not_spam_emails = " ".join(not_spam_emails)
    cloud_mask = np.array(Image.open("images\cloudmask.png"))
    spam_cloud = WordCloud(max_font_size = 150, mask=cloud_mask, background_color = "white", colormap="Reds").generate(spam_emails)
    not_spam_cloud = WordCloud(max_font_size = 150, mask=cloud_mask, background_color = "white").generate(not_spam_emails)

    plt.imshow(spam_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    plt.imshow(not_spam_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    # add some graphs here
    #bar
    values = ['not spam', 'spam']
    df['spam'].value_counts().plot(kind='bar')
    plt.xticks(df['spam'].unique(), values)
    plt.show()
#split our data set
x_train, x_test, y_train, y_test = train_test_split(df['text'], df['spam'], test_size = 0.3)

#set lemmatize
lemmatizer = nltk.WordNetLemmatizer() #my accuracy decreases when I change to lemma
x_train = [lemmatizer.lemmatize(word) for word in x_train] #sung -> sing
#feature extraction tf idf vectorize
global vectorizer
#term frequency x inverse document frequenct
vectorizer = TfidfVectorizer(input = x_train, lowercase = True, stop_words = 'english')
#shape of vectorizer is the shape on x_train 1000
tfidf_xtrain = vectorizer.fit_transform(x_train) #gives tf idf vector for x train
tfidf_xtest = vectorizer.transform(x_test) #gives tf idf for x trest # 300

# train the model using naive bayes
classifier = MultinomialNB() #model
classifier.fit(tfidf_xtrain, y_train)
actual = y_test.to_list()
print("classifier accuracy {:.2f}%".format(classifier.score(tfidf_xtest, y_test) * 100))
labels = classifier.predict(tfidf_xtest)
results = confusion_matrix(actual, labels)
#TP, FP
#FN, TN
print('Confusion Matrix :')
print(results)

#train the model using svm
global svm_model
svm_model = svm.SVC(C=1.0, kernel='linear', degree = 2, gamma='auto')
svm_model.fit(tfidf_xtrain, y_train)

predictions = svm_model.predict(tfidf_xtest)
# Use accuracy_score function to get the accuracy
print("SVM Accuracy Score -> ",accuracy_score(predictions, y_test)*100)
results2 = confusion_matrix(y_test.to_list(), predictions)
print(results2)

def get_input(text:str) -> int:
    # text =input("Enter email: ")
    play_speech(text) # can probably add "enter blah blah blah, this is classified as ___"
    vectorized_string = vectorizer.transform([text])
    if svm_model.predict(vectorized_string)[0] == 0:
        return 0
    else:
        return 1

# visualize(df)
# r = get_input("hello")

#To do:
#get more email data, do twitter and facebook create GUI, implement aws polly, aws transcribe




