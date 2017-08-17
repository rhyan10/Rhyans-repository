import pandas as pd
import numpy as np
from util.text_utilities import TextUtilities


def load_input_file(input_file_path = 'datasets/training.1600000.processed.noemoticon.csv', number_of_rows=10):
    print "Start loading file"
    train_csv = pd.read_csv('datasets/training.1600000.processed.noemoticon.csv')
    tweets = train_csv[train_csv.columns[-1]]
    rating = train_csv[train_csv.columns[0]]

    array_of_tweets = []
    ratings_array = []
    for i in tweets:
        array_of_tweets.append(i)
    for i in rating:
        ratings_array.append(i)
    k = 0
    while k < number_of_rows:
        array_of_tweets.append(tweets[k])
        ratings_array.append(rating[k])
        k = k + 1
    print "End loading file"
    return array_of_tweets, ratings_array



if __name__ == '__main__':
    print "Start twitter sentimental analysis"
    array_of_tweets, ratings_array = load_input_file()
    text_utilities = TextUtilities()

    df = pd.DataFrame(data=np.column_stack((ratings_array, text_utilities.removestopwords(array_of_tweets))),
                      columns=['SentimentRating', 'Tweet'])
    # df.to_csv('ratingsandtweets.csv')
