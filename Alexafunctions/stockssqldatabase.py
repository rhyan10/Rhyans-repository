from bs4 import BeautifulSoup as bs
import urllib2,lxml,urlparse,sys,datetime
import pymysql as sql
import numpy as np
import pandas as pd
import json
import requests as rq
db = sql.connect(host="127.0.0.1",user ="Dataspartan", passwd = "littledataspartan", db = "stock")
class database():
    def retrievesymbolsmk2(self):
        olumn = pd.read_csv("https://s3.amazonaws.com/quandl-static-content/Ticker+CSV%27s/secwiki_tickers.csv")
        column = olumn['Ticker']
        tickers = []
        for row in column:
            tickers.append(row)
        return tickers
    def retrievesymbols(self):
            r = urllib2.urlopen('http://www.nasdaq.com/markets/most-active.aspx').read()
            soup = bs(r)
            symbols = []
            for row in soup.findAll('h3'):
                symbol = row.find(text = True)
                print(symbol)
                if "NASDAQ" not in symbol:
                    symbols.append(symbol)
                else:
                    pass

            return symbols
    def input_to_table(self):
        stockdb = db.cursor()
        data = database()
        symbols = data.retrievesymbolsmk2()
        olumn = pd.read_csv("https://s3.amazonaws.com/quandl-static-content/Ticker+CSV%27s/secwiki_tickers.csv")
        #print(symbols)
        tickerlist = []
        namelist = []
        sectorlist = []
        namecolumn = olumn['Name']
        sectorcolumn = olumn['Sector']
        p = 0
        for name in symbols:
            print name
            try:
                csvlink = "http://www.google.co.uk/finance/historical?q=NASDAQ%3A"+name+"&start=0&num=61&output=csv"
                mycsvfile = pd.read_csv(csvlink)
                for i, row in mycsvfile.iterrows():
                    newdateformat = data.changingdateformat(row[0])
                    stockdb.execute("INSERT INTO StockAffluentData (StockName,Daate,Open,High,Low,Close,Volume) VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,newdateformat,row[1],row[2],row[3],row[4],row[5]))
                    db.commit()
                tickerlist.append(name)
                namelist.append(namecolumn[p])
                sectorlist.append(sectorcolumn[p])
            except Exception:
                pass
            p = p + 1
        mydict = dict(zip(namelist,tickerlist))
        #np.save('namesandtickersdictionary.npy', mydict)
    def changingdateformat(self,date):
        mydate = None
        listofdateparts = date.split('-')
        if listofdateparts[1] == "Jan":
            mydate = 01
        elif listofdateparts[1] == "Feb":
            mydate = 02
        elif listofdateparts[1] == "Mar":
            mydate = 03
        elif listofdateparts[1] == "Apr":
            mydate = 04
        elif listofdateparts[1] == "May":
            mydate = 05
        elif listofdateparts[1] == "Jun":
            mydate = 06
        elif listofdateparts[1] == "Jul":
            mydate = 07
        elif listofdateparts[1] == "Aug":
            mydate = int("08")
        elif listofdateparts[1] == "Sep":
            mydate = int("09")
        elif listofdateparts[1] == "Oct":
            mydate = 10
        elif listofdateparts[1] == "Nov":
            mydate = 11
        elif listofdateparts[1] == "Dec":
            mydate = 12
        lost = [listofdateparts[0],str(mydate),listofdateparts[2]]
        opo = "-".join(lost)
        return datetime.datetime.strptime(opo, '%d-%m-%y').strftime('%y-%m-%d')
    def createtable(self):
        stockdb = db.cursor()
        sqlcode = """ CREATE TABLE StockAffluentData (ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, StockName VARCHAR(10), Daate DATE,Open FLOAT,High FLOAT,Low FLOAT,Close FLOAT,Volume BIGINT); """
        stockdb.execute(sqlcode)
    def changingyear(self,date):
        date = str(date)
        parts = date.split('-')
        newparts = ['2017',parts[1],parts[2]]
        return "-".join(newparts)


#print (pd.read_csv("https://s3.amazonaws.com/quandl-static-content/Ticker+CSV%27s/secwiki_tickers.csv"))
#names = soup.find_all('h3')
#print(pd.read_csv('http://www.google.co.uk/finance/historical?q=NASDAQ%3AGOOGL&start=30&num=30&output=csv'))
