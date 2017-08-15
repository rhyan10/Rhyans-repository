from sklearn.ensemble import RandomForestClassifier as rfc
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
train_data = pd.read_csv('bitcointrain.csv.csv')
random_forest = rfc(n_estimators = 100, random_state = 10)
x = train_data[train_data.columns[1:5]]
y = train_data[train_data.columns[[-1]]].values.ravel()
random_forest.fit(x,y)
test_data = pd.read_csv('bitcointest.csv')
x_test = test_data[test_data.columns[1:5]]
y = random_forest.predict(x_test)
print test_data[test_data.columns[-1]]
print y
