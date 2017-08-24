import pandas as pd
import numpy as np
from stop_words import get_stop_words
from sklearn import feature_extraction as fe
import cPickle as pickle
# A class that provides text utility functions
class TextUtilities():

    # given a input list of words
    # it returns a matrix with stop words remvoed
    def removestopwords(self):
        print "Start removing stopwords"
        input_list, rating_array = self.load_input_file()
        stopwords = get_stop_words('english')
        newlist = []
        for index, sentence in enumerate(input_list):
            joinlist = []
            list_of_words = sentence.split(" ")
            print index
            for word in list_of_words:
                if word in stopwords:
                    pass
                else:
                    joinlist.append(word)
            newlist.append(" ".join(joinlist))
        matrix = self.TexttoNumericalconversion(newlist)
        print "Finish removing stopwords"
        return rating_array, matrix

    def load_input_file(number_of_rows=10):
        print "Start loading file"
        train_csv = pd.read_csv('training.1600000.processed.noemoticon.csv')
        tweets = train_csv[train_csv.columns[-1]]
        rating = train_csv[train_csv.columns[0]]
        array_of_tweets = []
        ratings_array = []
        k = 0
        while k < 10000:
            jk = tweets[k]
            array_of_tweets.append(jk)
            yk = rating[k]
            ratings_array.append(yk)
            k = k + 1
        #for i in tweets:
        #    array_of_tweets.append(i)
        #for i in rating:
        #    ratings_array.append(i)

        print "End loading file"
        return array_of_tweets, ratings_array

    def TexttoNumericalconversion(self,mylist):
        cv = fe.text.CountVectorizer()
        numerical = cv.fit_transform(mylist)
        gg = cv.get_feature_names()
        PIK = 'featuresnames.pkl'
        print numerical
        with open(PIK, 'wb') as f:
            pickle.dump(gg, f)
        return numerical.toarray()
from vectorsation import TextUtilities
Tex = TextUtilities()
array_of_tweet, rating_array = Tex.removestopwords()
PIKl = 'arrayoftweet.pkl'
with open(PIKl, 'wb') as f:
    pickle.dump(array_of_tweet, f)
PK = 'ratingarray.pkl'
with open(PK, 'wb') as f:
    pickle.dump(rating_array, f)
