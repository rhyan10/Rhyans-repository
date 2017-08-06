from bs4 import BeautifulSoup as bs
import urllib2,lxml,urlparse,sys,datetime
import MySQLdb as sql
import pandas as pd
import json


def visualise_stock(stock_name, start_date, end_date, type):
    return 0
def connect_to_database():
    db = sql.connect(host="127.0.0.1",user ="Dataspartan", passwd = "littledataspartan", db = "stock")
    return db
def retrievesymbols():
    r = urllib2.urlopen('http://www.nasdaq.com/markets/most-active.aspx').read()
    soup = bs(r)
    symbols = []
    for row in soup.findAll('h3'):
        symbol = row.find(text = True)
        if "NASDAQ" not in symbol:
            symbols.append(symbol)
        else:
            pass
    return symbols
def input_to_table():
    db = connect_to_database()
    stockdb = db.cursor()
    symbols = retrievesymbols()
    #print(symbols)
    for name in symbols:
        print name
        csvlink = "http://www.google.co.uk/finance/historical?q=NASDAQ%3A"+name+"&start=0&num=31&output=csv"
        mycsvfile = pd.read_csv(csvlink)
        #print mycsvfile
        for i, row in mycsvfile.iterrows():
            newdateformat = changingdateformat(row[0])
            stockdb.execute("INSERT INTO StockData (StockName,Daate,Open,High,Low,Close,Volume) VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,newdateformat,row[1],row[2],row[3],row[4],row[5]))
            db.commit()
def changingdateformat(date):
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
def createtable():
    db = connect_to_database()
    stockdb = db.cursor()
    sqlcode = """ CREATE TABLE StockData (ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, StockName VARCHAR(10), Daate DATE,Open FLOAT,High FLOAT,Low FLOAT,Close FLOAT,Volume BIGINT); """
    stockdb.execute(sqlcode)
def modifytable():
    pass






#names = soup.find_all('h3')
#print(pd.read_csv('http://www.google.co.uk/finance/historical?q=NASDAQ%3AGOOGL&start=30&num=30&output=csv'))
