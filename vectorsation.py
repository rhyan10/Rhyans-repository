import pandas as pd
import numpy as np
train_csv = pd.read_csv('training.1600000.processed.noemoticon.csv')
tweets = train_csv[train_csv.columns[-1]]
rating = train_csv[train_csv.columns[0]]
arrayoftweets = []
ratingsarray = []
for i in tweets:
    arrayoftweets.append(i)
for i in rating:
   ratingsarray.append(i)
k =0
while k < 200:
    ratingsarray.append(rating[k])
    arrayoftweets.append(tweets[k])
    k = k +1

 #Columns 0 and 6 contain the relevant data for the tweet and the emotion assciated with it
#sklearn.feature_extraction.text.CountVectorizer
from sklearn import feature_extraction as fe
class nltk():
    def removestopwords(self,text):
        from stop_words import get_stop_words
        stopwords = get_stop_words('english')
        newlist = []
        j = 0
        for l in text:
            print j
            joinlist = []
            stringlist = l.split(" ")
            for i in stringlist:
                if i in stopwords:
                    pass
                else:
                    joinlist.append(i)
            newlist.append(" ".join(joinlist))
            j = j +1
        matrix = self.TexttoNumericalconversion(newlist)
        print matrix[0]
        return matrix
    def TexttoNumericalconversion(self,mylist):
        cv = fe.text.CountVectorizer()
        numerical = cv.fit_transform(mylist)
        print len(numerical.toarray())
        return numerical.toarray()
from convertingdata import nltk
nlt = nltk()
df = pd.DataFrame(data=np.column_stack((ratingsarray,nlt.removestopwords(arrayoftweets))),columns=['SentimentRating','Tweet'])
#df.to_csv('ratingsandtweets.csv')
