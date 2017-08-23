import pandas as pd
import os

class Create_training_data_splits():

    global df
    df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding='latin-1', delimiter=',', quotechar='"')
    global names_array
    names_array = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af']
            
    def create_csv(passwrd):
        print('Splitting list into 32 parts... password is: ' + passwrd)

        #df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding='latin-1', delimiter=',', quotechar='"') 
        '''        
        for i in range(1, 33): #for name in names_array:
            start = 'Processing file {}...'.format(i)
            print (start)
            
            j = i-1
            indexer_name_variable = names_array[j]
            
            index_now = df[(50000*i)]
            index_previous = df[(50000*j)]
            
            new_df = index_now - index_previous
            
            index_using = 'Using index of {}'.format(indexer_name_variable)
            print(index_using)
            
            indexer_name_variable.to_csv("trainingdata_part{}".format(i), mode ='w', header=None, index=None)
            
            complete = 'Finished processing file {}...'.format(i)
            print (complete)    
        '''

        '''
        for i in range(1,33):
            for k in  
            df.iterrows()

            j = i-1

            main_value = 50000*i # 50000*1 = 50000
            lag_value = 50000*j  # 50000*0 = 0
        '''

        var = df.drop(df.index[5:10])           

        print(var)

        print ("All done!")
