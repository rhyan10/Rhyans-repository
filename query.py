import urllib2,lxml,urlparse,sys,datetime
import pymysql as sql
import pandas as pd
import json
import numpy as np
from stockssqldatabase import database
data = database()
db = sql.connect(host="127.0.0.1",user ="Dataspartan", passwd = "littledataspartan", db = "stock")
class Queries():
    def getdict(name):
        x=np.load('namesandtickersdictionary.npy')
        dici = dict(enumerate(x.flatten()))
        dic = dici[0]
        name = search(dic,'Multiband')
        ticker = dic[name]
        return ticker
    def search(values, searchFor):
        for k in values:
            for v in values[k]:
                if searchFor in v:
                    return k
        return k
