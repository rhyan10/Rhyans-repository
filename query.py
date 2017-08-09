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
        for k in dic:
            o = k.lower()
            if name in o:
                return dic[k]
            elif name == o:
                return dic[k]
            else:
                pass
    def avg_shares(self,name, start_date, end_date,):
        stockdb = db.cursor()
        sql = "SELECT AVG((0.5)*(Open+Close)) FROM stockaffluentdata WHERE stockname = %s AND daate BETWEEN %s AND %s;"
        stockdb.execute(sql,(name,start_date, end_date))
        result = stockdb.fetchall()
        return result
        db.commit()

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
    def saveaveragedata(self):
        x=np.load('namesandtickersdictionary.npy') #
        dici = dict(enumerate(x.flatten()))
        dic = dici[0]
        stockdb = db.cursor()
        standarddeviationlist = []
        namelist = []
        numberlist = []
        i = 0
        for k in dic.items():
            name = k[0]
            namelist.append(self.getdict(name)) #A
            sql = "SELECT AVG((0.5)*(Open+Close)) FROM stockaffluentdata WHERE stockname = %s group by stockname;"
            stockdb.execute(sql,(namelist[i]))
            result = stockdb.fetchall()
            try:
                numberlist.append(result[0])
                print result[0]
            except IndexError:
                pass
            i = i+1
        averagesdict = dict(zip(namelist,numberlist))
        np.save("Averagedictionary.npy",averagesdict)
    def leastrisky(self):
        stockdb = db.cursor()
        dicti = np.load("Averagedictionary.npy")
        dic = dict(enumerate(dicti.flatten()))
        realdict = dic[0]
        for i in realdict:
            sql = "SELECT (0.5)*(Open+close) FROM stockaffluentdata WHERE stockname = %s;"
            stockdb.execute(sql,i)
            result = stockdb.fetchall()
            try:
                type(str(result[0]))
                for a in list(result):
                    pass
            except:
                pass
        #this = realdict['AGN']
        #this[0]
from query import Queries
qr = Queries()
print qr.leastrisky()
