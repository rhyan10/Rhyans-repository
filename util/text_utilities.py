from stop_words import get_stop_words
from sklearn import feature_extraction as fe

# A class that provides text utility functions
class TextUtilities():

    # given a input list of words
    # it returns a matrix with stop words remvoed
    def removestopwords(self, input_list):
        print "Start removing stopwords"
        stopwords = get_stop_words('english')
        newlist = []
        for index, sentence in enumerate(input_list):
            print str(index)+": "+sentence
            joinlist = []
            list_of_words = sentence.split(" ")
            for word in list_of_words:
                if word in stopwords:
                    pass
                else:
                    joinlist.append(word)
            newlist.append(" ".join(joinlist))
        matrix = self.TexttoNumericalconversion(newlist)
        print "Finish removing stopwords"
        return matrix


    def TexttoNumericalconversion(self,mylist):
        cv = fe.text.CountVectorizer()
        numerical = cv.fit_transform(mylist)
        # print len(numerical.toarray())
        return numerical.toarray()