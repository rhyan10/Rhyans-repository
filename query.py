import urllib2,lxml,urlparse,sys,datetime
import pymysql as sql
import pandas as pd
import json
import numpy as np
from stockssqldatabase import database
from math import isnan
data = database()
db = sql.connect(host="127.0.0.1",user ="Dataspartan", passwd = "littledataspartan", db = "stock")
class Queries():
    def getdict(self,name):
        x=np.load('namesandtickersdictionary.npy') #
        dici = dict(enumerate(x.flatten()))
        dic = dici[0]
        name = name.lower()
        for k in dic.items():
            j = k[0]
            o = j.lower()
            if name in o:
                return dic[k[0]]
            else:
                pass
    def avg_shares(self,name, start_date, end_date,):
        stockdb = db.cursor()
        sql = "SELECT AVG((0.5)*(Open+Close)) FROM stockaffluentdata WHERE stockname = %s AND daate BETWEEN %s AND %s;"
        stockdb.execute(sql,(name,start_date, end_date))
        result = stockdb.fetchall()
        db.commit()
        return result

    def min_shares(self,name, start_date, end_date,):
        stockdb = db.cursor()
        sql = "SELECT MAX((0.5)*(Open+Close)) FROM stockaffluentdata WHERE stockname = %s AND daate BETWEEN %s AND %s;"
        stockdb.execute(sql,(name,start_date, end_date))
        result = stockdb.fetchall()
        db.commit()
        return result

    def max_shares(self,name, start_date, end_date,):
        stockdb = db.cursor()
        sql = "SELECT MIN(Low) FROM stockaffluentdata WHERE stockname = %s AND daate BETWEEN %s AND %s;"
        stockdb.execute(sql,(name,start_date, end_date))
        result = stockdb.fetchall()
        db.commit()
        return result

#x=np.load('namesandtickersdictionary.npy')
#dici = dict(enumerate(x.flatten()))
#dic = dici[0]
#for i in dic:
#    print i
