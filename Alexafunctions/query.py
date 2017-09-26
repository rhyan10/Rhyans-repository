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
    def totalaverage(self,name):
        stockdb = db.cursor()
        sql = "SELECT AVG((0.5)*(Open+Close)) FROM stockaffluentdata WHERE stockname = %s;"
        stockdb.execute(sql,(name))
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
    def createview():
        stockdb = db.cursor()
        sql = """create view deviation as
        select stockaffluentdata.StockName,power(sum((power((stockcount - ((0.5)*(open + close))),2)))/count(power((stockcount - ((0.5)*(open + close))),2) ),0.5) as standarddeviation
        from stockaffluentdata, tempstock
        where stockaffluentdata.StockName = tempstock.stockname
        group by stockaffluentdata.StockName;"""
        stockdb.execute(sql)
        db.commit()
    def getdata(self):
        stockdb = db.cursor()
        sql = "SELECT * from deviation"
        stockdb.execute(sql)
        result = stockdb.fetchall()
        myresult = dict(result)
        return myresult
    def leastvolatile(self):
        listofsd = self.getdata()
        mylist = list(listofsd)
        removelist = []
        for i in listofsd:
                if listofsd[i] == 0:
                    removelist.append(i)
                else:
                    pass
        for i in removelist:
            del listofsd[i]
        minimum = ""
        for i in listofsd:
            if listofsd[i] == min(listofsd.values()):
                minimum = i
            else:
                pass
        x=np.load('namesandtickersdictionary.npy') #
        dici = dict(enumerate(x.flatten()))
        dic = dici[0]
        for u in dic:
            if dic[u] == minimum :
                return u
            else:
                pass
    def mostvolatile(self):
        listofsd = self.getdata()
        mylist = list(listofsd)
        removelist = []
        for i in listofsd:
                if listofsd[i] == 0:
                    removelist.append(i)
                else:
                    pass
        for i in removelist:
            del listofsd[i]
        minimum = ""
        for i in listofsd:
            if listofsd[i] == max(listofsd.values()):
                minimum = i
            else:
                pass
        x=np.load('namesandtickersdictionary.npy') #
        dici = dict(enumerate(x.flatten()))
        dic = dici[0]
        for u in dic:
            if dic[u] == minimum :
                return u
            else:
                pass
    def simplefunctions(self,ticker,function,valuetype, start,end):
        abre = ''
        if function == 'maximum':
            abre = 'MAX'
        elif function == 'minimum':
            abre = 'MIN'
        else:
            abre = 'AVG'
        stockdb = db.cursor()
        print abre
        print valuetype
        print start
        print ticker
        print end
        # sql = "SELECT %s(%s) FROM stockaffluentdata WHERE daate BETWEEN %s AND %s AND stockname = %s;"
        sql = "SELECT "+abre+"("+str(valuetype)+") FROM stockaffluentdata WHERE daate BETWEEN '"+start+"' AND '"+end+"' AND stockname = '"+ticker+"';"
        print sql
        # stockdb.execute(sql,(abre,valuetype,str(start),str(end),ticker))
        stockdb.execute(sql)
        result = stockdb.fetchall()
        db.commit()
        return result
    def getdeviation(self,ticker):
        stockdb = db.cursor()
        sql = "SELECT standarddeviation FROM deviation WHERE stockname = %s;"
        stockdb.execute(sql,(ticker))
        result = stockdb.fetchall()
        db.commit()
        return result
        #this = realdict['AGN']
        #this[0]
