import pandas as pd
import numpy as np
from stop_words import get_stop_words
from sklearn import feature_extraction as fe
import pickle as pickle


# A class that provides text utility functions
class TextUtilities():


        # given a input list of words
        # it returns a matrix with stop words removed


    def load_input_file(number_of_rows=10):
        print("Start loading file")
        train_csv = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding='latin-1', delimiter=',', quotechar='"')
        train_csv[:100000]
        tweets = train_csv[train_csv.columns[-1]]
        rating = train_csv[train_csv.columns[0]]
        array_of_tweets = []
        ratings_array = []
        # k = 0
        # while k < 10000
        # :
        #    jk = tweets[k]
        #    array_of_tweets.append(jk)
        #    yk = rating[k]
        #    ratings_array.append(yk)
        #    k = k + 1
        for i in tweets:
            array_of_tweets.append(i)
        for k in rating:
            ratings_array.append(k)
        print("End loading file")
        return array_of_tweets, ratings_array

    def TexttoNumericalconversion(self, mylist):
        cv = fe.text.CountVectorizer()
        numerical = cv.fit_transform(mylist)
        gg = cv.get_feature_names()
        PIK = 'featuresnames.pkl'
        print(numerical)
        with open(PIK, 'wb') as f:
            pickle.dump(gg, f)
        return numerical.np.asarray()

    def removestopwords(self):
        print("Start removing stopwords")
        input_list, rating_array = self.load_input_file()
        stopwords = get_stop_words("english")
        newlist = []
        for index, sentence in enumerate(input_list):
            joinlist = []
            list_of_words = sentence.split(" ")
            print(index)
            for word in list_of_words:
                if word in stopwords:
                    pass
                else:
                    joinlist.append(word)
            newlist.append(" ".join(joinlist))
        matrix = self.TexttoNumericalconversion(newlist)
        print("Finish removing stopwords")
        return rating_array, matrix

from vectorsation import TextUtilities

n_bytes = 2**31
max_bytes= 2**31 - 1
data = bytearray(n_bytes)

Tex = TextUtilities()
rating_array, array_of_tweet = Tex.removestopwords()
PIKl = 'arrayoftweet.pkl'
bytes_out = pickle.dumps(data)

with open(PIKl, 'wb') as f_out:
    for idx in range(0, n_bytes, max_bytes):
        f_out.write(bytes_out[idx:idx+max_bytes])
        #pickle.dump(array_of_tweet, f_out)

n_bytes = 2**31
max_bytes= 2**31 - 1
data = bytearray(n_bytes)
bytes_out = pickle.dumps(data)

PK = 'ratingarray.pkl'

with open(PK, 'wb') as f_out:
    for idx in range(0, n_bytes, max_bytes):
        f = f_out.write(bytes_out[idx:idx+max_bytes])
        #pickle.dump(rating_array, f_out)
