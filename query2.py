import urllib2,lxml,urlparse,sys,datetime
import MySQLdb as sql
import pandas as pd
import json
import numpy as np
from stockssqldatabase import Database
data = Database()
db = sql.connect(host="192.168.1.23", port = 3306, user ="Dataspartan", passwd = "littledataspartan", db = "stock")
#class Queries():
def getdict(name):
    x=np.load('namesandtickersdictionary.npy')
    dici = dict(enumerate(x.flatten()))
    dic = dici[0]
    name = search(dic,name)
    ticker = dic[name]
    return ticker
def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return k

def avg_shares(name, start_date, end_date,):
    stockdb = db.cursor()
    sql = "SELECT AVG(0.5)*(Open-Close) FROM stockaffluentdata WHERE stockname = %s WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (start_date, end_date))
    result = stockdb.fetchall()
    db.commit()
    return results

def min_shares(name, start_date, end_date,):
    stockdb = db.cursor()
    sql = "SELECT MAX(Open-Close) FROM stockaffluentdata WHERE stockname = %s WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (start_date, end_date))
    result = stockdb.fetchall()
    db.commit()
    return results

def max_shares(name, start_date, end_date,):
    stockdb = db.cursor()
    sql = "SELECT MIN(Low) FROM stockaffluentdata WHERE stockname = %s WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (start_date, end_date))
    result = stockdb.fetchall()
    db.commit()
    return results
